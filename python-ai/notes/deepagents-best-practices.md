# DeepAgents 最佳实践速查

> 来源：官方文档 + 生产实践共识。每项需在 `p5-deep-research` 中至少验证一次。

## 1. 先简后繁

```python
# ✅ 第一步：单 tool 验证
agent = create_deep_agent(model="...", tools=[search_tool])

# ✅ 稳定后：加 subagents
agent = create_deep_agent(..., subagents=[researcher, writer])

# ✅ 最后：filesystem + skills + MCP
agent = create_deep_agent(..., backend=..., skills=["./skills"], ...)
```

## 2. Tool docstring 即契约

模型靠描述选 tool，不靠你的路由代码。

```python
@tool
def search_papers(query: str, max_results: int = 5) -> str:
    """Search academic papers by keyword.

    Use when the user asks for research citations or literature review.
    Do NOT use for general web news — use search_web instead.

    Args:
        query: English search keywords, 3-8 words.
        max_results: Number of papers to return (1-10).

    Returns:
        JSON string with fields: title, authors, abstract, url.
        On failure returns "ERROR: <reason>" — retry with simpler query.
    """
```

## 3. 子代理做「重活」

| 主代理保留 |  offload 给子代理 |
|------------|-------------------|
| 用户对话、计划、综合 | 大范围网页检索 |
| 最终答案撰写 | 长文草稿生成 |
| 任务分派 | 多文件代码修改 |

## 4. 文件系统防 context 膨胀

- 检索原始 HTML / PDF 全文 → 写 `/workspace/raw/`
- 主代理只读 `/workspace/summary.md`
- 用 `permissions` 限制敏感路径

## 5. 执行上限（必配）

```python
config = {"recursion_limit": 50}

# 自定义 state 计数（LangGraph 层）
# 在 middleware 中统计 tool_calls，超过 N 次强制结束
```

## 6. System prompt 当代码管

- 不要复制默认 prompt 全文；用 `system_prompt=` **增量补充**领域规则
- 变更记录到 `notes/prompt-changelog.md`
- 改一句可能导致：不再规划 / 乱调 tool / 过度写文件

## 7. 观测清单（LangSmith）

每次长任务跑完检查：

- [ ] 是否先写计划再调 tool？
- [ ] 子代理 handoff 时机是否合理？
- [ ] 是否有重复读同一文件？
- [ ] 哪一步 token 暴增？

## 8. MCP 接入原则

- 优先 MCP 连接**稳定、只读**的数据源
- 写操作一律 `interrupt_on` 人工审批
- 本地开发可用 `mcp-server-filesystem` 练手

## 9. Skills 目录约定

```
skills/
├── company-style/
│   └── SKILL.md      # 写作风格、术语表
├── codebase/
│   └── SKILL.md      # 仓库结构、约定
└── domain/
    └── SKILL.md      # 行业知识
```

Agent 按需加载，避免全部塞进 system prompt。

## 10. 何时**不要**用 DeepAgents

- 单步分类 / 提取 → Structured Output 即可
- 严格固定流程（如审批链 5 步）→ 纯 LangGraph 更清晰
- 延迟敏感 &lt;3s 的问答 → RAG + `create_agent`

---

*实践记录区（学习时填写）*

| 日期 | 尝试 | 结果 | 教训 |
|------|------|------|------|
| | | | |
