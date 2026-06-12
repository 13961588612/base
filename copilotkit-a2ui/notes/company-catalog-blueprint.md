# 公司 A2UI Component Catalog 蓝图

> P3 定稿。将 **reactjs 设计系统** 映射为 Agent 可组合的 Catalog。

## 设计原则

1. **Catalog = 安全边界**：Agent 只能请求已注册组件，不能注入任意 JSX/HTML。
2. **每个组件有 agent-facing description**：模型靠描述选型，不靠 if-else。
3. **生产优先 Fixed Schema**：Catalog 组件 + 预定义 layout 模板。
4. **样式在客户端**：A2UI 不传 CSS 字符串；用 Tailwind theme 统一外观。

## Catalog 结构（CopilotKit）

```typescript
// catalog/company.ts
export const companyCatalog = {
  catalogId: "company-v1",
  includeBasicCatalog: true, // 保留 Text/Card 等内置
  components: {
    StatusBadge: {
      description: "Show order or ticket status. Use values: pending | active | done | error.",
      schema: { /* JSON Schema for props */ },
      render: StatusBadge,
    },
    UserCard: { /* ... */ },
    MetricTile: { /* ... */ },
  },
};
```

## 推荐首批组件（来自 reactjs w1）

| 组件 | Agent 用途 | 关键 props |
|------|------------|------------|
| `StatusBadge` | 状态展示 | `status`, `label?` |
| `UserCard` | 人员摘要 | `name`, `role` |
| `TagList` | 标签列表 | `tags: string[]` |
| `MetricTile` | KPI 数字 | `title`, `value`, `delta?` |
| `DataTable` | 只读表格 | `columns`, `rows` |

## 目录建议（p3-a2ui-catalog）

```
p3-a2ui-catalog/
├── catalog/
│   ├── index.ts           # 导出 companyCatalog
│   ├── schemas/           # JSON Schema per component
│   └── components/        # React 实现（可 symlink reactjs）
├── templates/
│   ├── order-summary.json # Fixed Schema 模板
│   └── ticket-panel.json
└── docs/
    └── catalog-changelog.md
```

## Agent Prompt 片段（Fixed Schema）

```
When showing order status, use catalogId "company-v1" and template "order-summary".
Only update dataModel paths defined in the template.
Do not invent component types outside the catalog.
```

## 版本治理

| 版本 | 变更 | 兼容 |
|------|------|------|
| company-v1 | 初始 5 组件 | — |
| company-v2 | 加 DataTable 列类型 | 保留 v1 catalogId 只读 |

## 与 Theme

- Tailwind design token → A2UI renderer theme
- 暗色模式：客户端 CSS 变量，Agent 不感知

## 验收（P3）

- [ ] catalogId 稳定且文档化
- [ ] 每个组件有 description + schema + Storybook 或截图
- [ ] Fixed 模板 ≥2 个

---

*待对接：公司 Figma / shadcn 组件库名称*
