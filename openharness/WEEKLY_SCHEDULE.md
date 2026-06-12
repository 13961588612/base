# 14 周逐周执行表（25h/周）

> **入口**：完成 `python-ai` P0 后再写 Plugin/Gateway；W1 可同时预习架构。  
> **每日默认节奏**：晨间 2h 理论+笔记 · 午后 3h 编码 · 晚间 2h 项目/缓冲（可调）  
> **周五晚**：Weekly Review 1.5h（见 LEARNING_PLAN 反馈机制）  
> 理论标注：心=心理表征 · 费=费曼 · 边=舒适区边缘 · 馈=专注反馈 · 整=整体性 · 联=知识关联

---

## W1 · P0  安装与架构

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 安装 openharness-ai；`oh setup`；读 Quick Start | 5 | 馈 |
| 二 | 画十子系统图；对照 `notes/harness-architecture-map.md` | 5 | 心 |
| 三 | `oh --dry-run` 实验；解读 blocked/next actions | 5 | 心 |
| 四 | 配置 2 个 provider profile 并切换 | 4 | 联 |
| 五 | `-p` + `--output-format json/stream-json` | 4 | 馈 |
| 六 | 精读 `engine/` Agent Loop 源码 | 4 | 心 |
| 日 | 费曼笔记 + Weekly Review | 1.5 | 费 |

---

## W2 · P0  TUI 与 lab 验收

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | TUI：权限、/plan、/resume | 5 | 边 |
| 二 | `/skills` 与 CLAUDE.md 发现机制 | 5 | 心 |
| 三 | `p0-harness-lab`：实验记录模板 | 5 | 馈 |
| 四 | token 计数与 cost 跟踪观察 | 4 | 馈 |
| 五 | 对比 Claude Code / Cursor Harness 差异笔记 | 4 | 联 |
| 六 | P0 验收：白板 Agent Loop | 3 | 费 |
| 日 | Weekly Review | 1.5 | 馈 |

---

## W3 · P1  内置 Tool 与自定义 Tool

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 43 Tool 分类表 + 公司禁用清单 | 5 | 心 |
| 二 | `p1-custom-tool` 设计：只读域 Tool | 5 | 边 |
| 三 | 实现 Tool + Pydantic 校验 | 5 | 馈 |
| 四 | Tool docstring 路由实验 | 4 | 馈 |
| 五 | PreToolUse Hook 审计原型 | 4 | 馈 |
| 六 | 与 python-ai `@tool` 设计对照 | 3 | 联 |
| 日 | Review | 1.5 | 馈 |

---

## W4 · P1  Skills 与 Permissions

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | Skills 目录规范；读 anthropics/skills 示例 | 5 | 心 |
| 二 | `p2-company-skills`：Skill 1–2 | 5 | 整 |
| 三 | Skill 3 + 用户可调用 slash 命令 | 5 | 边 |
| 四 | `settings.json` permission 基线 | 4 | 馈 |
| 五 | Plan Mode 大任务实验 | 4 | 边 |
| 六 | 费曼：Skill vs Plugin | 3 | 费 |
| 日 | P1 验收 + Review | 1.5 | 馈 |

---

## W5 · P2  MCP 基础

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | MCP 协议复习；`oh mcp` 配置 | 5 | 心 |
| 二 | 写最小 MCP Server（stdio） | 5 | 边 |
| 三 | Harness 侧注册与调用 | 5 | 馈 |
| 四 | dry-run 检查 MCP；断线行为 | 4 | 馈 |
| 五 | MCP HTTP transport（若需） | 4 | 边 |
| 六 | 只读权限与参数校验 | 3 | 边 |
| 日 | Review | 1.5 | 馈 |

---

## W6 · P2  Plugins

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 安装 security-guidance plugin | 5 | 心 |
| 二 | 读 plugin Hook 源码 | 5 | 心 |
| 三 | `p3-mcp-integration` 联调内部只读 API | 5 | 边 |
| 四 | 自研 Plugin 脚手架 | 4 | 边 |
| 五 | Plugin enable/disable 与版本 pin | 4 | 馈 |
| 六 | P2 验收文档 | 3 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W7 · P3  Multi-Agent 基础

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | coordinator 文档 + 示例子 Agent | 5 | 心 |
| 二 | TeamCreate / SendMessage 实验 | 5 | 边 |
| 三 | Task 后台任务创建与 Output | 5 | 馈 |
| 四 | `--max-turns` 熔断配置 | 4 | 馈 |
| 五 | 子 Agent 上下文隔离验证 | 4 | 边 |
| 六 | 对比 LangGraph 子图 | 3 | 联 |
| 日 | Review | 1.5 | 馈 |

