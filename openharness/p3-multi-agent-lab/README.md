# p3-multi-agent-lab · 子 Agent 与长会话

W7–W8 专用。验证 coordinator、Task、Memory 在公司复杂场景下的用法。

## 场景

**调研 + 汇总**：主 Agent 接收用户问题 → spawn 调研子 Agent（MCP 查资料）→ 主 Agent 综合回答。

## 实验项

| # | 内容 | 验收 |
|---|------|------|
| 1 | 子 Agent spawn + SendMessage | 上下文隔离可观察 |
| 2 | 后台 Task 长任务 | TaskOutput 可 retrieve |
| 3 | MEMORY.md 跨会话 | 重启后关键事实仍在 |
| 4 | Auto-Compaction | 长对话后任务不丢 |
| 5 | `--max-turns` 熔断 | 死循环被截断 |

## 目录

```
p3-multi-agent-lab/
├── README.md
├── scenarios/
│   └── research-and-synthesize.md
└── notes/
    └── coordinator-vs-langgraph.md
```

## 与 LangGraph 分工

复杂 **固定审批流** 不下沉到 coordinator 硬写；应 LangGraph + MCP。  
见 `../notes/harness-vs-langchain-map.md`。

## 验收

见 `../LEARNING_PLAN.md` P3。

## 通过后

W9：`../p4-gateway-backend`
