# React + Next.js 全栈 · 知识点 Checklist

> 用法：学完打 `[x]`，阶段末对照验收。理论列：心=心理表征 · 费=费曼 · 边=舒适区边缘 · 馈=专注反馈 · 整=整体性学习 · 联=知识关联

---

## P0 · 环境与映射（W1）

- [x] Vue↔React 对照表完成（ref/reactive、computed、watch、Pinia、Router、SFC/JSX）— 联
- [ ] 能解释 React 无自动依赖追踪 — 心（见 notes/react-mental-model.md，请改用自己的话）
- [x] Vite + React 18 + TS 项目跑通 — 馈
- [ ] 5 个函数组件 + 费曼解释 — 费（已有 4 个，周二补第 5 个 + 讲解）
- [ ] Tailwind 卡片列表页 — 边（周五）
- [x] Props interface 无 any — 边
- [ ] 项目部署成功 — 馈（周日）

---

## P1 · React 18 核心（W2–W4）

### Hooks
- [ ] useState 闭包陷阱能复现并修复 — 心
- [ ] useEffect 依赖数组原则 — 心
- [ ] useRef DOM vs 可变值 — 心
- [ ] useMemo/useCallback 仅 Profiler 证明后使用 — 馈
- [ ] 自定义 Hook ≥3 个 — 整
- [ ] useReducer + Context — 联

### Concurrent
- [ ] useTransition / useDeferredValue — 边
- [ ] Suspense + lazy — 整
- [ ] Strict Mode 双重渲染含义 — 心

### 项目
- [ ] 项目1 天气页 — 边
- [ ] 项目2 Kanban — 边
- [ ] 项目3 仪表盘 — 馈
- [ ] React Router v6 嵌套路由 + loader — 联

### Vue 迁移
- [ ] 能说明「为何 React 不需要 watch 大部分场景」 — 费

---

## P2 · SPA 生态（W5–W7）

- [ ] TanStack Query：queryKey、staleTime、invalidate — 心
- [ ] 乐观更新 — 边
- [ ] React Hook Form + Zod — 馈
- [ ] Tailwind：token、暗色、组件抽取 — 整
- [ ] ESLint + Prettier + husky — 馈
- [ ] MSW Mock API — 联
- [ ] 博客 SPA 上线 — 边
- [ ] 能回答「何时 SPA 够、何时要 Next」 — 费

---

## P3 · Next.js + RSC 全栈（W8–W10）⭐

### App Router 基础
- [ ] layout / page / loading / error / not-found — 整
- [ ] 文件系统路由与动态路由 `[id]` — 心
- [ ] Route Groups `(group)` — 心
- [ ] Parallel Routes / Intercepting（了解即可） — 心

### RSC 核心
- [ ] RSC vs Client 决策树 — 心
- [ ] `'use client'` 使用边界 — 心
- [ ] RSC 中不能用 useState/useEffect — 馈
- [ ] Props 从 Server → Client 序列化限制 — 心
- [ ] 同一功能 RSC 版 vs Client+Query 对比实验 — 馈

### 数据获取
- [ ] 服务端 fetch + cache — 心
- [ ] `revalidate` 路径/标签 — 心
- [ ] `no-store` vs 静态 — 联
- [ ] Streaming + Suspense — 整

### Server Actions & API
- [ ] Server Action 表单 mutation — 心
- [ ] revalidatePath / revalidateTag — 馈
- [ ] Route Handlers vs Server Actions 选型 — 联
- [ ] middleware 路由守卫 — 馈

### 鉴权 & 数据库（PostgreSQL）
- [ ] 本地 Docker PostgreSQL 跑通 + `psql` 或 TablePlus 连接 — 馈
- [ ] Prisma `provider = "postgresql"` + migrate + seed — 联
- [ ] 理解 pg 基础：schema / table / index / 外键 — 心
- [ ] NextAuth/Clerk 登录流程 — 边
- [ ] 保护路由/server action — 馈
- [ ] RSC 读 pg + Server Action 写 pg — 边
- [ ] 全栈项目部署 Vercel + 云 PostgreSQL（Neon/Supabase 等）— 馈

### 必会概念（面试级）
- [ ] SSR / SSG / ISR / 动态渲染区别 — 费
- [ ] 能白板画请求到 RSC 到 hydration — 心

---

## P4 · 状态 + 性能 + 质量（W11–W13）

### 状态
- [ ] 服务端/URL/Zustand/Query 决策树 — 心
- [ ] Zustand 仅 Client 组件 — 联
- [ ] TS 泛型组件 — 边
- [ ] Discriminated Union UI 状态 — 边

### Next 性能
- [ ] next/image — 馈
- [ ] dynamic() — 馈
- [ ] generateStaticParams — 边
- [ ] Route Segment Config — 心

### 测试 & a11y
- [ ] Vitest + RTL ≥3 组件/Hook — 馈
- [ ] Playwright E2E ≥2 流程 — 整
- [ ] jsx-a11y 无 critical — 联
- [ ] Lighthouse Performance ≥85 — 馈

---

## P5 · React 19 + 作品集（W14–W17）

### React 19
- [ ] useActionState — 心
- [ ] useFormStatus — 心
- [ ] useOptimistic + Server Actions — 边
- [ ] React Compiler（可选对比） — 联
- [ ] PPR 概念（了解） — 心

### 专业实践
- [ ] 开源源码阅读笔记 — 心
- [ ] ADR 文档 ≥1 — 费
- [ ] Query + Next SSR 水合模式 — 联
- [ ] 作品集：Next 15 + PostgreSQL + 鉴权 + RSC — 边
- [ ] 作品集：测试 + CI — 馈
- [ ] 博客 2 篇 — 费
- [ ] 模拟面试完成 — 馈

---

## 跨域整合（全程）

- [ ] `notes/vue-react-map.md` 持续更新 — 联
- [ ] `notes/rsc-decision-tree.md` — 心
- [ ] 每周 200 字跨域映射 ≥17 篇 — 整

---

*配合 LEARNING_PLAN.md v1.0 使用*
