# p5-company-agent-platform · 公司统一 Agent 后端 MVP

W11–W12 专用。**整合 P1–P4 产出**为可 onboarding 的公司后端。

## 目标架构

见 `../notes/company-backend-blueprint.md`。

## 目录（与蓝图一致）

```
p5-company-agent-platform/
├── README.md
├── config/
│   ├── profiles/
│   ├── settings.json
│   └── mcp/
├── skills/                 #  symlink 或 submodule p2-company-skills
├── plugins/
├── gateway/                #  symlink 或 merge p4-gateway-backend
├── audit/
│   └── schema.json
└── docs/
    ├── ADR-001-harness-layer.md
    └── onboarding.md       # 30 分钟跑通
```

## MVP 功能清单

- [ ] 统一配置：profiles + permission 基线 + MCP 清单
- [ ] 鉴权：API Key 或 JWT（mock IdP 可接受）
- [ ] 审计：PostToolUse → JSON log（文件或 Postgres）
- [ ] 观测：LangSmith 或最小 metrics 端点
- [ ] Webhook 通道冒烟通过
- [ ] `oh --dry-run` 纳入 CI 检查（文档描述即可）

## 启动（目标形态）

```bash
cp ../.env.example .env
docker compose -f ../docker-compose.yml up -d
# 按 README 启动 gateway + harness
```

## 验收

- [ ] 新同事按 `docs/onboarding.md` ≤30min 跑通
- [ ] 审计 log 可追踪一次完整 tool 链
- [ ] ADR 说明为何选 OpenHarness

## 通过后

W13：`../p6-deploy-ops`
