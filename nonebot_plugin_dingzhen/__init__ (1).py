from nonebot.plugin import PluginMetadata, require

require("nonebot_plugin_localstore")

__plugin_meta__ = PluginMetadata(
    name="丁真语音生成器",
    description="一款丁真语音生成器，用于合成丁真语音并发送",
    usage="发送“丁真说 XX”即可命令机器人合成一段丁真语音并发出",
    type="application",
    homepage="https://github.com/Pochinki98/nonebot_plugin_dingzhen",
    supported_adapters={"~onebot.v11"},
)

from .dingzhen import speak
