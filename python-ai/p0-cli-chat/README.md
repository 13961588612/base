# p0-cli-chat · 多轮 CLI 对话

P0 阶段产物：LLM 流式对话 CLI，为后续 Agent 开发打基础。

> **前置**：完成 W1 `p0-python-drills`（Python 1/5 禁止跳过）。

## 初始化（W2 周一）

在 `python-ai/p0-cli-chat` 目录执行：

```bash
uv init --python 3.12 .
uv add langchain langchain-openai langchain-anthropic python-dotenv rich typer
```

## 目标功能

- [ ] 多轮对话历史（内存）
- [ ] 流式输出（Rich live display）
- [ ] `/reset` 清空历史
- [ ] `/model` 切换 provider（环境变量驱动）
- [ ] 异常重试与友好错误提示

## 运行

```bash
# 在 python-ai/ 目录复制环境变量
cp .env.example .env
# 编辑 .env 填入 API Key

cd p0-cli-chat
uv run python -m src.main
```

## 目录建议

```
p0-cli-chat/
├── pyproject.toml
├── uv.lock
├── README.md
└── src/
    ├── main.py          # Typer CLI 入口
    ├── chat.py          # 对话循环
    ├── models.py        # init_chat_model 工厂
    └── config.py        # 环境变量加载
```

## 验收标准

见 `../LEARNING_PLAN.md` P0 验收章节。
