# OpenHarness · 公司统一 AI Agent 后端学习计划

> **你的画像（v1.0 · 待锁定）**
>
> | 项 | 值 |
> |----|-----|
> | Python | **≥3/5**（需先完成 `python-ai` P0，或同等能力） |
> | Agent 框架经验 | 0–2/5（LangChain / LangGraph 初学即可；本轨侧重 **Harness 平台层**） |
> | 每周投入 | 25h |
> | 目标 | 基于 OpenHarness **设计、扩展、部署** 公司统一 Agent 后端 |
> | 周期 | **14 周**（Harness 专精；与 `python-ai` 可并行，见「入口门槛」） |
> | 包管理 | **uv**（子项目）+ `pip install openharness-ai`（CLI 全局/venv） |
> | 模型 | 公司统一网关：Anthropic-Compatible / OpenAI-Compatible profile |
> | 观测 | OpenHarness 内置 token 计数 + **自研补齐**（LangSmith / OTel，P5 起） |
>
> **终极目标**：交付 **公司级 Agent 后端 MVP**——统一 Provider 路由、Skills/Plugins 治理、MCP 接入内部系统、Gateway 多通道、权限与审计、容器化部署与运维手册。

---

## 〇、OpenHarness 是什么？与 python-ai 的关系

OpenHarness（`oh`）是 HKUDS 开源的 **Agent Harness** 实现：约 1.1 万行 Python，复刻 Claude Code 类产品的核心骨架。

> **The model is the agent. The code is the harness.**  
> 模型负责「想」；Harness 负责「手、眼、记忆、安全边界」。

```
┌─────────────────────────────────────────────────────────────┐
│  公司应用层：飞书 / Slack / 内部 Web / 业务系统 Webhook      │
├─────────────────────────────────────────────────────────────┤
│  Gateway 层：ohmo 模式扩展 — 会话路由、多租户、鉴权（自研）   │
├─────────────────────────────────────────────────────────────┤
│  OpenHarness：engine · tools · skills · plugins · hooks     │
│                permissions · memory · coordinator · MCP      │
├─────────────────────────────────────────────────────────────┤
│  内部能力：MCP Server（CRM/DB/工单）· 公司 Skills 库         │
├─────────────────────────────────────────────────────────────┤
│  LLM：公司统一 Profile（OpenAI / Anthropic Compatible）     │
└─────────────────────────────────────────────────────────────┘
```

| 维度 | `python-ai`（LangChain 生态） | `openharness`（本轨） |
|------|------------------------------|------------------------|
| 核心问题 | **如何编排 Agent 业务逻辑** | **如何运行、扩展、治理 Agent 运行时** |
| 典型产出 | RAG、LangGraph 工作流、DeepAgents | 统一后端、Skills 包、MCP 集成、Gateway |
| 代码位置 | 你的 `create_agent` / `StateGraph` | `openharness/` 源码 + 公司 `plugins/` |
| 互补方式 | LangChain Tool → **包装为 MCP** → OpenHarness 调用 | Harness 做入口与治理，LangGraph 做复杂子流程 |

详见 `notes/harness-vs-langchain-map.md`、`notes/company-backend-blueprint.md`。

---

## 一、入口门槛（禁止跳过）

| 条件 | 说明 |
|------|------|
| **python-ai P0 完成** | W1–W3：`p0-python-drills` + `p0-cli-chat`；能读 `@tool`、async、流式 |
| **或** 自评 Python ≥3/5 + 跑通过一次 LLM API | 需在 `notes/entry-self-check.md` 记录证据 |
| **未完成 P0 时** | 只可做 P0-H 预习（读架构图、`oh --dry-run`），**禁止**写公司 Plugin / Gateway |

---

## 二、Harness 十子系统（必读）

OpenHarness 将 Agent 能力拆为四层，详见 `notes/harness-architecture-map.md`：

