# p2-a2ui-surfaces · A2UI Fixed Schema 练习

W5–W6 专用。理解 A2UI 消息流；**Fixed Schema** 订单/工单卡片。

## Runtime 配置

```typescript
const runtime = new CopilotRuntime({
  agents: { default: myAgent },
  a2ui: true, // 或 { injectA2UITool: false } + 手写 A2UI emit
});
```

## 目录建议

```
p2-a2ui-surfaces/
├── app/
│   └── api/copilotkit/route.ts
├── a2ui/
│   ├── templates/
│   │   └── order-summary.json   # Fixed component tree
│   └── fixtures/
│       └── sample-messages.jsonl
├── catalog/
│   └── basic.ts                 # 先用内置 + 少量扩展
└── notes/
    └── message-trace.md         # 记录 SSE 中 A2UI 事件
```

## 练习

1. 手读 `sample-messages.jsonl`，对照 `../notes/a2ui-message-reference.md`
2. Agent（或 mock）按序 emit：`createSurface` → `updateComponents` → `updateDataModel`
3. 观察 CopilotChat 内 Surface 流式出现

## 验收

- [ ] Fixed Schema：改 dataModel 即可换订单数据
- [ ] 消息顺序错误时有可见 fallback 或日志

## 通过后

W7：`../p3-a2ui-catalog`
