# Agent 技术选型决策树

> 学完 P1/P3/P5 后用自己的话补充「真实踩坑」案例。

## 快速决策

```
你的任务是什么？
│
├─ 固定步骤、可画流程图、需要审批/回滚/持久化？
│   └─ ✅ LangGraph StateGraph
│
├─ 开放式多步任务（研究/编码/运维）、上下文会膨胀、要规划+子任务？
│   └─ ✅ DeepAgents create_deep_agent
│
└─ 少量工具、短对话、快速验证想法？
    └─ ✅ LangChain create_agent
```

## 对比表

| 维度 | LangChain Agent | LangGraph | DeepAgents |
|------|-----------------|-----------|------------|
| 上手速度 | ⭐⭐⭐ 最快 | ⭐⭐ 中等 | ⭐⭐ 中等 |
| 流程可控性 | ⭐ 低（模型决定） | ⭐⭐⭐ 高 | ⭐⭐ 中高 |
| 持久化 / HITL | 需自拼 | 原生 | 原生 |
| 长任务 / 上下文 | 易膨胀 | 需自建模式 | 内置规划+文件系统 |
| 子代理 | 需自建 | 子图实现 | 内置 `subagents` |
| 代码量 | 最少 | 中等 | 少（能力内置） |
| 适合阶段 | P1 原型 | P3 工作流 | P5 深代理 |

## 升级路径（推荐）

```
create_agent（验证 tool 设计）
    ↓ 需要固定流程 / checkpoint
StateGraph（显式编排）
    ↓ 需要规划 / 子代理 / 文件持久化
create_deep_agent（深代理脚手架）
```

**反模式**：一上来就用 DeepAgents 做「只有一个 calculator tool」的 demo——过度工程。

## 自检问题（选型前必答）

1. 能否用 3 句话描述用户任务的**固定步骤**？若能，优先考虑 LangGraph。
2. 任务是否可能超过 **10 次 tool 调用**？若是，考虑 DeepAgents 或 LangGraph + 限流。
3. 是否需要**人工审批**某些操作？LangGraph `interrupt` 或 DeepAgents `interrupt_on`。
4. 中间结果是否**大于 4k tokens**？需要文件系统 backend 落盘。

---

*待补充：你的项目选型记录*

| 项目 | 选了什么 | 为什么 | 若重来会改吗 |
|------|----------|--------|--------------|
| p1-weather-agent | | | |
| p3-research-graph | | | |
| p5-deep-research | | | |