```
openharness/
  engine/        # Agent Loop：stream → tool_use → execute → loop
  tools/         # 43+ 内置 Tool（File/Shell/Web/MCP/Agent/Task…）
  skills/        # 按需加载 .md 领域知识（兼容 anthropics/skills）
  plugins/       # 命令、Hooks、子 Agent、MCP（兼容 claude-code plugins）
  permissions/   # default / auto / plan；路径规则、命令 deny
  hooks/         # PreToolUse / PostToolUse 生命周期
  commands/      # 54 个斜杠命令（/plan、/commit、/resume…）
  mcp/           # MCP 客户端（stdio / HTTP）
  memory/        # MEMORY.md 跨会话持久化
  coordinator/   # 子 Agent、Team、后台 Task
  prompts/       # CLAUDE.md、system prompt 组装
  config/        # 多层 settings、profile、迁移
  ui/            # React TUI（Ink）
```

**公司后端重点子系统**：`engine`、`tools`、`skills`、`plugins`、`permissions`、`hooks`、`mcp`、`coordinator`、`config`。

---

## 三、学习内容总览（6 阶段 · 14 周）

| 阶段 | 主题 | 核心产出 | 周期 |
|------|------|----------|------|
| P0 | Harness 心智模型 + 本地跑通 | `p0-harness-lab` + 架构笔记 | 2 周 |
| P1 | Tools + Skills + Permissions | 自定义 Tool + 公司 Skills 包 | 2 周 |
| P2 | MCP + Plugins 生态 | 内部 MCP 接入 + 1 个 Plugin | 2 周 |
| **P3** | **Multi-Agent + Memory + Tasks** | 子 Agent 协作 + 持久化策略 | **2 周** |
| **P4** | **Gateway + 程序化 API** | ohmo 扩展 + stream-json 集成 | **2 周** |
| **P5** | **公司统一后端 MVP** | 多 Profile、审计、观测补齐 | **2 周** |
| P6 | 生产部署 + 运维 + ADR | Docker/K8s + 运行手册 + 作品集 | 2 周 |

### 实践项目路线图

| 周次 | 项目 | 技术点 |
|------|------|--------|
| W1–W2 | `p0-harness-lab` | 安装、`oh setup`、`--dry-run`、读 engine 源码 |
| W3–W4 | `p1-custom-tool` + `p2-company-skills` | 自定义 Tool、Hooks、Skills 目录规范 |
| W5–W6 | `p3-mcp-integration` | MCP Server、HTTP transport、Tool 权限 |
| W7–W8 | `p3-multi-agent-lab` | coordinator、Task、Memory 策略 |
| W9–W10 | `p4-gateway-backend` | ohmo gateway、stream-json、会话路由 |
| W11–W12 | `p5-company-agent-platform` | 统一入口、租户 Profile、审计日志 |
| W13–W14 | `p6-deploy-ops` | Docker、健康检查、回滚、ADR |

---

## 四、分阶段详细内容

### P0 · Harness 心智模型 + 本地跑通（W1–W2）

**学习目标**：理解 Agent Loop；能在本机安全预览与交互运行；画出十子系统协作图。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 0.0 | 安装 `openharness-ai`；Windows 用 `openh`；跑 `oh setup` | 馈 | 2h |
| 0.1 | 阅读官方 Quick Start + Architecture；对照 `notes/harness-architecture-map.md` 画 Mermaid | 心 | 4h |
| 0.2 | `oh --dry-run` 解读 readiness（ready/warning/blocked） | 心 | 2h |
| 0.3 | 配置 2 个 provider profile（如 OpenAI-Compatible + 公司网关）并 `oh provider use` 切换 | 联 | 3h |
| 0.4 | 非交互模式：`oh -p "..." --output-format json` / `stream-json` | 馈 | 3h |
| 0.5 | **精读** `engine/` Agent Loop 源码（while stream → tool_use → execute） | 心 | 6h |
| 0.6 | TUI 体验：权限对话框、/plan、/resume、/skills | 边 | 3h |
| 0.7 | 费曼：「模型决定 what，Harness 决定 how」各举 2 例 | 费 | 2h |

**P0 验收**：
- [ ] 能白板画出 Query → Engine → Tool → Permission → Hook → Loop
- [ ] `--dry-run` 能解释 blocked 原因与 next actions
- [ ] 切换 profile 不改业务 prompt 即可换模型后端

---

### P1 · Tools + Skills + Permissions（W3–W4）

