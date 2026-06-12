# p3-mcp-integration · 内部系统 MCP 接入

W5–W6 专用。将 **只读** 内部能力通过 MCP 暴露给 OpenHarness。

## 目标

- 1 个 MCP Server（stdio 或 HTTP）
- `oh mcp` 配置 + dry-run 验证
- 生产向：超时、只读、参数校验

## 推荐场景

| MCP Server | Tools 示例 |
|------------|------------|
| 工单系统 | `search_tickets`, `get_ticket` |
| 知识库 | `search_docs`（可对接 python-ai RAG） |
| 数据只读 | `run_readonly_query`（禁止 DDL/DML） |

## 目录建议

```
p3-mcp-integration/
├── README.md
├── mcp-server/
│   ├── pyproject.toml
│   ├── src/
│   │   └── server.py
│   └── README.md
├── config/
│   └── servers.json.example
└── notes/
    └── mcp-security.md
```

## 配置示例

```json
{
  "mcpServers": {
    "company-tickets": {
      "command": "uv",
      "args": ["run", "python", "-m", "mcp_server"],
      "env": {
        "TICKET_API_URL": "https://internal.example/api"
      }
    }
  }
}
```

## 安全基线

- 默认 **只读** Tool
- API Key 走环境变量，不入库
- 见 `../notes/openharness-best-practices.md` §6

## 验收

- [ ] Harness 会话中可调用 MCP Tool
- [ ] `--dry-run` 能发现 MCP 配置错误
- [ ] 文档记录权限级别与负责人

## 通过后

W7：`../p3-multi-agent-lab`
