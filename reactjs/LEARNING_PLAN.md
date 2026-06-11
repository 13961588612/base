# React 18/19 + Next.js 全栈学习计划

> **你的画像（v1.0）**
>
> | 项 | 值 |
> |----|-----|
> | JS / TS / HTML / CSS | 各 3/5 |
> | 框架经验 | 学过 Vue（可加速组件思维，需重建 React 心智模型） |
> | 每周投入 | 25h |
> | 目标 | 全栈（React 前端 + Next.js 服务端能力） |
> | 周期 | **16–17 周，不压缩不延长**（多出的时间用于加深 Next.js/RSC，而非赶进度） |
> | 样式 | Tailwind CSS |
> | 客户端状态 | Zustand |
> | 数据库 | **PostgreSQL**（Prisma ORM + `pg` 驱动） |
>
> **终极目标**：能独立开发、部署、维护 **Next.js 全栈** 生产应用（RSC、Server Actions、鉴权、数据库、测试、性能）。

---

## 一、学习内容总览（6 阶段 · 17 周）

| 阶段 | 主题 | 核心产出 | 周期 |
|------|------|----------|------|
| P0 | 环境与 Vue→React 映射 | React 18 项目 + 概念对照笔记 | 1 周 |
| P1 | React 18 核心 | 3 个 Vite SPA 小项目 | 3 周 |
| P2 | SPA 生态（Tailwind/Query/表单） | 博客前台 SPA | 3 周 |
| **P3** | **Next.js + RSC 全栈** | **App Router 全栈项目（含 DB）** | **3 周** |
| P4 | 状态架构 + 性能质量 | Zustand 分层 + 测试 + Next 性能优化 | 3 周 |
| P5 | React 19 + 专业作品集 | Next.js 全栈作品集 + 博客 | 4 周 |

### 为何必须加 Next.js / RSC？

| 能力 | 仅 Vite SPA | 加 Next.js |
|------|-------------|------------|
| SSR / SEO | 需额外方案 | 原生 |
| RSC 服务端组件 | ❌ | ✅ App Router |
| Server Actions | ❌ | ✅ 与 React 19 对齐 |
| API / BFF | 独立后端 | Route Handlers 一体 |
| 全栈部署 | 前后分离 | Vercel 一键 |
| 缓存策略 | 全靠 Query | fetch cache + revalidate |

**结论**：SPA 阶段（P1–P2）打 React 基本功；**P3 起主战场切换到 Next.js**，React 19 特性在 Next 15 里落地。

---

## 二、分阶段详细内容

### P0 · 环境与 Vue→React 映射（W1）

**学习目标**：建立 React 心理表征；完成 Vue 概念迁移，避免「用 Vue 的方式写 React」。

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 0.0 | 写「Vue ↔ React」对照表：响应式/ref/reactive、computed、watch、Pinia、Vue Router、SFC vs JSX | 知识关联 | 2h |
| 0.1 | Vite 创建 React 18 + TS 项目，画「浏览器 → ReactDOM → 组件树」流程图 | 心理表征 | 2h |
| 0.2 | 手写 5 个函数组件，每个用费曼话术解释（刻意不用 Vue 语法习惯） | 费曼技巧 | 3h |
| 0.3 | 同一 Todo：Vue 3 Composition API 版 vs React 版并列，标注「思维差异」 | 知识关联 | 2h |
| 0.4 | 阅读 react.dev「Thinking in React」并完成拆分练习 | 整体性学习 | 2h |
| 0.5 | 用 **Tailwind** 实现卡片列表页（跳过纯 CSS 深挖，CSS 3 可直接进 Tailwind） | 舒适区边缘 | 4h |
| 0.6 | **缓冲/加深**：react.dev/learn 前 3 章 + TS 3 补强——给 Props 写 interface 而非 any | 舒适区边缘 | 4h |

**验收**：能口述「React 无自动依赖追踪，为何还要 useEffect 依赖数组」；项目可部署。

---

### P1 · React 18 核心（W2–W4）

**学习目标**：Hooks 熟练；Concurrent 特性；3 个 SPA 项目巩固。

