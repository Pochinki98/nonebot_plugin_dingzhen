"""
@Author         : Noobie III
@Date           : 2025-01-04 19:00:09
@LastEditors    : Noobie III
@LastEditTime   : 2025-03-06 15:17:20
@Description    : Dingzhen's Voice plugin
@GitHub         : https://github.com/Pochinki98
"""

__author__ = "Noobie III"



from nonebot.plugin import PluginMetadata, require

require("nonebot_plugin_localstore")

__plugin_meta__ = PluginMetadata(
    name="丁真语音生成器",
    description="一款丁真语音生成器，用于合成丁真语音并发送",
    usage="发送“丁真/丁真说 XX”即可命令机器人合成一段丁真语音并发出",
    type="application",
    homepage="https://github.com/Pochinki98/nonebot_plugin_dingzhen",
    supported_adapters={"~onebot.v11"},
)

from .dingzhen import speak
