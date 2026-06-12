# CopilotKit + A2UI · 知识点 Checklist

> 用法：学完打 `[x]`，阶段末对照验收。理论列：心=心理表征 · 费=费曼 · 边=舒适区边缘 · 馈=专注反馈 · 整=整体性学习 · 联=知识关联

---

## 入口门槛

- [ ] reactjs P0–P1（组件、Hooks、TS、Tailwind） — 联
- [ ] Next.js App Router 基础（可与 P0 并行） — 心
- [ ] python-ai P1+ 或在 W9 前完成（LangGraph 对接） — 联

---

## P0 · CopilotKit v2 + Runtime（W1–W2）

- [ ] `npx copilotkit@latest create` 或等价脚手架 — 馈
- [ ] `createCopilotRuntimeHandler` + `BuiltInAgent` — 馈
- [ ] `CopilotKitProvider` + `runtimeUrl` 同源 — 心
- [ ] CopilotChat / CopilotSidebar 嵌入 — 边
- [ ] v1 GraphQL vs v2 AG-UI 差异 — 心
- [ ] API Key 仅服务端 — 馈
- [ ] 项目 `p0-copilotkit-starter` — 边
- [ ] 费曼：Runtime vs Agent — 费

---

## P1 · AG-UI 客户端原语（W3–W4）

- [ ] `useAgent` / `useAgentContext` — 心
- [ ] `useFrontendTool` — 边
- [ ] `useRenderToolCall` — 馈
- [ ] `useInterrupt` HITL — 边
- [ ] Generative UI 三模式选型表 — 心
- [ ] 项目 `p1-ag-ui-app` — 边
- [ ] 费曼：何时从 Frontend Tool 升级到 A2UI — 费

---

## P2 · A2UI 协议（W5–W6）

- [ ] `createSurface` / `updateComponents` / `updateDataModel` — 心
- [ ] 消息顺序与 `deleteSurface` — 心
- [ ] Runtime `a2ui: true` / `injectA2UITool` — 馈
- [ ] 内置 Catalog 渲染 — 边
- [ ] Fixed Schema 模式 — 边
- [ ] Catalog 白名单安全模型 — 心
- [ ] 项目 `p2-a2ui-surfaces` — 边

---

## P3 · 自定义 Catalog（W7–W8）

- [ ] `catalogId` + 组件 schema + React 映射 — 心
- [ ] `includeBasicCatalog` 策略 — 边
- [ ] 公司组件 ≥3 入 Catalog — 边
- [ ] A2UI theme / renderer 配置 — 馈
- [ ] Dynamic Schema（可选） — 边
- [ ] A2UI Composer 模板进 prompt — 联
- [ ] 项目 `p3-a2ui-catalog` — 边
- [ ] 费曼：Fixed vs Dynamic — 费

---

## P4 · LangGraph / 公司 Agent（W9–W10）

- [ ] `LangGraphAgent` 配置 — 心
- [ ] Agent 侧 emit A2UI — 边
- [ ] `onRequest` 鉴权 — 馈
- [ ] JWT → LangGraph configurable — 联
- [ ] 错误态与 fallback UI — 馈
- [ ] 与 openharness Gateway 分工理解 — 联
- [ ] 项目 `p4-langgraph-client` — 边

---

## P5 · 公司 Agent 客户端 MVP（W11–W12）

- [ ] 业务页 + CopilotSidebar 嵌入 — 整
- [ ] 多 Agent 路由 — 边
- [ ] 流式 A2UI 性能（骨架屏） — 馈
- [ ] a11y 基线 — 联
- [ ] Playwright E2E 冒烟 — 馈
- [ ] 部署（Vercel / Docker） — 馈
- [ ] ADR：CopilotKit+A2UI 选型 — 费
- [ ] 项目 `p5-company-agent-ui` — 边

---

## 跨域整合（全程）

- [ ] `notes/ag-ui-a2ui-stack-map.md` 持续更新 — 联
- [ ] `notes/company-catalog-blueprint.md` 定稿 — 心
- [ ] 每周 200 字客户端实践笔记 ≥12 篇 — 整

---

## 选型速查（阶段末必会）

- [ ] Frontend Tool vs A2UI vs Headless — 费
- [ ] Fixed vs Dynamic A2UI Schema — 费
- [ ] CopilotKit Runtime vs 纯 SSE 自研 — 费

---

*配合 LEARNING_PLAN.md v1.0 使用*