#### W2 · Hooks 基础

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 1.1 | useState / useEffect / useRef 场景卡片 + 反模式；对比 Vue watch/onMounted | 心理表征 + 知识关联 | 4h |
| 1.2 | Todo App（增删改、过滤），不用状态库 | 专注反馈 | 5h |
| 1.3 | DevTools 抓 3 次多余渲染并修复 | 专注反馈 | 2h |
| 1.4 | **项目 1**：天气查询页（fetch 三态） | 舒适区边缘 | 6h |
| 1.5 | **缓冲**：TS 类型——API 响应类型、联合类型收窄 | 舒适区边缘 | 4h |

#### W3 · Hooks 进阶

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 1.6 | useMemo/useCallback/memo：Profiler 验证后再用 | 专注反馈 | 3h |
| 1.7 | 自定义 Hook：useFetch、useDebounce、useLocalStorage | 整体性学习 | 4h |
| 1.8 | useReducer + Context 主题切换；对比 Pinia 写法差异 | 知识关联 | 4h |
| 1.9 | **项目 2**：Kanban 看板（拖拽） | 舒适区边缘 | 8h |
| 1.10 | **缓冲**：shadcn/ui 初探（Tailwind 组件库生态） | 心理表征 | 3h |

#### W4 · Concurrent

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 1.11 | createRoot、Strict Mode | 心理表征 | 2h |
| 1.12 | useTransition + useDeferredValue 搜索列表 | 舒适区边缘 | 4h |
| 1.13 | Suspense + lazy 路由级分割 | 整体性学习 | 4h |
| 1.14 | **项目 3**：多 Tab 仪表盘（lazy + Suspense） | 专注反馈 | 8h |
| 1.15 | **缓冲**：React Router v6 基础（嵌套路由、loader）——为理解 Next 路由铺垫 | 知识关联 | 4h |

**验收**：3 项目上线 GitHub；能解释 Hooks 闭包陷阱；能对比 Vue 与 React 数据流。

---

### P2 · SPA 生态（W5–W7）

**学习目标**：TanStack Query、表单、Tailwind 工程化；**SPA 作为 Client Component 思维训练**。

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 2.1 | TanStack Query：缓存、staleTime、乐观更新；对比 Vue Query/Pinia 分工 | 知识关联 | 6h |
| 2.2 | React Hook Form + Zod | 专注反馈 | 4h |
| 2.3 | Tailwind 设计 token、暗色模式、组件抽取模式 | 整体性学习 | 5h |
| 2.4 | ESLint + Prettier + husky | 工程化 | 2h |
| 2.5 | MSW Mock REST API | 知识关联（全栈契约） | 3h |
| 2.6 | **中型 SPA 项目**：博客/CMS 前台（列表/详情/搜索/登录 Mock） | 舒适区边缘 | 22h |
| 2.7 | **缓冲/预习**：Next.js 官方 Learn 课程前几章（App Router 概览） | 心理表征 | 3h |

**验收**：能说明「何时 SPA 足够、何时必须 Next」；项目 features 目录结构清晰。

---

### P3 · Next.js + RSC 全栈（W8–W10）⭐ 新增核心

**学习目标**：掌握 App Router、RSC/Client 边界、数据获取、Server Actions、Route Handlers、鉴权与数据库。

#### W8 · App Router 与 RSC 心智模型

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 3.1 | `create-next-app`（App Router + TS + Tailwind），画「请求 → RSC Payload →  hydration」流程 | 心理表征 | 3h |
| 3.2 | **RSC vs Client Component**：`'use client'` 决策树（交互/浏览器 API/状态 → Client） | 心理表征 | 4h |
| 3.3 | 文件系统路由：layout / page / loading / error / not-found | 整体性学习 | 3h |
| 3.4 | 服务端 fetch + `cache` / `revalidate` / `no-store` 对比 CSR | 知识关联 | 4h |
| 3.5 | 练习：同一列表页分别用 RSC fetch 与 Client+Query 实现，对比 TTFB/SEO/交互 | 专注反馈 | 6h |
| 3.6 | **缓冲**：Next.js Learn「Routing」「Data Fetching」全完成 | 舒适区边缘 | 3h |

#### W9 · Server Actions + Route Handlers + 鉴权

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 3.7 | Server Actions：表单 mutation、revalidatePath/Tag | 心理表征 | 4h |
| 3.8 | Route Handlers（`/api/*`）vs Server Actions 选型 | 知识关联 | 3h |
| 3.9 | NextAuth.js v5 或 Clerk 接入（登录/会话/保护路由） | 舒适区边缘 | 6h |
| 3.10 | 中间件 middleware：路由守卫、redirect | 专注反馈 | 3h |
| 3.11 | Streaming + Suspense 边界在 Next 中的用法 | 整体性学习 | 4h |
| 3.12 | **缓冲**：读 Next.js 文档「Server and Client Composition Patterns」 | 心理表征 | 2h |

