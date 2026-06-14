# p0-cli-chat · 多轮 CLI 对话

P0 阶段产物：LLM 流式对话 CLI，为后续 Agent 开发打基础。

> **前置**：完成 W1 `p0-python-drills`（Python 1/5 禁止跳过）。

## 初始化（W2 周一）✅

```bash
# 已执行（PyPI 慢时可设镜像）
# $env:UV_INDEX_URL = "https://pypi.tuna.tsinghua.edu.cn/simple"
uv init --python 3.12 .
uv add langchain langchain-openai langchain-anthropic python-dotenv rich typer
```

## pyproject.toml 速读（W2 周一）

| 字段 | 含义 |
|------|------|
| `[project]` | 包元数据：名称、版本、Python 版本要求 |
| `dependencies` | 运行时依赖（`uv add` 会写入这里） |
| `requires-python` | 最低 Python 版本 |
| `uv.lock` | 锁定全部传递依赖版本，保证 `uv sync` 可复现 |
| `.venv/` | 项目虚拟环境（勿提交 Git） |

常用命令：`uv sync` · `uv add <pkg>` · `uv run python -m src.main`

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
