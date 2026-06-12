# p5-company-agent-ui · 公司 Agent 客户端 MVP

W11–W12 专用。结业作品集。

## 目标

- Dashboard / 业务页 + **CopilotSidebar**
- 公司 Catalog + LangGraph（或 BuiltInAgent）端到端
- `onRequest` 鉴权、E2E 冒烟、部署

## 功能清单

- [ ] 多 Agent：`support` / `ops`（可选）
- [ ] Fixed A2UI 模板用于核心业务流程
- [ ] 流式 Surface 骨架屏
- [ ] Playwright：发消息 + 断言 Surface
- [ ] ADR：`docs/ADR-001-copilotkit-a2ui.md`
- [ ] 部署 URL 或 `docker compose` 说明

## 目录建议

```
p5-company-agent-ui/
├── app/
├── catalog/
├── features/dashboard/
├── e2e/
│   └── assistant.spec.ts
├── docs/
│   ├── ADR-001-copilotkit-a2ui.md
│   └── demo-script.md
└── README.md                   # 30 分钟 onboarding
```

## 与 openharness 关系（文档说明即可）

| 通道 | 技术 |
|------|------|
| Web 业务用户 | 本项目 CopilotKit |
| 飞书/Slack | openharness ohmo（远期统一 LangGraph） |

## 总验收

见 `../LEARNING_PLAN.md` P5 与作品集要求。
