# p1-ag-ui-app · AG-UI 客户端原语

W3–W4 专用。Sidebar 助手 + Context + Frontend Tool + Interrupt。

## 目标功能

- [ ] `useAgentContext`：当前选中业务对象
- [ ] `useFrontendTool`：如 `navigateTo`、`fillSearchQuery`
- [ ] `useRenderToolCall`：至少 1 个 Tool 富渲染
- [ ] `useInterrupt`：破坏性操作前确认
- [ ] `CopilotSidebar` 嵌入业务布局

## 目录建议

```
p1-ag-ui-app/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── api/copilotkit/route.ts
├── features/
│   ├── assistant/
│   │   ├── CopilotSidebarShell.tsx
│   │   ├── useAppContext.ts
│   │   └── frontendTools.ts
│   └── demo/
│       └── ProductList.tsx     # 可被 Agent 感知的页面
└── notes/
    └── generative-ui-choice.md # 填 ../notes/generative-ui-patterns.md
```

## 参考 API（v2）

| 需求 | Hook |
|------|------|
| 共享状态 | `useAgentContext` |
| Agent 调前端 | `useFrontendTool` |
| 渲染 Tool 结果 | `useRenderToolCall` |
| HITL | `useInterrupt` |
| 读 Agent 状态 | `useAgent` |

## 验收

- [ ] Agent 能根据 context 回答「当前选中的是哪个」
- [ ] 1 次 Frontend Tool 可演示
- [ ] 1 次 Interrupt 流程

## 通过后

W5：`../p2-a2ui-surfaces`
