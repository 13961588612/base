# CopilotKit + A2UI · Agent 客户端学习计划

> **你的画像（v1.0 · 待锁定）**
>
> | 项 | 值 |
> |----|-----|
> | React / TS | **≥3/5**（需完成 `reactjs` P0–P1；P3 Next.js 与本轨 **并行或先行**） |
> | Agent 后端 | 0–2/5（`python-ai` P1+ 或 `openharness` Gateway；本轨侧重 **客户端**） |
> | 每周投入 | 25h |
> | 目标 | 用 CopilotKit + A2UI 构建 **生产级 Agent 客户端**（Generative UI） |
> | 周期 | **12 周** |
> | 包管理 | **pnpm**（见仓库根 `README.md`） |
> | 框架 | **Next.js App Router** + CopilotKit **v2**（AG-UI / SSE） |
> | 样式 | Tailwind + 公司组件库映射为 **A2UI Catalog** |
>
> **终极目标**：交付 **公司统一 Agent 客户端 MVP**——CopilotChat 嵌入业务页、A2UI 声明式界面、自定义 Catalog、对接 LangGraph / 公司 Agent 后端、鉴权与可访问性基线。

---

## 〇、协议栈：AG-UI · A2UI · CopilotKit

Agent 客户端不是「聊天框 + fetch」，而是 **Agent ↔ 应用** 的双向运行时。CopilotKit 在浏览器侧实现 **AG-UI** 传输；**A2UI** 是 Google 主导的 **Generative UI 声明式规范**（JSON 消息 → 原生 React 组件）。

```
┌─────────────────────────────────────────────────────────────┐
│  业务应用（Next.js）— 你的页面、路由、设计系统               │
├─────────────────────────────────────────────────────────────┤
│  CopilotKit 客户端：CopilotKitProvider · CopilotChat        │
│  · useAgentContext · useFrontendTool · useRenderToolCall      │
│  · A2UI Renderer + 自定义 Catalog                            │
├─────────────────────────────────────────────────────────────┤
│  AG-UI 传输层（SSE）— Copilot Runtime `/api/copilotkit`      │
├─────────────────────────────────────────────────────────────┤
│  Agent 后端：BuiltInAgent / LangGraph / python-ai 服务       │
│  · 可 emit A2UI 消息（createSurface / updateComponents…）   │
├─────────────────────────────────────────────────────────────┤
│  公司模型网关 / openharness Gateway（可选）                  │
└─────────────────────────────────────────────────────────────┘
```

| 名称 | 层级 | 一句话 |
|------|------|--------|
| **AG-UI** | 传输 / 交互协议 | Agent 与 App 双向事件流（CopilotKit v2 默认） |
| **A2UI** | UI 声明规范 | Agent 发 JSON，客户端用 Catalog 渲染 Widget |
| **A2A** | Agent 间协议 | 远程 Agent 通信（可选；公司后端远期） |
| **CopilotKit** | 前端栈 + Runtime | Provider、Chat、Runtime Handler、A2UI 中间件 |

详见 `notes/ag-ui-a2ui-stack-map.md`。

---

## 一、Generative UI 三种模式（CopilotKit）

| 模式 | 机制 | 适用场景 | 本轨阶段 |
|------|------|----------|----------|
| **Frontend Tool** | `useFrontendTool` / `useRenderToolCall` | Agent 调前端能力、局部 React 渲染 | P1 |
| **Declarative A2UI** | `createSurface` + Catalog | 卡片、表单、仪表盘片段；**跨端可移植** | P2–P3 |
| **Headless** | 自绘 UI + `useAgent` | 完全定制布局 | P1 选修 |

**公司客户端主线**：Chat 壳 + **A2UI Catalog（设计系统）** + LangGraph 后端。

---

## 二、入口门槛

| 条件 | 说明 |
|------|------|
| **reactjs P0–P1** | 函数组件、Hooks、TS Props、Tailwind |
| **Next.js App Router 基础** | 可与 reactjs P3 **并行**；本轨 W1 含 Next 脚手架 |
| **python-ai P1+**（W9 前） | 对接 LangGraph Agent；无后端则 W9 暂用 BuiltInAgent |
| **未完成 React 基础** | 禁止跳过；先 `reactjs/w1-react-basics` |

---

## 三、学习内容总览（6 阶段 · 12 周）

