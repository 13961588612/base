# Python AI Agent 开发学习计划

> **你的画像（v1.1 · 已锁定）**
>
> | 项 | 值 |
> |----|-----|
> | Python | **1/5**（仅了解一点点；P0 含 1 周基础速成，**禁止跳过**） |
> | LLM 经验 | 0–2/5（用过 ChatGPT API 或 Copilot，未系统做过 Agent） |
> | 每周投入 | 25h |
> | 目标 | 能独立设计、开发、观测、部署 **生产级 AI Agent** |
> | 周期 | **19 周**（因 Python 基础 +1 周；Agent 主线不砍） |
> | 包管理 | **uv**（见仓库根 `README.md`） |
> | 模型 | OpenAI / Anthropic / 本地 Ollama 均可；计划以可切换 provider 为准 |
> | 观测 | LangSmith（从 P1 起贯穿） |
>
> **终极目标**：能选型 **LangChain → LangGraph → DeepAgents** 技术栈，交付可维护的多步 Agent 系统（含 RAG、工具、子代理、人机协同、持久化与评测）。

---

## 一、技术栈分层（必读）

LangChain 生态是**三层递进**，不是三选一：

```
┌─────────────────────────────────────────────────────────┐
│  DeepAgents  — 开箱即用的「深代理」脚手架                │
│  规划 · 子代理 · 虚拟文件系统 · Skills · MCP · HITL     │
├─────────────────────────────────────────────────────────┤
│  LangGraph   — 图运行时：状态机、持久化、流式、中断恢复   │
├─────────────────────────────────────────────────────────┤
│  LangChain   — 模型抽象、Prompt、Tool、Middleware、RAG  │
└─────────────────────────────────────────────────────────┘
```

| 场景 | 推荐层 | 理由 |
|------|--------|------|
| 单轮/少轮工具调用、轻量聊天 | LangChain `create_agent` | 最少样板代码 |
| 固定流程、分支、循环、需 checkpoint | LangGraph `StateGraph` | 图即文档，可控性强 |
| 多步研究、编码、长时任务、上下文膨胀 | DeepAgents `create_deep_agent` | 内置规划+子代理+文件系统 |

详见 `notes/agent-decision-tree.md`。

---

## 二、学习内容总览（6 阶段 · 19 周）

| 阶段 | 主题 | 核心产出 | 周期 |
|------|------|----------|------|
| P0 | **Python 基础** + 现代栈 + LLM | 基础练习 + uv 项目 + 流式 CLI | **3 周** |
| P1 | LangChain 核心 | 3 个 Tool Agent 小项目 | 3 周 |
| P2 | RAG + Memory + 结构化输出 | 文档问答 Agent（带评测） | 3 周 |
| **P3** | **LangGraph 图编排** | **带 HITL 的研究工作流** | **3 周** |
| P4 | 多 Agent + Middleware | Supervisor 协作 + 自定义中间件 | 3 周 |
| **P5** | **DeepAgents 深代理** | **代码/研究深代理 MVP** | **2 周** |
| P6 | 生产化 + 作品集 | FastAPI 服务 + 评测 + 部署 | 2 周 |

### 实践项目路线图

| 周次 | 项目 | 技术点 |
|------|------|--------|
| W1 | `p0-python-drills` | 语法、函数、类、模块、异常、文件 I/O |
| W2–W3 | `p0-cli-chat` | uv、类型/Pydantic、dotenv、流式、provider |
| W4 | `p1-weather-agent` | `@tool`、ReAct 循环、`create_agent` |
| W5 | `p1-sql-agent` | 结构化 tool 参数、错误重试 |
| W6 | `p1-multi-tool-agent` | 多工具路由、LangSmith trace |
| W7–W9 | `p2-rag-qa` | 分块、Embedding、向量库、Hybrid 检索 |
| W10–W12 | `p3-research-graph` | StateGraph、checkpoint、interrupt、stream |
| W13–W15 | `p4-supervisor` | 子图、handoff、自定义 Middleware |
| W16–W17 | `p5-deep-research` | `create_deep_agent`、subagents、skills、MCP |
| W18–W19 | `p6-agent-platform` | FastAPI + 前端/CLI + 评测 + 部署 |

