<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://v2.nonebot.dev/logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
</div>

<div align="center">

# nonebot_plugin_dingzhen（暂未上线）

_✨ 一款不怎么优秀的丁真语音生成器。 ✨_


<p align="center">
  <a href="https://raw.githubusercontent.com/cscs181/QQ-Github-Bot/master/LICENSE">
    <img src="https://img.shields.io/github/license/cscs181/QQ-Github-Bot.svg" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot_plugin_dingzhen">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-status.svg" alt="pypi">
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

_别否认，别纳闷，一定还会有下一个丁真。_

## 💿 安装  

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
  
  PS: 请查看你env中起始符的配置(默认```/```)  
  1. API图片系统(图片系统)  
  2. API文字系统(文字系统)
  3. API站点系统(站点系统)



## 📝 更新日志

<details>
<summary>展开/收起</summary>

### 1.1.0

- 站点代码重写更新  

### 1.0.7

- 优化更新  

### 1.0.6

- 维护更新，蟒蛇(Python)版本要求最低改为3.10  

### 1.0.5

- 修复ip查询中的致命语法错误  

### 1.0.4

- 更换稳定API, 修复部分Bug  

</details>
<div align="center">
  <a href="https://cqu.edu.cn"><img src="https://www2.cqu.edu.cn/Uploads/CQUmain/nowvi.png" width="227.2" height="71.7" alt="CQUlogo"></a>
  <br>
</div>