**学习目标**：扩展公司域 Tool；建立 Skills 仓库规范；掌握权限与 Hooks。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 1.1 | 梳理内置 43 Tool 分类表；标注公司场景禁用项（Bash、WebFetch…） | 心 | 3h |
| 1.2 | **项目 `p1-custom-tool`**：1 个 Pydantic 校验的只读 Tool（如查内部文档索引） | 边 | 8h |
| 1.3 | PreToolUse Hook：敏感路径拦截、操作审计日志 | 馈 | 5h |
| 1.4 | **项目 `p2-company-skills`**：≥3 个 SKILL.md（onboarding、发布流程、故障手册） | 整 | 8h |
| 1.5 | `settings.json`：permission mode、path_rules、denied_commands | 馈 | 4h |
| 1.6 | Plan Mode 大改前先规划；对比 default vs plan 行为 | 边 | 3h |
| 1.7 | 费曼：Skill vs System Prompt vs Plugin 何时用 | 费 | 2h |

**P1 验收**：
- [ ] 自定义 Tool 有 JSON Schema + docstring 路由说明
- [ ] 公司 Skills 可从项目级 `.openharness/skills/` 加载
- [ ] Hook 能在写操作前阻断并记录

---

### P2 · MCP + Plugins（W5–W6）

**学习目标**：内部系统通过 MCP 暴露给 Harness；复用 claude-code 插件生态。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 2.1 | MCP 概念复习；`oh mcp` 配置 stdio / HTTP server | 心 | 4h |
| 2.2 | **项目 `p3-mcp-integration`**：只读 MCP（工单查询 / DB 只读） | 边 | 12h |
| 2.3 | MCP 断线重连、tool-only server；`--dry-run` 检查 MCP 配置 | 馈 | 4h |
| 2.4 | 安装并启用 1 个官方 plugin（如 security-guidance）；读 Hook 源码 | 心 | 4h |
| 2.5 | 自写 Plugin：`commands/` + `hooks/` 最小结构 | 边 | 8h |
| 2.6 | 对比：内置 Tool vs MCP Tool vs LangChain `@tool` 包装路径 | 联 | 3h |

**P2 验收**：
- [ ] MCP Tool 在 Harness 中可调用且受 permission 约束
- [ ] 至少 1 个自研 Plugin 可 `oh plugin enable`
- [ ] 文档记录每个 MCP 的权限级别（只读/读写）

---

### P3 · Multi-Agent + Memory + Tasks（W7–W8）⭐

**学习目标**：长会话、子 Agent 分工、后台任务——公司复杂工单场景基础。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 3.1 | coordinator：子 Agent spawn、TeamCreate、SendMessage | 心 | 5h |
| 3.2 | Task 生命周期：Create → Output → Stop；后台任务观测 | 馈 | 4h |
| 3.3 | MEMORY.md + Auto-Compaction；跨会话知识策略 | 心 | 4h |
| 3.4 | **项目 `p3-multi-agent-lab`**：调研子 Agent + 汇总主 Agent | 边 | 12h |
| 3.5 | `--max-turns`、递归上限；防止 tool 死循环 | 馈 | 3h |
| 3.6 | 与 LangGraph checkpoint 对比：何时子流程下沉 LangGraph | 联 | 4h |
| 3.7 | 费曼：OpenHarness coordinator vs DeepAgents subagents | 费 | 2h |

**P3 验收**：
- [ ] 子 Agent 上下文隔离可演示
- [ ] 长对话 compaction 后任务状态可恢复
- [ ] 有「超过 N 次 tool 调用」的熔断策略

---

### P4 · Gateway + 程序化 API（W9–W10）⭐

**学习目标**：从 CLI/TUI 升级到 **多通道 Gateway**；对接业务系统。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 4.1 | ohmo：`init` → `config` → `gateway start`；飞书/Slack 通道原理 | 心 | 5h |
| 4.2 | 读 ohmo gateway 消息流：channel → harness → stream 回传 | 心 | 6h |
| 4.3 | **项目 `p4-gateway-backend`**：HTTP Webhook 通道（模拟内部 IM） | 边 | 14h |
| 4.4 | `stream-json` 事件解析；封装为内部 REST/SSE 契约 | 馈 | 6h |
| 4.5 | 会话 ID、用户 ID 映射；多租户 profile 路由 | 边 | 5h |
| 4.6 | 附件 / 多模态消息（若版本支持）与大小限制 | 边 | 3h |