---

## 三、分阶段详细内容

### P0 · Python 基础 + 现代栈 + LLM（W1–W3）

**学习目标**：Python 1/5 → 能独立读改 Agent 代码；掌握 uv 与 LLM 调用。

> W1 **只学 Python，不碰 LLM**。详见 `notes/python-basics-bridge.md`。

#### W1 · Python 基础速成（纯语法，零框架）

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 0.0 | 安装 Python 3.12+；用 `python` / `pip` 跑通第一个脚本 | 馈 | 2h |
| 0.1 | 变量、类型、`list`/`dict`/`set`、切片、推导式 | 心 | 5h |
| 0.2 | `if`/`for`/`while`、`def` 函数、`*args`/`**kwargs` | 心 | 5h |
| 0.3 | `class`、实例方法、`__init__`、继承初识 | 边 | 4h |
| 0.4 | 模块 `import`、`if __name__ == "__main__"` | 心 | 3h |
| 0.5 | 异常 `try/except`、读写文件、`with`、pathlib 初识 | 边 | 4h |
| 0.6 | **练习 `p0-python-drills`**：20 道小题 + 1 个命令行 Todo | 边 | 8h |
| 0.7 | 费曼：向自己解释「list vs dict 何时用」 | 费 | 2h |

**W1 验收**：
- [ ] 能不看答案完成 drills 中 ≥16/20 题
- [ ] Todo 脚本：增删列、持久化到 JSON 文件
- [ ] 能说出 `import` 与相对路径的区别

#### W2–W3 · 现代工具链 + LLM CLI

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 0.8 | 安装 uv、`uv init`、理解 `pyproject.toml` | 馈 | 3h |
| 0.9 | 类型标注、dataclass/Pydantic、pathlib 实战 | 边 | 6h |
| 0.10 | `async`/`await` 概念（先读懂，P3 前再写） | 心 | 3h |
| 0.11 | OpenAI / Anthropic SDK：chat、stream、token 计数 | 馈 | 6h |
| 0.12 | LangChain `init_chat_model` 统一多 provider | 联 | 4h |
| 0.13 | Prompt 模板、Message 类型、Few-shot | 心 | 4h |
| 0.14 | **项目 `p0-cli-chat`**：多轮 CLI + 流式 + `/reset` | 边 | 14h |
| 0.15 | 环境变量、`.env.example`、密钥不入库 | 馈 | 2h |
| 0.16 | 费曼：解释「temperature / max_tokens」 | 费 | 2h |

**P0 总验收**：
- [ ] `uv sync` 一键复现环境
- [ ] 能切换 2 个 model provider 而不改业务代码
- [ ] CLI 支持流式输出与对话历史
- [ ] 读得懂 `def` + `class` + `@decorator` 的 Agent 示例代码

---

### P1 · LangChain Agent 核心（W4–W6）

**学习目标**：掌握 Tool Calling、Agent 循环、Middleware 初探；LangSmith 可观测性。

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 1.1 | `@tool` 装饰器、docstring 即路由依据 | 心 | 3h |
| 1.2 | `create_agent` + `bind_tools` 理解 ReAct 循环 | 心 | 5h |
| 1.3 | LangSmith：project、trace、run 分析 | 馈 | 4h |
| 1.4 | **项目1** 天气/搜索 Agent（1–2 个 tool） | 边 | 10h |
| 1.5 | Tool 错误处理：返回字符串 vs raise；模型自我纠错 | 馈 | 4h |
| 1.6 | **项目2** 自然语言查 SQLite（text-to-SQL 轻量版） | 边 | 12h |
| 1.7 | Structured Output：`response_format` / Pydantic schema | 边 | 5h |
| 1.8 | Middleware 概念：before_model / after_model 钩子 | 心 | 4h |
| 1.9 | **项目3** 多工具个人助理（日历 mock + 计算 + 搜索） | 整 | 15h |
| 1.10 | `recursion_limit` 防无限循环；最大 tool 调用计数 | 馈 | 3h |

