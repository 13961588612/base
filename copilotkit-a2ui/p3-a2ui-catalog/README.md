# p3-a2ui-catalog · 公司 Component Catalog

W7–W8 专用。把 reactjs 组件映射为 **A2UI Catalog**。

## 目标

- [ ] `catalogId: "company-v1"`
- [ ] ≥3 组件：StatusBadge、UserCard、MetricTile（或 DataTable）
- [ ] Fixed 模板 ≥2
- [ ] 可选：Dynamic Schema 对比实验

## 目录

见 `../notes/company-catalog-blueprint.md`。

## Provider

```tsx
import { companyCatalog } from "@/catalog";

<CopilotKitProvider
  runtimeUrl="/api/copilotkit"
  a2ui={{ catalog: companyCatalog }}
>
```

## 与 reactjs 复用

可从 `../../reactjs/w1-react-basics/src/components/` 复制或提取 props 类型，**勿复制 any**。

## 验收

- [ ] Agent 能组合公司组件完成「订单摘要」Surface
- [ ] `catalog-changelog.md` 记录版本

## 通过后

W9：`../p4-langgraph-client`
