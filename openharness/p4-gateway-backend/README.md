# p4-gateway-backend · Gateway 与程序化 API

W9–W10 专用。从 CLI/TUI 升级到 **可对接业务系统的 Gateway**。

## 两条路径（至少完成一条）

### A. ohmo 通道（IM 优先）

```bash
ohmo init
ohmo config          # 配置飞书/Slack 等
ohmo gateway start
```

### B. 自研 HTTP Gateway（API 优先）

基于 `stream-json` 封装 REST/SSE，供内部 Web / Webhook 调用。

## 目录建议

```
p4-gateway-backend/
├── README.md
├── gateway/
│   ├── app.py              # FastAPI 入口
│   ├── harness_client.py   # 调用 oh -p --output-format stream-json
│   ├── channels/
│   │   └── webhook.py
│   └── session.py          # session_id 映射
├── contracts/
│   └── openapi.yaml        # 内部 API 契约
└── tests/
    └── test_webhook_smoke.py
```

## API 契约（示例）

```
POST /v1/chat
  Headers: Authorization: Bearer <GATEWAY_API_KEY>
  Body: { "session_id": "...", "user_id": "...", "message": "..." }
  Response: SSE stream
```

## 路由规则

| 输入 | 映射 |
|------|------|
| user_id / 部门 | provider profile |
| channel 类型 | system prompt 增量 |
| session_id | Harness resume |

## 验收

- [ ] 非 TUI 客户端完成一轮对话
- [ ] Gateway 重启后会话可 resume
- [ ] stream-json 事件正确解析为 SSE

## 通过后

W11：`../p5-company-agent-platform`