**最佳实践（P1 起强制执行）**：
1. 每个 tool 写清 docstring（参数语义、返回格式、失败时行为）
2. 每个 Agent 项目配置 LangSmith + README 运行说明
3. 从 1 个 tool 开始，稳定后再加工具

**验收**：
- [ ] 能白板画出 Agent 循环：User → Model → Tool → Model → Answer
- [ ] LangSmith 中能看到完整 tool call 链
- [ ] 3 个小项目均可 `uv run` 启动

---

### P2 · RAG + Memory + 评测（W7–W9）

**学习目标**：构建可评测的文档问答 Agent；理解上下文窗口与记忆策略。

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 2.1 | 文档加载、分块策略（fixed / recursive / semantic） | 心 | 5h |
| 2.2 | Embedding 模型选型；本地 vs API | 联 | 4h |
| 2.3 | 向量库：Chroma 本地；了解 pgvector | 边 | 6h |
| 2.4 | Retriever + `create_retriever_tool` 接入 Agent | 整 | 5h |
| 2.5 | Hybrid 检索（BM25 + 向量）概念与最小实现 | 边 | 6h |
| 2.6 | Conversation Memory：buffer / summary / trim | 心 | 5h |
| 2.7 | **项目 `p2-rag-qa`**：对公司手册/开源 README 集合问答 | 边 | 20h |
| 2.8 | RAG 评测：固定 20 题 golden set + 人工打分 | 馈 | 6h |
| 2.9 | 幻觉防护：引用来源、citation in answer | 馈 | 4h |
| 2.10 | 费曼：解释「为何 RAG 不能替代微调」 | 费 | 2h |

**验收**：
- [ ] Golden set 准确率基线可复现
- [ ] 回答带可追溯引用
- [ ] 能说明何时用 RAG vs 长上下文 vs 微调

---

### P3 · LangGraph 图编排（W10–W12）⭐

**学习目标**：用图表达非线性工作流；checkpoint、人机协同、流式。

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 3.1 | `StateGraph`、`TypedDict` state、reducer | 心 | 5h |
| 3.2 | Node / Edge / conditional_edge / END | 心 | 5h |
| 3.3 | `compile(checkpointer=...)` + Postgres checkpoint | 馈 | 6h |
| 3.4 | `interrupt_before` / `interrupt_after` 人机审批 | 边 | 6h |
| 3.5 | `stream` / `astream_events` 事件流 | 馈 | 4h |
| 3.6 | 子图 `add_node(subgraph)` 模块化 | 整 | 5h |
| 3.7 | **项目 `p3-research-graph`**：搜索→摘要→人工批准→写报告 | 边 | 25h |
| 3.8 | 时间旅行调试：从 checkpoint 恢复并重放 | 馈 | 4h |
| 3.9 | 对比实验：同一任务 LangChain Agent vs LangGraph 版图 | 联 | 5h |

**验收**：
- [ ] 能画出 research 项目的 state 转移图
- [ ] 中断后人工编辑 state 再继续执行
- [ ] Docker Postgres checkpoint 重启不丢会话

---

### P4 · 多 Agent + Middleware（W13–W15）

**学习目标**：Supervisor 模式、handoff、可组合 Middleware。

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 4.1 | Supervisor 架构：路由 vs 全员参与 | 心 | 4h |
| 4.2 | 专用子 Agent：researcher / writer / critic | 整 | 6h |
| 4.3 | Handoff tool：显式移交上下文 | 边 | 5h |
| 4.4 | 自定义 Middleware：日志、限流、PII 过滤 | 边 | 8h |
| 4.5 | 并行 fan-out / fan-in 模式 | 边 | 5h |
| 4.6 | **项目 `p4-supervisor`**：内容生产流水线（调研→撰写→审稿） | 边 | 22h |
| 4.7 | Agent 评测：trajectory 评分、结果评分 | 馈 | 6h |
| 4.8 | 成本追踪：token 用量 per-node 统计 | 馈 | 4h |

**验收**：
- [ ] Supervisor 能正确路由到子 Agent
- [ ] 至少 1 个自写 Middleware 接入生产路径
- [ ] 有 trajectory 评测报告

