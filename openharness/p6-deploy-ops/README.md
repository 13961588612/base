# p6-deploy-ops · 生产部署与运维

W13–W14 专用。容器化、健康检查、发布回滚、运行手册。

## 交付物

```
p6-deploy-ops/
├── README.md
├── deploy/
│   ├── Dockerfile
│   ├── docker-compose.prod.yml
│   └── k8s/                    # 可选
├── scripts/
│   ├── healthcheck.sh
│   └── preflight-dry-run.sh
└── docs/
    ├── runbook.md              # 故障树
    └── release-checklist.md
```

## Dockerfile 要点

- 多阶段构建；镜像内 **无** API Key
- 非 root 用户运行 Gateway
- 健康检查：`/health` + MCP 探活脚本

## 发布 checklist

见 `../notes/openharness-best-practices.md` §9。

## runbook 必含

| 故障 | 排查 | 缓解 |
|------|------|------|
| profile blocked | `oh --dry-run` | 修 auth / base_url |
| MCP 超时 | server 日志 | 降级只读 / 缓存 |
| Gateway OOM | session 数 | 限流 + TTL |
| compaction 丢上下文 | memory 策略 | 调整 prompt / 手动 resume |

## 总验收（14 周结业）

- [ ] compose 一键启动 staging
- [ ] release-checklist 完整
- [ ] 模拟 Security + SRE 问答通过
- [ ] 作品集 README + 架构图