#### W10 · 数据库 + 全栈项目冲刺

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 3.13 | 本地 Docker 起 PostgreSQL + Prisma init/migrate；`DATABASE_URL` 连接 pg | 知识关联（全栈） | 5h |
| 3.14 | RSC 读库 + Server Actions 写库 + Client 乐观 UI（useOptimistic 预习） | 舒适区边缘 | 5h |
| 3.15 | **全栈项目 MVP**：SaaS 控制台或电商——≥4 模块、登录、DB、RSC 列表 + Server Action 表单 | 舒适区边缘 | 28h |

**验收**：
- [ ] 能白板画出 RSC / Client 组件边界
- [ ] 能解释 SSR / SSG / ISR / 动态 RSC 选型
- [ ] 全栈项目部署 Vercel + PostgreSQL（Neon / Supabase / Vercel Postgres 任选）

---

### P4 · 状态架构 + 性能质量（W11–W13）

**学习目标**：Zustand 在 Next 中的用法；Next 性能；测试体系。

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 4.1 | 状态三层决策树：DB 服务端 / RSC props / URL / Zustand / Query | 心理表征 | 2h |
| 4.2 | Zustand 跨 Client 组件 + 持久化；**禁止**在 RSC 里用 Zustand | 知识关联 | 5h |
| 4.3 | TS 进阶：泛型组件、Discriminated Union 状态机 | 舒适区边缘 | 6h |
| 4.4 | Next 性能：`<Image>`、dynamic import、Route Segment Config、`generateStaticParams` | 专注反馈 | 4h |
| 4.5 | React Profiler + Lighthouse + Next Analytics 基线 | 专注反馈 | 3h |
| 4.6 | 虚拟列表（TanStack Virtual） | 舒适区边缘 | 4h |
| 4.7 | Vitest + RTL 测 Client 组件与 Hooks | 专注反馈 | 8h |
| 4.8 | Playwright E2E：登录 + 核心 CRUD | 整体性学习 | 5h |
| 4.9 | a11y：jsx-a11y + 键盘导航 | 知识关联 | 3h |
| 4.10 | 对 P3 全栈项目：性能 + 测试 + a11y 一轮改进 | 专注反馈 | 12h |

**验收**：Lighthouse ≥85；核心路径 E2E 通过；能讲清 P3 项目状态分层。

---

### P5 · React 19 + Next 15 + 作品集（W14–W17）

**学习目标**：React 19 在 Next 15 落地；生产级全栈作品集。

#### W14 · React 19 × Next 15

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 5.1 | useActionState / useFormStatus 替换传统表单提交 | 心理表征 | 4h |
| 5.2 | useOptimistic + Server Actions 完整乐观流 | 舒适区边缘 | 4h |
| 5.3 | React Compiler（Next 配置 experimental）对比手动 memo | 知识关联 | 3h |
| 5.4 | Partial Prerendering（PPR）概念与 Next canary 体验（可选） | 舒适区边缘 | 3h |
| 5.5 | **缓冲**：react.dev 19 迁移指南 + Next 15 升级说明 | 整体性学习 | 3h |

#### W15 · 开源与架构

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 5.6 | 读 shadcn/ui 源码 1 个组件 + Next.js 某 RSC 示例 | 心理表征 | 6h |
| 5.7 | Tech Lead 式 Code Review P3 项目 | 费曼 + 专注反馈 | 3h |
| 5.8 | 写 ADR：为何某页面用 RSC、某功能用 Client | 费曼技巧 | 2h |
| 5.9 | **缓冲**：TanStack Query 在 Next Client 组件中的 SSR 水合模式 | 知识关联 | 4h |

#### W16–W17 · 作品集

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 5.10 | **全栈作品集**（Next 15 + DB + 鉴权 + RSC/Server Actions + 测试） | 舒适区边缘 | 55h |
| 5.11 | 博客 2 篇：「Vue 开发者转 React 心智差异」「RSC 边界实践 ADR」 | 费曼技巧 | 6h |
| 5.12 | 模拟面试：30min  live coding + 15min 架构问答（RSC/缓存/鉴权） | 专注反馈 | 4h |