| 阶段 | 主题 | 核心产出 | 周期 |
|------|------|----------|------|
| P0 | CopilotKit v2 + Next Runtime | `p0-copilotkit-starter` | 2 周 |
| P1 | AG-UI 客户端原语 | Chat、Context、Frontend Tool、Interrupt | 2 周 |
| P2 | A2UI 协议 + 内置 Catalog | Surface 消息流、Fixed Schema 入门 | 2 周 |
| **P3** | **自定义 Catalog + 主题** | 公司组件映射、Dynamic Schema | **2 周** |
| **P4** | **LangGraph / 公司 Agent 对接** | 鉴权、HITL、流式 A2UI | **2 周** |
| P5 | 公司 Agent 客户端 MVP | 嵌入业务页 + 部署 + a11y | 2 周 |

### 实践项目路线图

| 周次 | 项目 | 技术点 |
|------|------|--------|
| W1–W2 | `p0-copilotkit-starter` | create、Runtime、CopilotChat |
| W3–W4 | `p1-ag-ui-app` | useAgentContext、Frontend Tool、Interrupt |
| W5–W6 | `p2-a2ui-surfaces` | A2UI 消息、内置 Catalog、Fixed Schema |
| W7–W8 | `p3-a2ui-catalog` | 自定义 Catalog、主题、Dynamic Schema |
| W9–W10 | `p4-langgraph-client` | LangGraphAgent、onRequest 鉴权 |
| W11–W12 | `p5-company-agent-ui` | 业务嵌入、错误态、部署、作品集 |

---

## 四、分阶段详细内容

### P0 · CopilotKit v2 + Next Runtime（W1–W2）

**学习目标**：跑通 Next.js + `CopilotKitProvider` + `createCopilotRuntimeHandler`；理解 AG-UI 替代 GraphQL v1。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 0.0 | `npx copilotkit@latest create` 或手动 Next + pnpm add | 馈 | 2h |
| 0.1 | 读 CopilotKit 文档：Chat / Headless / Generative UI 三分法 | 心 | 3h |
| 0.2 | `app/api/copilotkit/route.ts` + `BuiltInAgent` | 馈 | 4h |
| 0.3 | `CopilotKitProvider runtimeUrl="/api/copilotkit"` 同源部署 | 心 | 3h |
| 0.4 | CopilotChat / CopilotSidebar 嵌入布局 | 边 | 4h |
| 0.5 | 对比 v1 GraphQL vs v2 AG-UI（`notes/ag-ui-a2ui-stack-map.md`） | 联 | 2h |
| 0.6 | 环境变量、`.env.example`；密钥只在服务端 | 馈 | 2h |
| 0.7 | 费曼：Runtime 与 Agent 的分工 | 费 | 2h |

**P0 验收**：
- [ ] 本地多轮对话 + 流式输出
- [ ] 能指出 `route.ts` 与 `layout.tsx` 各负责什么
- [ ] 未把 API Key 暴露到客户端 bundle

---

### P1 · AG-UI 客户端原语（W3–W4）

**学习目标**：Agent 与前端 **共享状态**、**前端 Tool**、**Interrupt/HITL**。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 1.1 | `useAgent` / `useAgentContext`：把页面状态交给 Agent | 心 | 5h |
| 1.2 | `useFrontendTool`：Agent 触发前端动作（导航、表单填充） | 边 | 6h |
| 1.3 | `useRenderToolCall`：Tool 结果自定义 React 渲染 | 馈 | 5h |
| 1.4 | `useInterrupt`：人工确认再继续 | 边 | 4h |
| 1.5 | **项目 `p1-ag-ui-app`**：带 Sidebar 的「业务助手」壳 | 边 | 8h |
| 1.6 | 对比 CopilotKit Frontend Tool vs A2UI（何时升级） | 联 | 2h |
| 1.7 | 费曼：Generative UI 三种模式选型 | 费 | 2h |

**P1 验收**：
- [ ] Agent 能读当前页 context 并完成 1 次前端 Tool
- [ ] 至少 1 个 Interrupt 流程可演示
- [ ] 见 `notes/generative-ui-patterns.md` 填完选型表

---

### P2 · A2UI 协议 + 内置 Catalog（W5–W6）

