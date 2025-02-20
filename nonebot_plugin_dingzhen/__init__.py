"""
@Author         : Noobie III
@Date           : 2025-01-04 19:00:09
@LastEditors    : Noobie III
@LastEditTime   : 2025-02-20 15:00:00
@Description    : Dingzhen's Voice plugin
@GitHub         : https://github.com/Pochinki98
"""

__author__ = "Noobie III"


import os
import json
import httpx
import aiofiles
import logging
import random
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import MessageSegment, Message
from nonebot.typing import T_State
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="丁真语音生成器",
    description="一款丁真语音生成器，用于合成丁真语音并发送",
    usage="发送“丁真说 XX”即可命令机器人合成一段丁真语音并发出",
    type="application",
    homepage="https://github.com/Pochinki98/nonebot_plugin_dingzhen",
    supported_adapters={"~onebot.v11"},
)

# 配置日志
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  # 配置日志级别

speak = on_command("speak", aliases={"丁真说", "丁真"}, priority=5, block=True)

# 获取插件的当前目录
plugin_dir = os.path.dirname(__file__)
temp_dir = os.path.join(plugin_dir, "temp")

# 确保 temp 目录存在，如果不存在则创建
try:
    os.makedirs(temp_dir, exist_ok=True)
    logger.info(f"成功创建或确认 temp 目录存在: {temp_dir}")
except Exception as e:
    logger.error(f"创建 temp 目录失败: {e}")

@speak.handle()
async def handle_speak(
    bot: Bot,
    event: Event,
    state: T_State,
    args: Message = CommandArg()  # 正确的类型声明
):
    wav_path = ""  # 初始化 wav_path 以确保在 finally 块中可访问
    try:
        # 提取用户输入的文本
        args_text = args.extract_plain_text().strip()
        logger.info(f"收到用户输入的文本: '{args_text}'")
        
        if not args_text:
            logger.warning("用户未提供文本")
            await speak.finish("请提供要转换为语音的文本，例如：/丁真说 你好世界")
        
        text = args_text
        logger.debug(f"处理的文本: '{text}'")

        # 立即回复“稍等片刻...”
        await speak.send("稍等片刻…")
        logger.info("已发送回复: '稍等片刻…'")

        # 请求的URL
        url = "https://midd1eye-dz-bert-vits2.ms.show/run/predict"
        logger.info(f"语音生成 API URL: {url}")

        # 请求的头部
        headers = {
            "Content-Type": "application/json"
        }
        logger.debug(f"请求头部: {headers}")

        # 请求体
        data = {
            "data": [text, "Speaker", 1, 1.0, 0.9, 0.9],
            "event_data": None,
            "fn_index": 0,
            "dataType": ["textbox", "dropdown", "slider", "slider", "slider", "slider"],
            "session_hash": "caonimade"
        }
        logger.debug(f"请求体数据: {data}")

        # 发送 POST 请求，设置超时为 20 秒
        async with httpx.AsyncClient(timeout=20.0) as client:
            try:
                logger.info(f"发送 POST 请求到 {url}")
                response = await client.post(url, headers=headers, data=json.dumps(data))
                logger.info(f"收到响应, 状态码: {response.status_code}")
            except httpx.RequestError as e:
                logger.error(f"请求失败: {e}")
                await speak.finish(f"请求失败: {e}")

        # 检查响应状态码
        if response.status_code != 200:
            logger.error(f"请求失败, 状态码: {response.status_code}")
            await speak.finish(f"请求失败, 状态码: {response.status_code}")

        # 解析响应数据
        try:
            response_data = response.json()
            logger.debug(f"响应 JSON 数据: {response_data}")
            name_field = response_data['data'][1]['name']
            logger.debug(f"从响应中提取的文件路径: '{name_field}'")
            
            # 构建下载URL，确保 'name' 包含完整路径
            file_url = f"https://midd1eye-dz-bert-vits2.ms.show/file={name_field}"
            logger.info(f"生成的语音文件下载 URL: {file_url}")

            # 生成随机八位数字作为文件名
            random_filename = f"{random.randint(10000000, 99999999)}.wav"
            wav_path = os.path.join(temp_dir, random_filename)
            logger.debug(f"本地保存的文件路径: '{wav_path}'")
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            logger.error(f"解析响应数据失败: {e}")
            await speak.finish(f"错误: 无法提取文件 URL. {e}")

        # 下载 WAV 文件，设置超时为 20 秒
        try:
            async with httpx.AsyncClient(timeout=20.0) as client:
                logger.info(f"下载语音文件从 {file_url}")
                wav_response = await client.get(file_url)
                logger.info(f"下载语音文件响应状态码: {wav_response.status_code}")
                if wav_response.status_code != 200:
                    logger.error(f"无法下载音频文件, 状态码: {wav_response.status_code}")
                    await speak.finish(f"无法下载音频文件, 状态码: {wav_response.status_code}")
                
                # 确保父目录存在（虽然本地只保存到 temp_dir，通常不需要，但为了安全）
                parent_dir = os.path.dirname(wav_path)
                os.makedirs(parent_dir, exist_ok=True)
                logger.debug(f"确保父目录存在: {parent_dir}")
                
                # 将内容写入临时文件
                async with aiofiles.open(wav_path, 'wb') as f:
                    await f.write(wav_response.content)
                    logger.info(f"成功下载并保存语音文件: {wav_path}")
        except httpx.RequestError as e:
            logger.error(f"下载音频文件失败: {e}")
            await speak.finish(f"下载音频文件失败: {e}")
        except Exception as e:
            logger.error(f"保存音频文件失败: {e}, 尝试保存路径: {wav_path}")
            await speak.finish(f"保存音频文件失败: {e}")

        # 发送语音消息
        await speak.finish(MessageSegment.record(wav_path))
    
    finally:
        # 确保临时文件被删除
        if wav_path and os.path.exists(wav_path):
            try:
                os.remove(wav_path)
                logger.info(f"成功删除临时文件: {wav_path}")
            except Exception as e:
                logger.warning(f"删除临时文件失败: {e}")
