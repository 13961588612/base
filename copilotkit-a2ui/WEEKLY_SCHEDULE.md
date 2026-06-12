# 12 周逐周执行表（25h/周）

> **入口**：reactjs P0–P1；Next.js 可与 W1 并行。  
> **每日默认节奏**：晨间 2h 理论+笔记 · 午后 3h 编码 · 晚间 2h 项目/缓冲  
> **周五晚**：Weekly Review 1.5h  
> 理论标注：心=心理表征 · 费=费曼 · 边=舒适区边缘 · 馈=专注反馈 · 整=整体性 · 联=知识关联

---

## W1 · P0  脚手架与 Runtime

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `npx copilotkit@latest create`；pnpm 安装 | 5 | 馈 |
| 二 | 读 docs：Chat / Generative UI 概览 | 5 | 心 |
| 三 | `api/copilotkit/route.ts` + BuiltInAgent | 5 | 馈 |
| 四 | CopilotKitProvider + layout | 4 | 心 |
| 五 | CopilotChat 首屏对话 | 4 | 边 |
| 六 | `.env.example`；密钥隔离检查 | 3 | 馈 |
| 日 | 费曼笔记 + Review | 1.5 | 费 |

---

## W2 · P0  v2 协议与验收

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | AG-UI vs v1 GraphQL 对照笔记 | 5 | 心 |
| 二 | CopilotSidebar 布局模式 | 5 | 边 |
| 三 | SSE Network 面板读事件 | 5 | 馈 |
| 四 | `p0-copilotkit-starter` README | 4 | 馈 |
| 五 | 部署试跑（Vercel 可选） | 4 | 馈 |
| 六 | P0 验收 | 3 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W3 · P1  Agent Context

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `useAgent` / `useAgentContext` 文档 | 5 | 心 |
| 二 | 把页面选中项注入 context | 5 | 边 |
| 三 | `p1-ag-ui-app` 脚手架 | 5 | 馈 |
| 四 | context 变更触发 Agent 行为 | 4 | 馈 |
| 五 | `generative-ui-patterns.md` 初稿 | 4 | 心 |
| 六 | 与 reactjs 状态思维对照 | 3 | 联 |
| 日 | Review | 1.5 | 馈 |

---

## W4 · P1  Frontend Tool + Interrupt

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `useFrontendTool` 导航/填表 | 5 | 边 |
| 二 | `useRenderToolCall` 自定义渲染 | 5 | 馈 |
| 三 | `useInterrupt` 确认流 | 5 | 边 |
| 四 | 完善 Sidebar 助手 UX | 4 | 边 |
| 五 | P1 验收演示 | 4 | 费 |
| 六 | 费曼：三模式选型 | 3 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W5 · P2  A2UI 消息协议

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 读 a2ui.org Message Reference | 5 | 心 |
| 二 | 手绘 createSurface 流程 | 5 | 心 |
| 三 | Runtime 开启 `a2ui: true` | 5 | 馈 |
| 四 | 内置 Catalog 首屏 | 4 | 边 |
| 五 | `a2ui-message-reference.md` 笔记 | 4 | 心 |
| 六 | 安全：Catalog 白名单 | 3 | 心 |
| 日 | Review | 1.5 | 馈 |

---

## W6 · P2  Fixed Schema Surfaces

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 预写 Fixed Schema JSON | 5 | 边 |
| 二 | Agent 只更新 dataModel | 5 | 边 |
| 三 | `p2-a2ui-surfaces` 订单卡片 | 5 | 边 |
| 四 | 流式渲染观察 | 4 | 馈 |
| 五 | 错误消息 fallback | 4 | 馈 |
| 六 | P2 验收 | 3 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W7 · P3  Catalog 设计

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `company-catalog-blueprint.md` | 5 | 整 |
| 二 | catalogId + schema 定义 | 5 | 心 |
| 三 | 映射 reactjs UserCard → Catalog | 5 | 联 |
| 四 | StatusBadge / TagList 入 Catalog | 4 | 边 |
| 五 | Provider `a2ui={{ catalog }}` | 4 | 馈 |
| 六 | Agent description 文案规范 | 3 | 馈 |
| 日 | Review | 1.5 | 馈 |

---

## W8 · P3  Theme + Dynamic（可选）

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | A2UI theme / renderer | 5 | 馈 |
| 二 | DataTable 或复杂组件入 Catalog | 5 | 边 |
| 三 | `p3-a2ui-catalog` 联调 | 5 | 边 |
| 四 | Dynamic Schema 实验（可选） | 4 | 边 |
| 五 | Fixed vs Dynamic 对比表 | 4 | 费 |
| 六 | P3 验收 | 3 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W9 · P4  LangGraph Runtime

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | LangGraphAgent 文档 | 5 | 心 |
| 二 | 本地 LangGraph 服务或 mock | 5 | 边 |
| 三 | `p4-langgraph-client` 脚手架 | 5 | 馈 |
| 四 | 端到端对话（无 A2UI） | 4 | 馈 |
| 五 | Agent emit A2UI 原型 | 4 | 边 |
| 六 | python-ai 项目对照 | 3 | 联 |
| 日 | Review | 1.5 | 馈 |

---

## W10 · P4  鉴权与错误态

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `onRequest` JWT 校验 | 5 | 馈 |
| 二 | properties → LangGraph configurable | 5 | 联 |
| 三 | 401/500 UI 降级 | 5 | 馈 |
| 四 | A2UI 由 LangGraph 驱动 demo | 4 | 边 |
| 五 | openharness Gateway 分工笔记 | 4 | 联 |
| 六 | P4 验收 | 3 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W11 · P5  业务嵌入

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `p5-company-agent-ui` Dashboard 布局 | 5 | 整 |
| 二 | CopilotSidebar + 业务路由 | 5 | 边 |
| 三 | 多 Agent `support` / `ops` | 5 | 边 |
| 四 | 大 Surface 骨架屏 | 4 | 馈 |
| 五 | a11y 键盘与 aria 检查 | 4 | 联 |
| 六 | ADR 初稿 | 3 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W12 · P5  测试与部署

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | Playwright E2E 冒烟 | 5 | 馈 |
| 二 | 生产环境变量与 build | 5 | 馈 |
| 三 | Vercel / Docker 部署 | 5 | 馈 |
| 四 | 作品集 README + 架构图 | 4 | 费 |
| 五 | 录屏脚本演练 | 4 | 费 |
| 六 | 总验收 | 3 | 费 |
| 日 | 结业 Review | 1.5 | 馈 |

---

## 四轨并行对照

| 本轨周 | reactjs | python-ai | openharness |
|--------|---------|-----------|-------------|
| W1–W2 | P3 Next | P0–P1 | — |
| W3–W6 | P2–P3 | P1–P2 | P0 预习 |
| W7–W10 | P3–P4 | P3 LangGraph | P4 Gateway |
| W11–W12 | P4 | P3–P6 | P5 后端 |
