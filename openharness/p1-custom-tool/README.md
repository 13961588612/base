# p1-custom-tool · 公司域只读 Tool + 审计 Hook

W3 专用。在 OpenHarness 扩展机制上实现 **1 个生产可用的只读 Tool** 和 **Pre/PostToolUse 审计原型**。

## 目标

- Pydantic 校验输入
- docstring 明确路由边界（何时用 / 何时不用）
- Hook 写结构化 audit 事件（可先 print / 写文件）

## 建议域 Tool 示例（选一）

| Tool | 说明 |
|------|------|
| `search_internal_docs` | 查公司内部文档索引（mock 或真实 API） |
| `get_service_status` | 查服务健康状态（只读） |
| `lookup_employee_directory` | 查公开通讯录（注意脱敏） |

## 目录建议

```
p1-custom-tool/
├── README.md
├── src/
│   ├── tools/
│   │   └── internal_docs.py
│   └── hooks/
│       └── audit.py
├── tests/
│   └── test_tool_schema.py
└── notes/
    └── tool-design.md           # 费曼：为何不用 Bash 代替
```

## 实现要点

1. Tool 输入 schema 自描述，模型能自动理解
2. 失败返回 `ERROR: ...` 字符串引导模型纠错（与 python-ai 规范一致）
3. Hook 不 log 全量敏感参数

## 验收

- [ ] Tool 在 `oh` 交互会话中被正确选中
- [ ] permission default 模式下行为符合预期
- [ ] Hook 产生可解析的 audit 记录

## 通过后

W4：`../p2-company-skills`
