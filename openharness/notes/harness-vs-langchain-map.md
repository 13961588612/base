# OpenHarness ↔ LangChain 生态对照

> 学完 `python-ai` P1 + openharness P1 后，用**自己的话**补充「公司项目」列。

## 定位对比

| | LangChain / LangGraph / DeepAgents | OpenHarness |
|--|-----------------------------------|-------------|
| 层级 | **应用框架** — 你写业务 Agent | **Harness 运行时** — 模型+Tool+治理 |
| 入口 | Python 代码 `create_agent()` | CLI `oh` / Gateway / stream-json |
| 扩展点 | `@tool`、Middleware、StateGraph | Tool、Skill、Plugin、Hook、MCP |
| 知识加载 | Prompt、DeepAgents `skills/` | `SKILL.md`、CLAUDE.md |
| 子代理 | DeepAgents `subagents` / LangGraph 子图 | coordinator / Agent Tool |
| 持久化 | LangGraph checkpoint | MEMORY.md、session resume |
| 观测 | LangSmith 原生 | token 计数 + **需自研 audit/OTel** |

## 概念映射表

| LangChain 生态 | OpenHarness | 关键差异（你的理解） |
|----------------|-------------|----------------------|
| `@tool` | 内置 Tool / 自定义 Tool / MCP Tool | Harness Tool 走 permission+hook；MCP 适合跨语言 |
| `create_agent` ReAct | engine Agent Loop | 逻辑相似；Harness 内置 43 Tool |
| Prompt Template | prompts/ + CLAUDE.md | Harness 自动发现项目 CLAUDE.md |
| Middleware | hooks Pre/PostToolUse | Hook 更贴近 Tool 生命周期 |
| DeepAgents `skills/` | `.openharness/skills/` | 格式同为 Markdown 目录 |
| LangGraph `interrupt` | permissions + AskUser Tool | 审批 UX 在 TUI/Gateway 层 |
| LangGraph checkpoint | session resume / memory | 图状态 vs 会话级记忆 |
| FastAPI 包装 Agent | stream-json + Gateway | P4 公司后端衔接点 |

## 公司后端推荐分工

```
                    ┌─────────────────────────┐
                    │   OpenHarness Gateway    │  ← 统一入口、鉴权、审计
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │   OpenHarness Runtime    │  ← Tool/Skill/Plugin/MCP
                    └───────────┬─────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
     ┌────────▼────────┐ ┌──────▼──────┐ ┌───────▼────────┐
     │ MCP: 工单/CRM   │ │ MCP: RAG    │ │ LangGraph 子服务│
     │ (只读/读写)     │ │ (python-ai) │ │ (复杂审批流)   │
     └─────────────────┘ └─────────────┘ └────────────────┘
```

**原则**：
- **OpenHarness**：统一对话入口、Tool 治理、Skills 发布、权限基线
- **MCP**：把 `python-ai` 里已有 Agent/RAG **包装成 Tool**，不重复造入口
- **LangGraph**：固定多步审批、强 checkpoint 的子流程，由 MCP 或 HTTP 暴露

## 升级路径

```
python-ai create_agent（验证 Tool 设计）
    ↓ 需要公司级入口 + 多通道
OpenHarness + MCP 包装
    ↓ 需要固定流程 / 强审计图
LangGraph 子服务 + MCP 接入 Harness
```

**反模式**：
- 用 OpenHarness 重写已在 LangGraph 里稳定的审批流（应 MCP 暴露）
- 用 LangChain 再造一套 Gateway（应复用 ohmo 模式）

## 自检（选型前）

1. 需求是「统一 IM/API 入口」还是「单业务 Agent 逻辑」？
2. Tool 是否需要跨团队复用与版本 pin？
3. 是否需要飞书/Slack 级 Gateway？

---

*公司项目记录：*

| 场景 | Harness | LangChain 层 | 原因 |
|------|---------|--------------|------|
| | | | |