**P4 验收**：
- [ ] 非 TUI 客户端可通过 API 发起对话并收流式响应
- [ ] Gateway 进程可独立重启，会话可 resume
- [ ] 有 channel 级配置文档

---

### P5 · 公司统一 Agent 后端 MVP（W11–W12）⭐

**学习目标**：整合 P1–P4 产出为 **单一可部署后端**；补齐 OpenHarness 未内置的企业能力。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 5.1 | 架构 ADR：为何选 OpenHarness 作 Harness 层（对比自研/LangGraph-only） | 费 | 3h |
| 5.2 | **项目 `p5-company-agent-platform`**：统一配置仓库结构 | 整 | 16h |
| 5.3 | 鉴权层（自研）：API Key / JWT → 映射 profile + permission mode | 边 | 8h |
| 5.4 | 审计：Hook 写结构化 audit log（谁、何时、何 Tool、何参数摘要） | 馈 | 6h |
| 5.5 | 观测补齐：LangSmith 或 OpenTelemetry 包装 stream-json | 馈 | 6h |
| 5.6 | 配置治理：Skills/Plugin 版本 pin；`allow_project_skills` 策略 | 馈 | 4h |
| 5.7 | 安全：prompt injection 意识、MCP 白名单、敏感 Tool 默认 deny | 边 | 4h |

**公司后端目录建议**（写入 `p5-company-agent-platform/README.md`）：

```
company-agent-backend/
├── config/
│   ├── profiles/          # 各环境 LLM profile
│   ├── settings.json      # permission 基线
│   └── mcp/               # MCP server 清单
├── skills/                # 公司级 SKILL.md
├── plugins/               # 自研 plugin
├── gateway/               # ohmo 扩展 / FastAPI 适配层
├── audit/                 # 审计日志 schema
└── deploy/                # Docker / compose
```

**P5 验收**：
- [ ] 一条命令启动「Gateway + Harness + MCP」联调环境
- [ ] 新同事按 README 30 分钟内跑通
- [ ] 审计日志可追踪一次完整 tool 调用链

---

### P6 · 生产部署 + 运维 + 作品集（W13–W14）

**学习目标**：容器化、健康检查、发布回滚、运维手册。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 6.1 | **项目 `p6-deploy-ops`**：Dockerfile + compose（gateway + 可选 Postgres） | 馈 | 8h |
| 6.2 | 健康检查：`/health`、MCP 探活、model profile ready | 馈 | 4h |
| 6.3 | 密钥：K8s Secret / Vault；禁止镜像内嵌 Key | 馈 | 4h |
| 6.4 | 限流、超时、并发会话上限 | 边 | 5h |
| 6.5 | 发布 checklist：dry-run → staging → prod | 整 | 4h |
| 6.6 | 运行手册：故障树（MCP 挂、profile 失效、compaction 异常） | 费 | 4h |
| 6.7 | 作品集 README + 架构图 + 演示录像脚本 | 费 | 4h |
| 6.8 | 模拟评审：Security + SRE 双视角问答 | 费 | 2h |

**作品集最低要求**：
- 1 套公司 Skills 库（≥5 个 SKILL.md）
- 1 个 MCP 集成（只读内部数据）
- 1 个 Gateway 可演示（Webhook 或 ohmo 通道）
- 1 份 ADR + 1 份部署运行手册
- 审计日志样例 + 权限配置样例

---

## 五、14 周时间轴

```
周      阶段    主题                              25h
──────────────────────────────────────────────────────────
W1–W2   P0      Harness 心智模型 + 本地跑通        50h
W3–W4   P1      Tools + Skills + Permissions      50h
W5–W6   P2      MCP + Plugins                     50h
W7–W8   P3      Multi-Agent + Memory ⭐            50h
W9–W10  P4      Gateway + 程序化 API ⭐            50h
W11–W12 P5      公司统一后端 MVP ⭐                50h
W13–W14 P6      生产部署 + 运维                   50h
```

**与 python-ai 并行建议**：

| python-ai 进度 | openharness 可并行内容 |
|----------------|------------------------|
| W1（纯 Python） | 仅 P0 阅读架构，不写 Plugin |
| W2–W3（LLM CLI） | 启动 openharness P0 全部 |
| W4–W6（LangChain Agent） | openharness P1–P2；Tool 设计互证 |
| W10+（LangGraph） | openharness P3–P5；复杂子流程下沉 LangGraph |

