# RSC vs Client Component 决策树（W8 填写）

```
组件是否需要：
├─ useState / useReducer / useEffect / 浏览器 API？
│   └─ 是 → 'use client'
├─ 仅展示服务端数据、无交互？
│   └─ 是 → Server Component（默认）
├─ 子组件需要交互但父组件不需要？
│   └─ 父 RSC + 子 Client（组合模式）
└─ 需要 Zustand / TanStack Query？
    └─ Client（且注意 SSR 水合）
```

## 我的项目文件标注（W10 前完成）

| 文件路径 | RSC / Client | 理由 |
|----------|--------------|------|
| | | |
