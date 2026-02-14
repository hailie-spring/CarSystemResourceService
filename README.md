# Car System Resource Service

Claude AI 交互式聊天机器人应用

## 功能特性

- 🤖 基于 Claude AI 的对话交互
- 💬 支持多轮对话历史记录
- 🎨 彩色命令行界面输出
- 🔄 实时流式响应展示

## 项目结构

```
CarSystemResourceService/
├── src/
│   └── claudedemo.py      # 主应用程序
├── requirements.txt        # 项目依赖
├── .gitignore             # Git忽略配置
└── README.md              # 项目文档
```

## 前置要求

- Python 3.7+
- Anthropic API key
- 必要的 Python 依赖包

## 安装步骤

1. 克隆项目
```bash
git clone <repository-url>
cd CarSystemResourceService
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
创建 `.env` 文件并添加以下配置：
```
API_KEY=your_anthropic_api_key
BASE_URL=your_api_base_url
MODEL_NAME=your_model_name
```

## 使用方法

运行聊天应用：
```bash
python src/claudedemo.py
```

启动后，可以：
- 输入任何问题或对话内容与 Claude AI 交互
- 输入 `quit` 退出应用程序

## 功能说明

### chat_with_claude()
主聊天函数，支持：
- 持续的多轮对话
- 完整的对话历史记录保留
- 实时流式响应显示
- 彩色化的用户界面

## 环保提示

本项目使用 `.gitignore` 忽略 `.env` 文件，防止敏感信息（如 API keys）被上传到版本控制系统。

## License

MIT