---

## 六、反馈与调整机制

| 场景 | 调整 |
|------|------|
| 读不懂 engine 源码 | 回退 python-ai P0；先画 Agent Loop 再读代码 |
| `--dry-run` 长期 blocked | 优先修 auth / MCP config，不强行 `--dangerously-skip-permissions` |
| Tool 被模型误用 | 改 docstring + 加 Hook 拒绝 + 缩小 Tool 暴露面 |
| Gateway 内存涨 | 会话 TTL、compaction 策略、限制附件大小 |
| MCP 延迟高 | 只读缓存、异步 Task、非关键查询 offload 子 Agent |
| 公司要求强审计 | P5 提前：所有写 Tool 必须 PostToolUse audit |
| 项目超时 | 先 1 个 MCP + 1 个 Skill + CLI stream-json，再 Gateway |

**每周五晚 Weekly Review（1.5h）**：
1. CHECKLIST 完成率
2. 挑 1 次失败会话（权限拒、Tool 错、MCP 超时）做根因
3. 下周唯一重点（只能有 1 个）

---

## 七、跨知识整合

| 整合 | 做法 | 理论 |
|------|------|------|
| python-ai Tool 设计 | LangChain `@tool` → MCP Server → OpenHarness 调用 | 联 |
| python-ai DeepAgents Skills | 对照 OpenHarness `SKILL.md` 目录规范 | 联 |
| python-ai P6 FastAPI | Gateway 层 REST 契约与 FastAPI 路由对照 | 整 |
| reactjs 全栈 | Next.js 管理台：Skills 发布、审计查询、会话监控 | 联 |
| DevOps | Docker compose 与 python-ai / reactjs 共用 Postgres 经验 | 联 |

---

## 八、OpenHarness 已知边界（公司后端必补）

| 开源版缺失 | 公司后端补齐方式 | 阶段 |
|------------|------------------|------|
| 企业 SSO / OAuth | 网关层 JWT + IdP 集成 | P5 |
| 集中 telemetry | LangSmith / OTel + audit log | P5 |
| 多租户隔离 | profile + 会话 namespace + MCP 权限 | P4–P5 |
| HA / 水平扩展 | Gateway 无状态 + 队列化长 Task | P6 |
| 细粒度 RBAC | Hook + 自研 authz 中间件 | P5 |

详见 `notes/openharness-best-practices.md`。

---

## 九、推荐资源

| 类型 | 资源 |
|------|------|
| 官方仓库 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) |
| 安装 | `pip install openharness-ai` / 官方 install.sh |
| 架构导读 | [OpenHarness Visual Guide](https://ursb.me/en/notes/openharness-visual-guide/) |
| Skills 格式 | [anthropics/skills](https://github.com/anthropics/skills) |
| Plugins 格式 | [claude-code plugins](https://github.com/anthropics/claude-code/tree/main/plugins) |
| MCP | [modelcontextprotocol.io](https://modelcontextprotocol.io/) |
| 本仓库笔记 | `notes/harness-architecture-map.md` 等 |

---

## 十、文件索引

```
openharness/
├── LEARNING_PLAN.md              ← 本文件 v1.0
├── CHECKLIST.md                  ← 知识点勾选
├── WEEKLY_SCHEDULE.md            ← 逐周执行表
├── docker-compose.yml            ← 本地 Gateway + Postgres（审计/会话扩展）
├── .env.example                  ← Provider / MCP / Gateway 模板
├── notes/
│   ├── harness-architecture-map.md
│   ├── harness-vs-langchain-map.md
│   ├── company-backend-blueprint.md
│   ├── company-backend-decision-tree.md
│   └── openharness-best-practices.md
├── p0-harness-lab/               ← W1–W2
├── p1-custom-tool/                 ← W3
├── p2-company-skills/              ← W4
├── p3-mcp-integration/             ← W5–W6
├── p3-multi-agent-lab/             ← W7–W8
├── p4-gateway-backend/             ← W9–W10
├── p5-company-agent-platform/      ← W11–W12
└── p6-deploy-ops/                  ← W13–W14
```

---

*v1.0 · 入口=python-ai P0 · 25h/周 · OpenHarness 公司 Agent 后端 · 14周*
