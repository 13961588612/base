# p4-langgraph-client · LangGraph + A2UI 全栈客户端

W9–W10 专用。Runtime 对接 **python-ai LangGraph**；鉴权与错误态。

## 架构

```
Browser → CopilotKitProvider → POST /api/copilotkit
         → LangGraphAgent(deploymentUrl) → python-ai p3-research-graph
         → A2UI messages → Catalog render
```

## Runtime 示例

```typescript
import { LangGraphAgent } from "@copilotkit/runtime/langgraph";

const runtime = new CopilotRuntime({
  agents: {
    default: new LangGraphAgent({
      deploymentUrl: process.env.LANGGRAPH_URL!,
    }),
  },
  a2ui: true,
});

export const POST = createCopilotRuntimeHandler({
  runtime,
  basePath: "/api/copilotkit",
  mode: "single-route",
  hooks: {
    onRequest: ({ request }) => {
      // Bearer JWT 校验
    },
  },
});
```

## 前置

- 本地 LangGraph 服务 **或** mock server 返回固定 A2UI
- 完成 `python-ai` P3 更佳；否则 W9 用 BuiltInAgent + 手写 A2UI 保进度

## 目录建议

```
p4-langgraph-client/
├── app/api/copilotkit/route.ts
├── lib/auth/verifyJwt.ts
├── catalog/                    # 从 p3 复用
└── docs/
    └── langgraph-a2ui-contract.md
```

## 验收

- [ ] 鉴权失败返回 401
- [ ] LangGraph 驱动 ≥1 个 A2UI Surface
- [ ] Agent 离线有降级 UI

## 通过后

W11：`../p5-company-agent-ui`
