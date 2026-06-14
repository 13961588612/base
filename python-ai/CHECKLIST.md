# Python AI Agent · 知识点 Checklist

> 用法：学完打 `[x]`，阶段末对照验收。理论列：心=心理表征 · 费=费曼 · 边=舒适区边缘 · 馈=专注反馈 · 整=整体性学习 · 联=知识关联

---

## P0 · Python 基础 + 现代栈 + LLM（W1–W3）

### W1 · Python 基础（禁止跳过）

- [x] 变量、list/dict、if/for/while — 心
- [x] 函数 def、参数、返回值 — 心
- [x] class + `__init__` + 方法 — 边
- [x] import 与 `if __name__ == "__main__"` — 心
- [x] try/except、读写文件、JSON — 边
- [x] 能**读** `@decorator` 代码（不要求 W1 会写） — 心
- [x] `p0-python-drills` ≥16/20 — 馈
- [x] 命令行 Todo + JSON 持久化 — 边
- [x] 费曼：list vs dict 何时用 — 费

### W2–W3 · 现代栈 + LLM

- [ ] uv 安装、`uv init`、`uv sync`、`uv add`、`uv run` — 馈
- [ ] `pyproject.toml` 与 `uv.lock` 理解 — 心
- [ ] Python 类型标注 + Pydantic v2 模型 — 边
- [ ] `async`/`await` 能读懂（W1 不要求会写） — 心
- [ ] `.env` + `python-dotenv`，密钥不入库 — 馈
- [ ] OpenAI / Anthropic 直连 chat + stream — 馈
- [ ] LangChain `init_chat_model` 多 provider 切换 — 联
- [ ] Message 类型：System / Human / AI / Tool — 心
- [ ] Prompt Template + Few-shot — 心
- [ ] 项目 `p0-cli-chat` 完成 — 边
- [ ] 费曼解释 temperature / max_tokens — 费

---

## P1 · LangChain Agent 核心（W4–W6）

### Tool & Agent 循环

- [ ] `@tool` 装饰器与 docstring 规范 — 心
- [ ] `create_agent` ReAct 循环能白板画出 — 心
- [ ] Tool 返回字符串引导模型纠错 — 馈
- [ ] `recursion_limit` 防止死循环 — 馈
- [ ] Structured Output（Pydantic schema） — 边

### 可观测性

- [ ] LangSmith 项目创建与 trace 查看 — 馈
- [ ] 环境变量 `LANGCHAIN_TRACING_V2` 配置 — 馈

### Middleware

- [ ] Middleware 钩子概念（before/after model） — 心
- [ ] 至少阅读 1 个内置 middleware 源码 — 心

### 项目

- [ ] `p1-weather-agent` — 边
- [ ] `p1-sql-agent` — 边
- [ ] `p1-multi-tool-agent` — 整
- [ ] 费曼：解释 Agent 与普通 chain 的区别 — 费

---

## P2 · RAG + Memory + 评测（W7–W9）

### RAG 管道

- [ ] 文档加载器（PDF / Markdown / Web） — 心
- [ ] 分块策略对比实验（至少 2 种） — 馈
- [ ] Embedding 模型选型记录 — 联
- [ ] Chroma 向量库 CRUD — 边
- [ ] `create_retriever_tool` 接入 Agent — 整
- [ ] Hybrid 检索（BM25 + 向量）概念 — 心

### Memory

- [ ] ConversationBufferMemory — 心
- [ ] Summary / trim 策略 — 边
- [ ] 能说明「何时用 RAG vs 长上下文」 — 费

### 评测

- [ ] Golden set ≥20 题 — 馈
- [ ] 引用来源 / citation 机制 — 馈
- [ ] 项目 `p2-rag-qa` 上线 README — 边

---

## P3 · LangGraph 图编排（W10–W12）⭐

### 图基础

- [ ] `StateGraph` + `TypedDict` state — 心
- [ ] Node / Edge / conditional_edge — 心
- [ ] State reducer（如 `operator.add`） — 心
- [ ] 子图组合 — 整

### 持久化与流

- [ ] Postgres checkpointer（Docker） — 馈
- [ ] `interrupt_before` 人机审批 — 边
- [ ] `stream` / `astream_events` — 馈
- [ ] Checkpoint 恢复与时间旅行 — 馈

### 对比与项目

- [ ] 同任务 Agent vs Graph 对比笔记 — 联
- [ ] 项目 `p3-research-graph` — 边
- [ ] 能画 state 转移图 — 费

---

## P4 · 多 Agent + Middleware（W13–W15）

- [ ] Supervisor 路由模式 — 心
- [ ] 专用子 Agent（researcher / writer / critic） — 整
- [ ] Handoff 上下文移交 — 边
- [ ] 自定义 Middleware（日志/限流/PII） — 边
- [ ] 并行 fan-out / fan-in — 边
- [ ] Trajectory 评测 — 馈
- [ ] Token 成本 per-node 统计 — 馈
- [ ] 项目 `p4-supervisor` — 边

---

## P5 · DeepAgents 深代理（W16–W17）⭐

### 四大支柱

- [ ] 显式规划（planning tool） — 心
- [ ] 子代理 `subagents` 上下文隔离 — 心
- [ ] 虚拟文件系统 `backend` — 心
- [ ] `skills/` 按需加载 — 整

### 进阶能力

- [ ] `create_deep_agent` 参数全览 — 心
- [ ] MCP tool 接入 — 联
- [ ] `interrupt_on` 敏感操作审批 — 馈
- [ ] `stream.subagents` 观测 — 馈
- [ ] 执行上限（recursion + 自定义计数） — 馈
- [ ] System prompt 变更 changelog — 馈

### 项目

- [ ] `p5-deep-research` 跨多步调研任务 — 边
- [ ] 费曼：Shallow vs Deep Agent 四支柱 — 费

---

## P6 · 生产化 + 作品集（W18–W19）

- [ ] FastAPI 包装 Agent + SSE 流式 — 边
- [ ] 限流 / 超时 / 熔断 — 馈
- [ ] Prompt injection 防护意识 — 边
- [ ] Tool 权限白名单 — 馈
- [ ] Docker 化部署 — 馈
- [ ] 项目 `p6-agent-platform` — 边
- [ ] ADR 架构决策记录 ≥1 篇 — 整
- [ ] 作品集 README + LangSmith 截图 — 馈
- [ ] 模拟面试白板通过 — 费

---

## 选型速查（阶段末必会）

- [ ] 何时用 LangChain `create_agent` — 费
- [ ] 何时用 LangGraph `StateGraph` — 费
- [ ] 何时用 DeepAgents `create_deep_agent` — 费