**学习目标**：读懂 A2UI v0.9 消息；Runtime 开启 `a2ui`；Fixed Schema 流式渲染。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 2.1 | 读 [A2UI Message Reference](https://a2ui.org/reference/messages/) | 心 | 4h |
| 2.2 | 消息流：`createSurface` → `updateComponents` → `updateDataModel` | 心 | 4h |
| 2.3 | Runtime：`a2ui: true` 或 `injectA2UITool: true` | 馈 | 4h |
| 2.4 | Provider：`a2ui={{ catalog }}` + 内置 Text/Card/… | 边 | 5h |
| 2.5 | **Fixed Schema**：预写 JSON 树，Agent 只填 dataModel | 边 | 6h |
| 2.6 | **项目 `p2-a2ui-surfaces`**：订单卡片 / 状态面板 demo | 边 | 10h |
| 2.7 | 安全：Catalog 白名单、无任意代码执行 | 心 | 2h |

**P2 验收**：
- [ ] 能手绘一条 Surface 的消息顺序
- [ ] Fixed Schema demo 流式渲染成功
- [ ] 理解「声明式数据 ≠ 执行代码」

---

### P3 · 自定义 Catalog + Dynamic Schema（W7–W8）⭐

**学习目标**：把 **公司设计系统** 映射为 A2UI Catalog；可选 Dynamic Schema。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 3.1 | Catalog 三要素：`catalogId`、组件 schema、React 映射 | 心 | 4h |
| 3.2 | `includeBasicCatalog: true` vs 仅公司组件 | 边 | 3h |
| 3.3 | **项目 `p3-a2ui-catalog`**：StatusBadge、UserCard、DataTable 入 Catalog | 边 | 12h |
| 3.4 | A2UI theme / `createA2UIMessageRenderer` | 馈 | 4h |
| 3.5 | Dynamic Schema：`injectA2UITool` + 二级 LLM 生成 schema（可选） | 边 | 6h |
| 3.6 | A2UI Composer 生成模板 → 写入 Agent prompt | 联 | 3h |
| 3.7 | 费曼：Fixed vs Dynamic  latency / 可控性 tradeoff | 费 | 2h |

**Catalog 规范**见 `notes/company-catalog-blueprint.md`。

**P3 验收**：
- [ ] ≥3 个公司组件在 Catalog 中可被 Agent 组合
- [ ] 文档说明每个组件的 agent-facing description
- [ ] Fixed Schema 生产路径优先于 Dynamic

---

### P4 · LangGraph / 公司 Agent 对接（W9–W10）⭐

**学习目标**：Runtime 接 **python-ai LangGraph** 或公司 HTTP Agent；生产鉴权。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 4.1 | `LangGraphAgent` + `deploymentUrl` / 自托管 | 心 | 5h |
| 4.2 | Agent 侧 emit A2UI（tool result / middleware） | 边 | 6h |
| 4.3 | `createCopilotRuntimeHandler` + `onRequest` JWT 校验 | 馈 | 5h |
| 4.4 | Token 转发 → LangGraph `configurable` | 联 | 4h |
| 4.5 | **项目 `p4-langgraph-client`**：对接 `python-ai/p3-research-graph` 或 mock | 边 | 12h |
| 4.6 | 错误态：Agent 离线、A2UI 解析失败 fallback | 馈 | 4h |
| 4.7 | 与 openharness Gateway 分工（HTTP vs AG-UI） | 联 | 2h |

**P4 验收**：
- [ ] 前端经鉴权访问 LangGraph Agent
- [ ] 至少 1 个 A2UI Surface 由后端 Agent 驱动
- [ ] 401 / 500 有用户可见降级

---

### P5 · 公司 Agent 客户端 MVP（W11–W12）

**学习目标**：嵌入真实业务布局；a11y、性能、部署。

| 序号 | 学习动作 | 理论 | 时长 |
|------|----------|------|------|
| 5.1 | **项目 `p5-company-agent-ui`**：Dashboard + CopilotSidebar | 整 | 14h |
| 5.2 | 路由级 Provider；多 Agent `agents: { support, ops }` | 边 | 5h |
| 5.3 | 流式 A2UI 性能：大 Surface 分片、骨架屏 | 馈 | 4h |
| 5.4 | a11y：键盘、aria、对比度（Catalog 组件责任） | 联 | 4h |
| 5.5 | E2E 冒烟：Playwright 发消息 + 断言 Surface | 馈 | 5h |
| 5.6 | Vercel / Docker 部署；Runtime 环境变量 | 馈 | 4h |
| 5.7 | ADR：为何 CopilotKit+A2UI vs 纯自定义 SSE | 费 | 3h |
| 5.8 | 作品集 README + 录屏脚本 | 费 | 2h |

**作品集最低要求**：
- Next.js + CopilotKit v2 Runtime
- 自定义 A2UI Catalog ≥3 组件
- LangGraph（或 BuiltInAgent + Fixed A2UI）端到端
- 鉴权 onRequest + `.env.example`
- 部署 URL 或 compose 说明

---

## 五、12 周时间轴

```
周      阶段    主题                              25h
──────────────────────────────────────────────────────────
W1–W2   P0      CopilotKit v2 + Next Runtime      50h
W3–W4   P1      AG-UI 客户端原语                  50h
W5–W6   P2      A2UI + 内置 Catalog               50h
W7–W8   P3      自定义 Catalog ⭐                 50h
W9–W10  P4      LangGraph 对接 ⭐                 50h
W11–W12 P5      公司 Agent 客户端 MVP             50h
```

### 与其他轨道并行建议

| 本轨周 | 建议并行 |
|--------|----------|
| W1–W2 | reactjs P3（Next.js） |
| W3–W6 | reactjs P2–P3；python-ai P1 |
| W7–W8 | python-ai P2–P3 |
| W9–W12 | python-ai P3 LangGraph；openharness P4 Gateway（API 对照） |

---

## 六、反馈与调整机制

| 场景 | 调整 |
|------|------|
| Runtime 404 / CORS | 同源 `runtimeUrl`；检查 `basePath` 与 route 一致 |
| A2UI 不渲染 | 确认 Runtime `a2ui: true`；查消息顺序与 catalogId |
| Catalog 组件不出现 | 检查 agent description 与 schema 是否匹配 |
| Dynamic Schema 慢 | 回退 Fixed Schema + 预定义模板 |
| LangGraph 连不上 | 先 BuiltInAgent + Fixed A2UI 保进度 |
|  bundle 过大 | 动态 import Chat；Catalog 按需注册 |

**每周五晚 Weekly Review（1.5h）**：
1. CHECKLIST 完成率
2. 录屏 1 次失败 UI 渲染，查 Network SSE 事件
3. 下周唯一重点

---

## 七、跨知识整合

| 整合 | 做法 |
|------|------|
| reactjs | Catalog 复用 `w1-react-basics` 组件；Next 布局同 P3 |
| python-ai | LangGraph Agent emit A2UI；Tool 设计互证 |
| openharness | IM Gateway vs CopilotKit Web 客户端；统一后端 ADR |
| 公司设计系统 | Tailwind token → A2UI theme |

---

## 八、推荐资源

| 类型 | 资源 |
|------|------|
| CopilotKit | [docs.copilotkit.ai](https://docs.copilotkit.ai/) |
| A2UI 规范 | [a2ui.org](https://a2ui.org/) |
| A2UI + AG-UI 集成 | [a2ui-with-any-agent-framework](https://a2ui.org/guides/a2ui-with-any-agent-framework/) |
| Generative UI 指南 | [CopilotKit 2026 Guide](https://www.copilotkit.ai/blog/the-developer-s-guide-to-generative-ui-in-2026) |
| 脚手架 | `npx copilotkit@latest create my-app --framework a2ui` |
| LangGraph | [CopilotKit LangGraph Python](https://docs.copilotkit.ai/langgraph-python/) |

---

## 九、文件索引

```
copilotkit-a2ui/
├── LEARNING_PLAN.md              ← 本文件 v1.0
├── CHECKLIST.md
├── WEEKLY_SCHEDULE.md
├── .env.example
├── notes/
│   ├── ag-ui-a2ui-stack-map.md
│   ├── generative-ui-patterns.md
│   ├── a2ui-message-reference.md
│   ├── company-catalog-blueprint.md
│   └── copilotkit-best-practices.md
├── p0-copilotkit-starter/        ← W1–W2
├── p1-ag-ui-app/                 ← W3–W4
├── p2-a2ui-surfaces/             ← W5–W6
├── p3-a2ui-catalog/              ← W7–W8
├── p4-langgraph-client/          ← W9–W10
└── p5-company-agent-ui/          ← W11–W12
```

---

*v1.0 · 入口=reactjs P0–P1 · 25h/周 · CopilotKit v2 + A2UI · 12周*