---

### P5 · DeepAgents 深代理（W16–W17）⭐

**学习目标**：掌握 `create_deep_agent` 四大支柱——规划、子代理、文件系统、Skills。

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 5.1 | DeepAgents vs `create_agent` vs 裸 LangGraph 选型 | 心 | 3h |
| 5.2 | `create_deep_agent` 最小示例：1 tool + system_prompt | 馈 | 4h |
| 5.3 | 规划工具：任务分解、可检查的计划 artifact | 心 | 4h |
| 5.4 | `subagents` 参数：上下文隔离、专项子代理 | 边 | 6h |
| 5.5 | 虚拟文件系统：`backend`、权限、大结果落盘 | 边 | 6h |
| 5.6 | `skills/` 目录：按需加载领域知识 | 整 | 4h |
| 5.7 | MCP 接入：连接外部数据库/API | 联 | 6h |
| 5.8 | `interrupt_on` 敏感 tool 人工审批 | 馈 | 4h |
| 5.9 | **项目 `p5-deep-research`**：多源调研 + 报告生成 + 文件持久化 | 边 | 20h |
| 5.10 | `stream.subagents` 观测子代理进度 | 馈 | 3h |

**DeepAgents 最佳实践清单**：
1. **先简后繁**：1 tool → 加 planning → 加 subagent → 加 filesystem
2. **Tool docstring 即 API 契约**：路由逻辑靠描述，不靠 if-else
3. **子代理做重活**：检索、爬虫、长文生成 offload 到子代理
4. **文件系统防 context 膨胀**：中间结果写文件，主代理读摘要
5. **执行上限**：`recursion_limit` + 自定义 tool 调用计数
6. **System prompt 当代码管**：变更需 review，保留 changelog
7. **LangSmith 全链路 trace**：规划步、子代理 handoff 必查

**验收**：
- [ ] 深代理能完成 ≥30min 跨多步任务（调研类）
- [ ] 子代理上下文与主代理隔离可验证
- [ ] 重启后会话/文件状态可恢复

---

### P6 · 生产化 + 作品集（W18–W19）

**学习目标**：API 化、部署、安全、完整作品集。

| 序号 | 学习动作 | 理论标注 | 时长 |
|------|----------|----------|------|
| 6.1 | FastAPI 包装 Agent：session、SSE 流式 | 边 | 8h |
| 6.2 | 限流、超时、熔断；队列化长任务 | 馈 | 5h |
| 6.3 | 安全：prompt injection 防护、tool 权限白名单 | 边 | 5h |
| 6.4 | Docker 化 Agent 服务 + compose 联调 | 馈 | 6h |
| 6.5 | **项目 `p6-agent-platform`**：统一入口 + 多 Agent 路由 | 边 | 20h |
| 6.6 | 文档：ADR（为何选 DeepAgents / LangGraph） | 整 | 4h |
| 6.7 | 模拟面试：白板架构 + 现场改 tool | 费 | 4h |
| 6.8 | 博客/笔记：一篇「从 Shallow 到 Deep Agent」 | 费 | 3h |

**作品集最低要求**：
- 1 个 LangGraph 工作流（含 HITL）
- 1 个 DeepAgents 深代理
- 1 个 RAG 问答（含评测数据）
- 全部有 LangSmith 截图 + README

---

## 四、19 周时间轴

```
周      阶段    主题                              25h
──────────────────────────────────────────────────────────
W1      P0      Python 基础速成（不碰 LLM）        25h
W2–W3   P0      uv 现代栈 + LLM CLI               50h
W4–W6   P1      LangChain Agent 三角项目          75h
W7–W9   P2      RAG + Memory + 评测               75h
W10–W12 P3      LangGraph 研究工作流 ⭐            75h
W13–W15 P4      多 Agent + Middleware             75h
W16–W17 P5      DeepAgents 深代理 ⭐               50h
W18–W19 P6      生产化 + 作品集                   50h
```

**25h 分配建议（每周）**：核心学习 ~18h · 项目实战 ~5h · 反馈复盘 ~1.5h · 跨域整合 ~0.5h

