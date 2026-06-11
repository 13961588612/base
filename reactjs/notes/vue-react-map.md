# Vue ↔ React 对照表（学习过程中持续填写）

> **说明**：下表为学习起点，请你用**自己的话**改写「关键差异」列（费曼要求）。

| 概念 | Vue 3 | React 18 | 关键差异（你的理解） |
|------|-------|----------|----------------------|
| 响应式 | `ref` / `reactive` | `useState` | Vue 改 `.value` 自动触发更新；React 必须调用 `setState` 才会重渲染 |
| 派生状态 | `computed` | `useMemo` | 都避免重复计算；React 需手写依赖数组，不会自动收集 |
| 副作用 | `watch` / `watchEffect` | `useEffect` | Vue 自动追踪依赖；React 必须列出 deps，漏写会出 bug |
| 生命周期 | `onMounted` 等 | `useEffect(..., [])` | React 没有独立生命周期 API，统一进 useEffect |
| 全局状态 | Pinia | Zustand（W11 学） | 都是外部 store；React 里 store 只在 Client 组件用 |
| 路由 | Vue Router | React Router（W4）/ Next App Router（W8） | Vue 配置式；Next 是文件系统路由 |
| 模板 | SFC `<template>` | JSX | JSX 即 JavaScript，条件/列表都是表达式 |
| 双向绑定 | `v-model` | 受控组件 `value` + `onChange` | React 单向数据流，表单需显式回写 state |
| 列表 | `v-for` | `array.map()` + `key` | key 同样重要，用稳定 id 而非 index（可变列表时） |
| 条件 | `v-if` / `v-show` | `&&` / 三元 / 提前 return | 无指令，直接用 JS 表达式 |

## 为何 React 大多不需要 watch？

Vue 的 `watch` 用于「当 A 变时做 B」。React 里通常：

1. **事件里直接做 B**（点击、提交时处理，而非盯 state）
2. **渲染时派生**（用变量或 `useMemo` 从 state 算出展示值）
3. **确实要同步副作用** 才用 `useEffect`，并写清 deps

## 易错迁移习惯（自查）

- [ ] 是否在 useEffect 里「模拟 watch」而不写依赖？
- [ ] 是否想给 props 加 reactive？
- [ ] 是否在 RSC 里找 Pinia 等价物？（W8 前不会遇到）
