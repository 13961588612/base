# OpenHarness · 知识点 Checklist

> 用法：学完打 `[x]`，阶段末对照验收。理论列：心=心理表征 · 费=费曼 · 边=舒适区边缘 · 馈=专注反馈 · 整=整体性学习 · 联=知识关联

---

## 入口门槛

- [ ] 完成 `python-ai` P0（W1–W3）或等价自评 — 联
- [ ] 能读 OpenHarness Agent Loop 伪代码 — 心

---

## P0 · Harness 心智模型（W1–W2）

- [ ] 安装 `openharness-ai`；Windows 知悉 `openh` 别名 — 馈
- [ ] `oh setup` / `oh provider list` / `oh provider use` — 馈
- [ ] `oh --dry-run` 解读 ready / warning / blocked — 心
- [ ] 非交互：`--output-format json` / `stream-json` — 馈
- [ ] 十子系统名称与职责 — 心
- [ ] Agent Loop：stream → tool_use → permission → hook → execute — 心
- [ ] TUI：权限对话框、/plan、/resume、/skills — 边
- [ ] 费曼：「模型 what / Harness how」 — 费
- [ ] 项目 `p0-harness-lab` 笔记完成 — 边

---

## P1 · Tools + Skills + Permissions（W3–W4）

- [ ] 43 内置 Tool 分类与禁用策略 — 心
- [ ] 自定义 Tool：Pydantic + JSON Schema — 边
- [ ] PreToolUse / PostToolUse Hook — 馈
- [ ] `settings.json`：mode、path_rules、denied_commands — 馈
- [ ] Plan Mode vs Default Mode — 心
- [ ] Skills：`.openharness/skills/<name>/SKILL.md` — 心
- [ ] `allow_project_skills` 不可信仓库策略 — 馈
- [ ] 项目 `p1-custom-tool` — 边
- [ ] 项目 `p2-company-skills` ≥3 个 — 边
- [ ] 费曼：Skill vs Plugin vs System Prompt — 费

---

## P2 · MCP + Plugins（W5–W6）

- [ ] MCP stdio / HTTP 配置 — 心
- [ ] `oh mcp` 管理与 dry-run 检查 — 馈
- [ ] MCP Tool 权限与只读原则 — 边
- [ ] 官方 Plugin 安装启用 — 边
- [ ] 自研 Plugin 结构（commands + hooks） — 边
- [ ] 项目 `p3-mcp-integration` — 边
- [ ] LangChain Tool → MCP 路径理解 — 联

---

## P3 · Multi-Agent + Memory（W7–W8）

- [ ] coordinator：子 Agent、Team、SendMessage — 心
- [ ] Task 后台生命周期 — 心
- [ ] MEMORY.md + Auto-Compaction — 心
- [ ] `--max-turns` / 死循环熔断 — 馈
- [ ] 项目 `p3-multi-agent-lab` — 边
- [ ] 费曼：coordinator vs LangGraph vs DeepAgents — 费

---

## P4 · Gateway + API（W9–W10）

- [ ] ohmo init / config / gateway — 心
- [ ] channel 消息 ↔ Harness 回路 — 心
- [ ] stream-json 事件解析 — 馈
- [ ] 会话 ID / 用户 ID / profile 路由 — 边
- [ ] 项目 `p4-gateway-backend` — 边

---

## P5 · 公司统一后端 MVP（W11–W12）

- [ ] 统一配置仓库结构 — 整
- [ ] 鉴权层（API Key / JWT） — 边
- [ ] 审计 Hook + 结构化日志 — 馈
- [ ] 观测（LangSmith 或 OTel） — 馈
- [ ] Skills/Plugin 版本治理 — 馈
- [ ] MCP 白名单 + 敏感 Tool deny — 边
- [ ] ADR：为何 OpenHarness 作 Harness 层 — 费
- [ ] 项目 `p5-company-agent-platform` — 边

---

## P6 · 生产部署（W13–W14）

- [ ] Docker + compose 一键启动 — 馈
- [ ] 健康检查与探活 — 馈
- [ ] 密钥不入库 / Secret 管理 — 馈
- [ ] 限流、超时、并发上限 — 边
- [ ] 发布 checklist（dry-run → staging → prod） — 整
- [ ] 运行手册 / 故障树 — 费
- [ ] 项目 `p6-deploy-ops` — 边
- [ ] 模拟 Security + SRE 评审 — 费

---

## 跨域整合（全程）

- [ ] `notes/harness-vs-langchain-map.md` 持续更新 — 联
- [ ] `notes/company-backend-blueprint.md` 架构图定稿 — 心
- [ ] 每周 200 字 Harness 实践笔记 ≥14 篇 — 整

---

## 选型速查（阶段末必会）

- [ ] 何时用 OpenHarness 作统一入口 — 费
- [ ] 何时下沉 LangGraph 子流程 — 费
- [ ] 何时 MCP vs 内置 Tool vs 自定义 Tool — 费

---

*配合 LEARNING_PLAN.md v1.0 使用*
