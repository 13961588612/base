# 跨领域刻意学习仓库

按领域分文件夹，每个领域一份独立学习计划。方法论底层：《刻意学习》+ 《如何高效学习》。

## 工具约定

| 领域类型 | 包管理 / 运行时 | 锁文件 | 说明 |
|----------|-----------------|--------|------|
| **JavaScript / TypeScript**（React、Next.js 等） | **pnpm** | `pnpm-lock.yaml` | 不用 npm / yarn；项目内统一 `pnpm install` |
| **Python**（AI Agent 等） | **uv** | `uv.lock` | 不用 pip / poetry；`uv sync` |
| **数据库（本地）** | Docker Compose | — | PostgreSQL，见 `reactjs/docker-compose.yml` |

### 前置安装（一次性）

```bash
# Node 包管理 — 推荐通过 corepack 启用 pnpm
corepack enable
corepack prepare pnpm@latest --activate

# Python 包管理（python-ai 领域）
pip install uv
```

### 常用命令对照

| 操作 | JS/TS 项目 | Python 项目 |
|------|------------|---------------|
| 安装依赖 | `pnpm install` | `uv sync` |
| 开发服务器 | `pnpm dev` | `uv run ...` |
| 加依赖 | `pnpm add <pkg>` | `uv add <pkg>` |
| 构建 | `pnpm build` | — |
| 本地数据库 | `docker compose up -d`（reactjs/） | `docker compose up -d`（python-ai/） |

### Monorepo

根目录 `pnpm-workspace.yaml` 管理所有 JS/TS 子项目（如 `reactjs/*`）。在子项目目录内执行 pnpm 命令即可。

---

## 领域索引

| 文件夹 | 领域 | 状态 |
|--------|------|------|
| [reactjs](./reactjs/LEARNING_PLAN.md) | React 18/19 + Next.js 全栈 | **v1.1 可执行** |
| [python-ai](./python-ai/LEARNING_PLAN.md) | Python AI Agent（LangChain / LangGraph / DeepAgents） | **v1.1 可执行** |

## 使用方式

1. 打开对应领域的 `LEARNING_PLAN.md`
2. 按 `CHECKLIST.md` 与 `WEEKLY_SCHEDULE.md` 推进
3. 每周执行反馈调整机制
