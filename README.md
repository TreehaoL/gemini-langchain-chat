# Gemini LangChain 本地调用项目

## 项目说明

本项目使用 LangChain 调用 Gemini API，实现控制台连续对话、流式输出和简单上下文记忆。

## 环境要求

- Anaconda 或 Miniconda
- Python
- Gemini API Key

## 安装环境

使用 environment.yml 创建环境：

    conda env create -f environment.yml

激活环境：

    conda activate ai
    
## 一键安装环境（依赖Anaconda）

本项目提供 setup_env.bat，用于自动创建或更新 Conda 环境。

首次使用时，在项目目录下运行：

    setup_env.bat

如果双击无法运行（如环境变量没配好，会找不到命令），请打开 Anaconda Prompt，进入项目目录后执行：

    setup_env.bat

## 配置 API Key

打开 .env文件，然后填写自己的 Gemini API Key。

.env 文件格式如下：

    GOOGLE_API_KEY=你的Gemini API Key

## 运行项目

进入项目目录后运行（或者直接运行run.bat文件）：

    python main.py

程序启动后，可以在控制台输入问题。

输入以下任意内容可以退出对话：

    exit
    quit
    q

## 文件说明

- main.py：程序入口，负责用户输入和循环对话
- llm_config.py：配置 Gemini 模型
- chat_service.py：封装 AI 调用和流式输出
- .env：保存 API Key
- environment.yml：Conda 环境依赖文件
- README.md：项目说明文档
  
## requirements.txt 说明

requirements.txt 用来记录本项目需要安装的 Python 第三方库。

如果使用 pip 安装依赖，可以执行：

    python -m pip install -r requirements.txt

如果使用 Anaconda / Miniconda，更推荐使用 environment.yml 创建环境：

    conda env create -f environment.yml
    conda activate ai

本项目中 requirements.txt 主要包含 LangChain、Gemini 接口包以及读取 .env 文件所需的依赖。

## 运行效果

程序启动后，可以在控制台中连续输入问题，AI 会进行流式输出，并在输入 `exit`、`quit` 或 `q` 后退出。

```text
连续对话已启动，输入 exit 退出。

你：介绍一下你自己

AI 正在思考中...

你好！很高兴能和你交流。

我是一个大型语言模型，由 Google 训练。我的主要目标是协助用户完成各种任务，提供信息，并进行有意义的交流。

Token 统计：
输入 tokens: 0
输出 tokens: 5
总 tokens: 5

你：三句话介绍LangChain

AI 正在思考中...

LangChain 是一个开源框架，旨在简化大型语言模型应用的开发流程。
它可以帮助开发者把大语言模型与外部数据源、工具、提示词模板和记忆模块结合起来。
通过 LangChain，开发者可以更方便地构建聊天机器人、文档问答和智能 Agent 等应用。

Token 统计：
输入 tokens: 0
输出 tokens: 0
总 tokens: 0

你：q
对话结束。

进程已结束，退出代码为 0
```