---

## W8 · P3  Memory 与 lab

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | MEMORY.md 策略设计 | 5 | 心 |
| 二 | Auto-Compaction 长会话实验 | 5 | 馈 |
| 三 | `p3-multi-agent-lab`：调研+汇总 | 5 | 边 |
| 四 | 完善 lab README 与演示脚本 | 4 | 馈 |
| 五 | 费曼：coordinator vs DeepAgents | 3 | 费 |
| 六 | P3 验收 | 4 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W9 · P4  ohmo Gateway

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | ohmo init / config 流程 | 5 | 心 |
| 二 | gateway start；通道消息流阅读 | 5 | 心 |
| 三 | 飞书/Slack 配置文档研读（选 1） | 5 | 边 |
| 四 | `p4-gateway-backend` 需求与 API 契约 | 4 | 整 |
| 五 | Webhook 通道原型 | 4 | 边 |
| 六 | 会话 resume 实验 | 3 | 馈 |
| 日 | Review | 1.5 | 馈 |

---

## W10 · P4  stream-json API

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | stream-json 事件解析器 | 5 | 馈 |
| 二 | REST/SSE 封装层 | 5 | 边 |
| 三 | 用户 ID → profile 路由 | 5 | 边 |
| 四 | 附件/多模态限制策略 | 4 | 边 |
| 五 | Gateway 集成测试 | 4 | 馈 |
| 六 | P4 验收 | 3 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W11 · P5  平台骨架

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 写 ADR：Harness 层选型 | 5 | 费 |
| 二 | `p5-company-agent-platform` 目录脚手架 | 5 | 整 |
| 三 | 统一 config/profiles/skills 布局 | 5 | 整 |
| 四 | 鉴权中间件原型 | 4 | 边 |
| 五 | MCP 白名单配置 | 4 | 馈 |
| 六 | 内部 README  onboarding | 3 | 馈 |
| 日 | Review | 1.5 | 馈 |

---

## W12 · P5  审计与观测

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | PostToolUse 审计 log schema | 5 | 馈 |
| 二 | LangSmith 或 OTel 接入 | 5 | 馈 |
| 三 | 敏感 Tool 默认 deny 清单 | 5 | 边 |
| 四 | 端到端演示：IM → Gateway → MCP | 4 | 边 |
| 五 | 30 分钟 onboarding 演练 | 4 | 馈 |
| 六 | P5 验收 | 3 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W13 · P6  容器化

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | Dockerfile（gateway + harness） | 5 | 馈 |
| 二 | docker-compose 联调 | 5 | 馈 |
| 三 | 健康检查 /health | 5 | 馈 |
| 四 | Secret 与环境分离 | 4 | 馈 |
| 五 | 限流与超时配置 | 4 | 边 |
| 六 | staging 环境 dry-run 发布 | 3 | 整 |
| 日 | Review | 1.5 | 馈 |

---

## W14 · P6  运维与作品集

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 运行手册 / 故障树 | 5 | 费 |
| 二 | 回滚流程与 checklist | 5 | 整 |
| 三 | 作品集 README + 架构图 | 5 | 费 |
| 四 | 演示录像脚本 | 4 | 馈 |
| 五 | 模拟 Security 评审 | 4 | 费 |
| 六 | 模拟 SRE 评审 + 总验收 | 3 | 费 |
| 日 | 结业 Review | 1.5 | 馈 |

---

## 并行 python-ai 时的周对照

| openharness 周 | 建议 python-ai 进度 |
|----------------|---------------------|
| W1–W2 | python-ai W2–W3（LLM CLI） |
| W3–W6 | python-ai W4–W6（LangChain Agent） |
| W7–W8 | python-ai W7–W9 或 W10（RAG / LangGraph 预习） |
| W9–W14 | 与 python-ai P3+ 深度互补 |
