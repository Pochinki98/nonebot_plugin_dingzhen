<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://v2.nonebot.dev/logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
</div>

<div align="center">

# nonebot_plugin_dingzhen

_✨ 一款QQ丁真语音生成器 ✨_


<p align="center">
  <a href="https://raw.githubusercontent.com/Pochinki98/nonebot_plugin_dingzhen/master/LICENSE">
    <img src="https://img.shields.io/github/license/Pochinki98/nonebot_plugin_dingzhen.svg" alt="license">
  <a href="https://pypi.python.org/pypi/nonebot_plugin_dingzhen">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_dingzhen.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</p>


</div>

## 🙏 致谢

感谢[MiDd1Eye](https://www.modelscope.cn/profile/MiDd1Eye)提供[语音模型](https://www.modelscope.cn/studios/MiDd1Eye/DZ-Bert-VITS2)。

感谢项目[Bert-VITS2](https://github.com/fishaudio/Bert-VITS2)。

感谢[chaichaisi](https://github.com/chaichaisi/)作为精神支柱。

感谢[丁真](https://bilibili.com/video/BV1Y7SWYpERP)对本项目的贡献。

## 📖 前言

此次是我首次发布插件，写的或有漏缺，或不规范，还望诸位海涵。  
目前实测暂未发现bug。如果发现插件bug或有其他建议的请提issue，感激不尽。

<del>_别否认，别纳闷，一定还会有下一个丁真。_</del>

## 💿 安装  

在开始安装前，请先安装aiofiles。
```
pip install aiofiles
```

### 1. nb-cli安装（推荐）

在bot配置文件同级目录下执行以下命令：
```
nb plugin install nonebot_plugin_dingzhen
```

### 2. pip安装
```
pip install nonebot_plugin_dingzhen
```  
打开 nonebot2 项目的 ```bot.py``` 文件, 在其中写入  
```nonebot.load_plugin('nonebot_plugin_dingzhen')```  
当然，如果是默认nb-cli创建的nonebot2的话，在bot路径```pyproject.toml```的```[tool.nonebot]```的```plugins```中添加```nonebot_plugin_dingzhen```即可。  

### 更新版本
```
nb plugin update nonebot_plugin_dingzhen
```

## 🎉 功能

可以通过语音模型生成一段很像丁真的语音。  

## 👉 命令

```丁真/丁真说/speak 内容```  
如```丁真说 这是雪豹```  

PS: 请查看你env中起始符的配置(默认```/```)。  

## 💡 未来期望

可能会支持修改配置来改变模型生成语音的参数。

## 📝 更新日志

<details>
<summary>展开/收起</summary>  

### 1.2.5.1

- 参照建议除去了一些不必要的函数参数，并修改了优先级
- 调整了插件结构
- 按照要求禁止在插件目录下保存文件，现改为采用[nonebot_plugin_localstore](https://github.com/nonebot/plugin-localstore)插件的方案。

### 1.1 

- 稳定版

### 1.0.0 beta

- 首次上线


</details>

## 
<div align="center">
  <a href="https://cqu.edu.cn"><img src="https://www2.cqu.edu.cn/Uploads/CQUmain/nowvi.png" width="227.2" height="71.7" alt="CQUlogo"></a>
  <br>
</div>