---

## 五、反馈与调整机制

| 场景 | 调整 |
|------|------|
| W1 drills 正确率 &lt;60% | **禁止进入 W2**；重复 W1 直至 ≥16/20；减少 LLM 相关内容 |
| 看不懂装饰器 / import 报错 | 回退 `notes/python-basics-bridge.md` 第 4–5 节；用 2h 重写最小 `@tool` |
| Agent 无限循环调 tool | 立即加 `recursion_limit=10`，检查 tool 返回值是否误导模型 |
| RAG 回答胡编 | 暂停加功能，先修分块与 citation；golden set 回归 |
| LangGraph state 混乱 | 画 state 图；为每个 field 写清 reducer 语义 |
| DeepAgent 上下文爆炸 | 启用文件系统 backend，子代理 offload |
| 项目超时 | 砍 scope：先 1 tool + 1 条 happy path，再迭代 |
| API 费用过高 | 换小模型做 routing，大模型仅用于最终生成 |

**每周五晚 Weekly Review（1.5h）**：
1. 本周 CHECKLIST 完成率
2. LangSmith 挑 1 条失败 trace 根因分析
3. 下周唯一重点（只能有 1 个）

---

## 六、跨知识整合

| 整合 | 做法 | 理论 |
|------|------|------|
| React 全栈 ↔ Agent API | 用 Next.js 给 P6 做聊天 UI | 知识关联 |
| SQL ↔ text-to-SQL Agent | 复用 reactjs 的 PostgreSQL 知识 | 知识关联 |
| CRUD API ↔ Tool 设计 | 每个 REST 端点映射为一个 tool | 整体性学习 |
| 状态机 ↔ LangGraph | 画 UML 状态图与 StateGraph 对照 | 心理表征 |
| Shallow ↔ Deep Agent | 同一任务做两版，列能力差距表 | 专注反馈 |

---

## 七、推荐资源

| 类型 | 资源 |
|------|------|
| Python 入门 | [Python 官方教程](https://docs.python.org/3/tutorial/)（W1 主线） |
| Python 练习 | `notes/python-basics-bridge.md` + `p0-python-drills` |
| LangChain | [docs.langchain.com/oss/python](https://docs.langchain.com/oss/python) |
| LangGraph | [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) |
| DeepAgents | [Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview) |
| 定制 | [Customize Deep Agents](https://docs.langchain.com/oss/python/deepagents/customization) |
| 观测 | [LangSmith 文档](https://docs.smith.langchain.com/) |
| MCP | [Model Context Protocol](https://modelcontextprotocol.io/) |
| 源码 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) |
| 本地模型 | [Ollama](https://ollama.com/) + LangChain Ollama 集成 |
| 向量库 | Chroma 文档；pgvector + PostgreSQL |

---

## 八、文件索引

**包管理**：本领域所有 Python 子项目使用 **uv**（见仓库根 `README.md`）。

```
python-ai/
├── LEARNING_PLAN.md          ← 本文件 v1.1
├── CHECKLIST.md              ← 知识点勾选
├── WEEKLY_SCHEDULE.md        ← 逐周执行表
├── docker-compose.yml        ← Postgres（LangGraph checkpoint / pgvector）
├── .env.example              ← API Key 模板（勿提交真实密钥）
├── notes/
│   ├── python-basics-bridge.md
│   ├── agent-decision-tree.md
│   ├── langchain-ecosystem-map.md
│   └── deepagents-best-practices.md
├── p0-python-drills/         ← W1
├── p0-cli-chat/              ← W2–W3
├── p1-weather-agent/         ← W4
├── p1-sql-agent/             ← W5
├── p1-multi-tool-agent/      ← W6
├── p2-rag-qa/                ← W7–W9
├── p3-research-graph/        ← W10–W12
├── p4-supervisor/            ← W13–W15
├── p5-deep-research/         ← W16–W17
└── p6-agent-platform/        ← W18–W19
```

---

*v1.1 · Python=1 · LLM 初学 · 25h/周 · LangChain/LangGraph/DeepAgents · 19周*