**验收**：作品集可演示；含 README 架构图；测试 + CI；能答 Next/RSC 高频面试题。

---

## 三、17 周进度表（25h/周）

```
周次    阶段    主题                          约时长
──────────────────────────────────────────────────────────
W1      P0      Vue→React 映射 + Tailwind      25h
W2      P1      Hooks 基础 + 项目1             25h
W3      P1      Hooks 进阶 + 项目2             25h
W4      P1      Concurrent + 项目3 + Router  25h
W5      P2      Query + Hook Form              25h
W6      P2      Tailwind 深入 + MSW            25h
W7      P2      博客 SPA 冲刺 + Next 预习      25h
W8      P3      App Router + RSC ⭐            25h
W9      P3      Server Actions + 鉴权 ⭐       25h
W10     P3      Prisma + PostgreSQL + 全栈 ⭐  25h
W11     P4      Zustand + TS + Next 性能       25h
W12     P4      测试 Vitest + Playwright       25h
W13     P4      a11y + 项目质量改进            25h
W14     P5      React 19 + Next 15             25h
W15     P5      开源阅读 + ADR                 25h
W16     P5      作品集冲刺                     25h
W17     P5      作品集 + 博客 + 模拟面试       25h
```

**25h 分配建议（每周）**：核心学习 ~18h · 缓冲加深 ~4h · 反馈复盘 ~1.5h · 跨域整合 ~1.5h

---

## 四、反馈与调整机制

（同 v0.1，补充 Next 专项）

| 场景 | 调整 |
|------|------|
| RSC/Client 边界混乱 | 暂停新课，只做「标注练习」：给现有项目每个文件标 RSC/Client 并说明理由 |
| Server Action 报错 | 25min 最小 demo：仅 server action + 1 个表单，不加 DB |
| 全栈项目超时 | 本地 Docker pg 保持不动，先 2 模块 MVP；上线再迁云 PG |

**Vue 迁移专项检查（W2 末）**：是否仍在找「Vue 里的 watch 等价物」→ 若是，加练「事件驱动 vs 响应式」对比文。

---

## 五、跨知识整合

| 整合 | 做法 | 理论 |
|------|------|------|
| Vue ↔ React | 每学一概念填对照表一行 | 知识关联 |
| Vue Router ↔ Next App Router | 画路由树对比（file-based vs config） | 知识关联 |
| RSC ↔ 后端 | 「RSC = 在服务端跑的 React 组件」↔ MVC 中 Controller 返回 View | 心理表征 |
| Server Actions ↔ REST | 同一 CRUD 写 Action 版 + Route Handler 版，列优缺点 | 整体性学习 |
| DB ↔ UI | Prisma schema 变更 → 迁移 → RSC 列表自动反映 | 专注反馈 |
| HTTP 缓存 ↔ Next | 浏览器缓存 / CDN / fetch revalidate 三层对照 | 整体性学习 |

---

## 六、推荐资源

| 类型 | 资源 |
|------|------|
| React | [react.dev](https://react.dev) |
| Next.js | [nextjs.org/learn](https://nextjs.org/learn) + App Router 文档 |
| RSC | React 文档「Server Components」+ Next 「Server/Client Composition」 |
| 样式 | Tailwind 文档 + [ui.shadcn.com](https://ui.shadcn.com) |
| 状态 | Zustand 文档；TanStack Query 文档 |
| 全栈 | Prisma + PostgreSQL 文档；Docker Postgres 本地；Neon/Supabase 云 PG |
| 鉴权 | NextAuth 或 Clerk 文档 |
| 对比 | 自维护 `notes/vue-react-map.md` |

---

## 七、文件索引

**包管理**：本领域所有 JS/TS 项目使用 **pnpm**（见仓库根 `README.md` 工具约定）。

```
reactjs/
├── LEARNING_PLAN.md       ← 本文件 v1.1
├── CHECKLIST.md           ← 知识点勾选
├── WEEKLY_SCHEDULE.md     ← 逐周执行表
└── notes/                 ← vue-react-map、rsc-decision-tree、postgresql-setup
```

---

*v1.1 · JS/TS/HTML/CSS=3 · Vue · 25h/周 · 全栈 · Tailwind · Zustand · PostgreSQL · 17周*
