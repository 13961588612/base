# OpenHarness 公司后端 · 最佳实践速查

> 来源：官方文档 + 生产补齐共识。P5 项目每项至少验证一次。

## 1. Profile 即环境边界

```bash
# 开发 / 预发 / 生产用不同 profile，禁止共用一个 API Key
oh provider add company-prod \
  --label "Company Prod GW" \
  --provider openai \
  --api-format openai \
  --base-url https://llm-gateway.company.com/v1 \
  --model company-default
```

- 凭证 **profile-scoped**，不混用 Anthropic/OpenAI key
- CI 用 `--dry-run` 验证 profile ready，不跑真实模型

## 2. 权限：生产永远不用 auto

| 环境 | permission mode | 说明 |
|------|-----------------|------|
| 本地开发 | default | 熟悉权限对话框 |
| 公司 staging | default + 严格 path_rules | 接近生产 |
| 生产 Gateway | default 或 plan | **禁止** `--dangerously-skip-permissions` |

```json
{
  "permission": {
    "mode": "default",
    "path_rules": [
      {"pattern": "/etc/*", "allow": false},
      {"pattern": "~/.ssh/*", "allow": false}
    ],
    "denied_commands": ["rm -rf", "DROP TABLE", "curl | sh"]
  }
}
```

## 3. Tool 暴露最小化

- 生产 Gateway **关闭**或严格限制：Bash、Write、Edit（除非编码 Agent 专用池）
- 内部业务：**MCP 只读** 优先
- docstring 写清 **何时不要用**（与 python-ai Tool 规范一致）

## 4. Skills 即组织知识

```
skills/
├── incident-response/SKILL.md   # 故障处理
├── release-process/SKILL.md     # 发布 checklist
└── security-baseline/SKILL.md   # 安全基线
```

- 公司 Skills 放 **独立 Git 仓库**，版本 tag 发布
- 不可信项目：`oh config set allow_project_skills false`
- 用户可调用 Skill → slash 命令（如 `/incident-response`）

## 5. Hook = 审计主挂载点

```python
# 概念 — 实现见 p1-custom-tool / p5
def post_tool_use(tool_name, args, result, user_id):
    audit_log.emit({
        "user_id": user_id,
        "tool": tool_name,
        "args_summary": redact(args),
        "ok": not result.is_error,
        "ts": now(),
    })
```

- 参数 **摘要 + 脱敏**，不 log 全量 PII
- 写操作 **必须** PostToolUse

## 6. MCP 接入原则

- 优先 **只读** MCP；读写分离不同 server
- dry-run 检查 MCP config，避免上线后 blocked
- 断线：Harness 有 reconnect；业务侧仍要超时
- 与 python-ai RAG：RAG 服务 → MCP `search_docs` tool

## 7. Gateway 与 Harness 分离

- Gateway **无状态**；session 存 Postgres/Redis
- Harness 进程可按会话 spawn 或连接池（按负载选型）
- stream-json 解析层与 IM 适配层分开，便于加 Web 通道

## 8. 长会话与成本

- 启用 Auto-Compaction 策略文档化（何时 compact、保留什么）
- `--max-turns` 必配；子 Agent offload 重检索
- 按 profile 汇总 token / cost（内置计数 + 导出）

## 9. 发布 checklist

```
[ ] oh --dry-run -p "smoke test" → ready
[ ] MCP servers 探活
[ ] Skills tag 与 deploy 版本一致
[ ] settings.json permission 审查
[ ] 审计 log 写入验证
[ ] staging Webhook 冒烟
[ ] 回滚：上一版 Skills + compose image tag
```

## 10. 开源版边界（勿假造已有）

OpenHarness **不自带**：企业 SSO、集中 APM、HA 编排、细粒度 RBAC。  
公司后端必须在 P4–P6 **显式实现**，见 `company-backend-blueprint.md`。

## 11. 与 python-ai 协作

| python-ai 产出 | OpenHarness 用法 |
|----------------|------------------|
| `@tool` 查天气 | 保留为独立服务 → MCP |
| LangGraph HITL 流 | MCP 或 HTTP 子调用 |
| DeepAgents skills | 对照迁移为 SKILL.md |
| p6 FastAPI | 可合并进 Gateway 层或并列 |

## 12. 观测清单（每次长任务后）

- [ ] 是否有未授权 Tool 调用尝试？
- [ ] MCP 超时集中在哪个 server？
- [ ] compaction 后任务是否丢上下文？
- [ ] 哪一步 token 暴增？

---

*踩坑记录：*

| 现象 | 根因 | 修复 |
|------|------|------|
| | | |
