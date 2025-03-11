# dingzhen.py

import json
import httpx
import random
from nonebot import on_command
from nonebot import logger
from nonebot.adapters.onebot.v11 import MessageSegment, Message, Bot
from nonebot.params import CommandArg
from nonebot_plugin_localstore import get_plugin_cache_dir
from nonebot.exception import FinishedException



speak = on_command("speak", aliases={"丁真说", "丁真"}, block=True)

# 使用 localstore 获取缓存目录
temp_dir = get_plugin_cache_dir()

@speak.handle()
async def handle_speak(
    bot: Bot,
    args: Message = CommandArg()
):
    wav_path = ""
    try:
        args_text = args.extract_plain_text().strip()
        logger.info(f"收到用户输入的文本: '{args_text}'")
        
        if not args_text:
            logger.warning("用户未提供文本")
            await speak.send("请提供要转换为语音的文本，例如：丁真说 这是雪豹")
            return

        text = args_text
        await speak.send("稍等片刻…")

        url = "https://midd1eye-dz-bert-vits2.ms.show/run/predict"
        headers = {"Content-Type": "application/json"}
        data = {
            "data": [text, "Speaker", 1, 1.0, 0.9, 0.9],
            "event_data": None,
            "fn_index": 0,
            "dataType": ["textbox", "dropdown", "slider", "slider", "slider", "slider"],
            "session_hash": "caonimade"
        }

        async with httpx.AsyncClient(timeout=20.0) as client:
            try:
                response = await client.post(url, headers=headers, data=json.dumps(data))
                if response.status_code != 200:
                    logger.error(f"请求失败, 状态码: {response.status_code}")
                    await speak.send(f"请求失败, 状态码: {response.status_code}")
                    return

                response_data = response.json()
                name_field = response_data['data'][1]['name']
                file_url = f"https://midd1eye-dz-bert-vits2.ms.show/file={name_field}"

                # 使用 localstore 的缓存目录生成文件路径
                random_filename = f"{random.randint(10000000, 99999999)}.wav"
                wav_path = temp_dir / random_filename
                
                # 下载文件
                wav_response = await client.get(file_url)
                if wav_response.status_code != 200:
                    logger.error(f"无法下载音频文件, 状态码: {wav_response.status_code}")
                    await speak.send(f"无法下载音频文件, 状态码: {wav_response.status_code}")
                    return
                
                # 保存文件
                wav_path.write_bytes(wav_response.content)
                logger.info(f"成功下载并保存语音文件: {wav_path}")

                # 发送语音消息
                await speak.send(MessageSegment.record(str(wav_path)))

            except httpx.RequestError as e:
                logger.error(f"网络请求错误: {e}")
                await speak.send(f"网络请求错误: {e}")
                return
            except json.JSONDecodeError as e:
                logger.error(f"JSON解析错误: {e}")
                await speak.send(f"服务器响应格式错误")
                return
            except Exception as e:
                logger.error(f"处理过程中发生错误: {e}")
                await speak.send(f"处理过程中发生错误: {e}")
                return
    
    except FinishedException:
        pass
    except Exception as e:
        logger.error(f"未预期的错误: {e}")
        await speak.send("发生未知错误，请稍后再试")
    
    finally:
        # 删除临时文件
        if wav_path and wav_path.exists():
            try:
                wav_path.unlink()
                logger.info(f"成功删除临时文件: {wav_path}")
            except Exception as e:
                logger.warning(f"删除临时文件失败: {e}")

