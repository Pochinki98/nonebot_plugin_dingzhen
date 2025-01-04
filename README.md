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

## 📖 前言及介绍

PS: 这是我第一次发布插件，没有多少经验，写的也不规范，还望诸位海涵多提issue。
目前实测暂无bug。

## 🔧 开发环境
Nonebot2：2.0.0rc4  
python：3.11.3  
操作系统：Linux（Windows兼容性问题不大）  
编辑器：VS Code

## 💿 安装  

### 1. nb-cli安装（推荐）

在你bot工程的文件夹下，运行cmd/shell（运行路径要对啊），执行nb命令安装插件，插件配置会自动添加至配置文件  
```
nb plugin install nonebot_plugin_dingzhen
```

### 2. pip安装
```
pip install nonebot_plugin_smallapi
```  
打开 nonebot2 项目的 ```bot.py``` 文件, 在其中写入  
```nonebot.load_plugin('nonebot_plugin_smallapi')```  
当然，如果是默认nb-cli创建的nonebot2的话，在bot路径```pyproject.toml```的```[tool.nonebot]```的```plugins```中添加```nonebot_plugin_smallapi```即可  
pyproject.toml配置例如：  
``` 
[tool.nonebot]
plugin_dirs = ["src/plugins"]
plugins = ["nonebot_plugin_smallapi"]
``` 

### 3. 本地安装(不推荐)

仓库没更新，建议nb-cli
将项目clone到你的机器人插件下的对应插件目录内（一般为机器人文件夹下的`src/plugins`），然后把`nonebot_plugin_smallapi`文件夹里的内容拷贝至上一级目录即可。  
clone命令参考（得先装`git`，懂的都懂）：
```
git clone https://github.com/chaichaisi/nonebot_plugin_smallapi.git
``` 
也可以直接下载压缩包到插件目录解压，然后同样提取`nonebot_plugin_smallapi`至上一级目录。  
目录结构： ```你的bot/src/plugins/nonebot_plugin_smallapi/__init__.py```  

### 更新版本
```
nb plugin update nonebot_plugin_dingzhen
```

## 🎉 功能
  
  1. 齐全的API随机图片系统  
  2. 齐全的API随机文本系统  
  3. 好使的网站工具系统

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
  <a href="https://cqu.edu.cn"><img src="https://github.com/haowang-cqu/CQU-Logo/blob/main/%E6%A0%A1%E5%BE%BD/%E6%A0%A1%E5%BE%BD_%E8%93%9D%E8%89%B2_1024x1024.png" width="180" height="180" alt="CQUlogo"></a><br>
  <a href="https://cqu.edu.cn"><img src="https://github.com/haowang-cqu/CQU-Logo/blob/main/%E4%B8%AD%E6%96%87%E6%A0%A1%E5%90%8D/%E4%B8%AD%E6%96%87%E6%A0%A1%E5%90%8D_%E8%93%9D%E8%89%B2_1555x512.png" width="180" height="59.266688" alt="CQUlogo2"></a>
  <br>
</div>

<div align="center">
