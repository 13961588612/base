# A2UI 消息速查（v0.9 主线）

> 官方：[Message Reference](https://a2ui.org/reference/messages/)。W5 对照实验更新。

## 核心概念

| 概念 | 说明 |
|------|------|
| **Surface** | 一块 UI 画布（对话框内区域、侧栏 panel） |
| **Component** | Catalog 中的类型实例（Text、Card、Button…） |
| **Data Model** | 组件绑定的数据；JSON Pointer 路径更新 |
| **Catalog** | 允许 Agent 使用的组件类型集合 |

## v0.9 消息类型

| 消息 | 作用 |
|------|------|
| `createSurface` | 创建 surfaceId + **catalogId**（v0.9 替代 v0.8 `beginRendering` 部分职责） |
| `updateComponents` | 扁平 adjacency list 定义组件树；**必须含 `"id": "root"`** |
| `updateDataModel` | 更新绑定数据 |
| `deleteSurface` | 移除 surface |

## 推荐顺序

```
1. createSurface     { surfaceId, catalogId, version }
2. updateComponents  { surfaceId, components: [...] }  // 含 root
3. updateDataModel   { surfaceId, updates: [...] }
4. （流式）可多次 updateComponents / updateDataModel
5. deleteSurface     { surfaceId }  // 可选
```

**注意**：v0.8 的 `beginRendering` 在 v0.9 由 `createSurface` + root 约定替代；读旧文时对照版本。

## updateComponents 片段示例

```json
{
  "surfaceId": "order-card",
  "components": [
    { "id": "root", "component": "Card", "children": ["title", "status"] },
    { "id": "title", "component": "Text", "text": "订单 #1024" },
    { "id": "status", "component": "StatusBadge", "status": "/order/status" }
  ]
}
```

数据绑定路径在 `updateDataModel` 中填充。

## CopilotKit 侧开关

```typescript
const runtime = new CopilotRuntime({
  agents: { default: myAgent },
  a2ui: {
    injectA2UITool: true, // Dynamic：注入 render_a2ui tool
  },
});
```

```tsx
<CopilotKitProvider
  runtimeUrl="/api/copilotkit"
  a2ui={{ catalog: myCatalog }}
>
  {children}
</CopilotKitProvider>
```

无 Runtime `a2ui` 配置 → A2UI 消息当普通 tool result，**不会渲染**。

## 实验记录（W5–W6）

| 实验 | 预期 | 实际 | 备注 |
|------|------|------|------|
| 内置 Catalog 卡片 | 流式出现 | | |
| Fixed Schema | 只改 dataModel | | |
| 错误 catalogId | fallback | | |

---

*薄弱点：*

- 
