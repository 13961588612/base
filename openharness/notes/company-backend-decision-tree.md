# 公司 Agent 后端 · 技术选型决策树

> 在 openharness / python-ai / 自研 Gateway 之间选型。阶段末用真实项目填表。

## 快速决策

```
需要公司统一 IM/API 入口 + Tool 治理？
│
├─ 是 → OpenHarness 作 Harness 层（本轨主线）
│       │
│       ├─ 内部能力已有 LangChain Agent？
│       │   └─ ✅ 包装为 MCP，不搬逻辑
│       │
│       └─ 固定多步审批 + checkpoint？
│           └─ ✅ LangGraph 子服务 + MCP 暴露
│
└─ 否，只是单业务 PoC？
    └─ ✅ python-ai create_agent / LangGraph 即可
```

## 三层对比

| 维度 | 仅 LangChain/FastAPI | OpenHarness | OpenHarness + LangGraph MCP |
|------|---------------------|-------------|----------------------------|
| 上手 | 快 | 中（学 Harness 概念） | 中高 |
| 多通道 Gateway | 需自研 | ohmo 模式可扩展 | 同左 |
| Tool 治理 | 自研 | 内置 permission+hook | 同左 |
| 复杂工作流 | LangGraph 强 | coordinator 够用 | **最佳** |
| 企业审计 | 自研 | Hook 补齐 | 同左 |
| 适合 | 单团队 PoC | **公司统一入口** | 大型平台 |

## OpenHarness 适用场景（公司）

✅ **适合**：
- 多部门共用同一 Agent 后端
- 需要 Skills/Plugin 版本化治理
- 飞书/Slack + 内部 API 多入口
- 希望 Tool 权限、审计一致

❌ **不适合单独使用**：
- 纯批处理 ETL（无对话）
- 强合规已购商业 Agent 平台且禁止自托管
- 团队不愿维护 Python 运行时

## Tool 暴露方式选型

| 方式 | 何时用 | 风险 |
|------|--------|------|
| 内置 Tool | 文件/Shell 等通用能力 | 生产限制 Bash/Write |
| 自定义 Tool | 简单只读域 API | 需维护 Python 代码 |
| **MCP** | **跨团队、跨语言、内部系统** | 网络与 auth 要管好 |
| LangGraph MCP | 复杂状态机子流程 | 运维两个服务 |

## 自检（立项前必答）

1. 是否有 **≥2 个** 消费通道（IM + API）？→ 倾向 OpenHarness Gateway
2. 是否已有 **python-ai** Agent 要复用？→ MCP 包装
3. 审计是否 **强制**？→ P5 Hook 提前，不用 auto mode
4. 是否接受 **MIT 开源** Harness 自托管？→ 否则评估商业方案

---

*项目选型记录：*

| 项目 | 选型 | 为什么 | 若重来 |
|------|------|--------|--------|
| p5-company-agent-platform | | | |
