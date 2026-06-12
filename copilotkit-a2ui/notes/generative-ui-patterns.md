# Generative UI 三种模式选型

> CopilotKit 2026 指南 + 本仓库实践。P1 填完选型表。

## 模式对照

| 模式 | API | Agent 输出 | 渲染方 | 安全边界 |
|------|-----|------------|--------|----------|
| **Frontend Tool** | `useFrontendTool` | tool call 名 + args | 你写的 React handler | 仅注册过的 handler |
| **Render Tool Call** | `useRenderToolCall` | tool 结果 JSON | 按 tool 名映射组件 | 同左 |
| **A2UI Declarative** | Runtime `a2ui` + Catalog | A2UI 消息流 | Catalog 映射组件 | **Catalog 白名单** |
| **Headless** | `useAgent` | 任意事件 | 完全自绘 | 自行负责 |

## 决策树

```
需要跨 Web/移动复用同一份 Agent UI？
├─ 是 → A2UI + Catalog
└─ 否
    ├─ 只需改当前页局部状态/导航？
    │   └─ Frontend Tool
    ├─ Tool 结果要富渲染但结构固定？
    │   └─ Render ToolCall
    └─ 要完全自定义布局？
        └─ Headless + useAgent
```

## A2UI 子模式

| 子模式 | Schema 来源 | 延迟 | 可控性 | 公司推荐 |
|--------|-------------|------|--------|----------|
| **Fixed Schema** | 人写 JSON 树 | 低 | 高 | **生产默认** |
| **Dynamic Schema** | LLM 生成树 + 数据 | 高 | 中 | 探索/内部工具 |

## 场景示例

| 场景 | 推荐 | 原因 |
|------|------|------|
| 订单状态卡片 | A2UI Fixed | 结构固定、可审计 |
| 「打开设置页」 | Frontend Tool | 纯客户端路由 |
| 工单详情表格 | A2UI Catalog DataTable | 设计系统一致 |
| 审批确认 | useInterrupt + A2UI | HITL + 结构化展示 |
| 聊天里贴代码块 | 默认 Markdown | 不必 A2UI |

## 反模式

- 用 Dynamic A2UI 做 **支付/权限** 界面（应 Fixed + 严格 Catalog）
- 用 Frontend Tool 拼 **复杂表单**（应 A2UI dataModel 绑定）
- 在 Catalog 里注册 **任意 HTML** 组件（破坏安全模型）

---

*我的选型记录（请填写）：*

| 功能 | 选了 | 为什么 |
|------|------|--------|
| p1-ag-ui-app | | |
| p2-a2ui-surfaces | | |
| p5-company-agent-ui | | |
