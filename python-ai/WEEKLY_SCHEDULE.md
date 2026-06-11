# 19 周逐周执行表（25h/周）

> **Python 1/5**：W1 只做语法与 drills，**不碰 LLM / LangChain**。

> **每日默认节奏**：晨间 2h 理论+笔记 · 午后 3h 编码 · 晚间 2h 项目/缓冲（可调）  
> **周五晚**：Weekly Review 1.5h（见 LEARNING_PLAN 反馈机制）  
> 理论标注：心=心理表征 · 费=费曼 · 边=舒适区边缘 · 馈=专注反馈 · 整=整体性 · 联=知识关联

---

## W1 · P0  Python 基础速成（零 LLM）

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 安装 Python 3.12；官方教程 §1–3；变量/list/dict | 5 | 心 |
| 二 | if/for/函数；drills 01–08 | 5 | 心 |
| 三 | class + import；drills 09–15 | 5 | 边 |
| 四 | 异常 + 文件 JSON；drills 16–20 | 5 | 边 |
| 五 | Todo 项目：add/list | 5 | 馈 |
| 六 | Todo：done/save + drills 验收 ≥16/20 | 4 | 费 |
| 日 | 费曼笔记 + Weekly Review | 1.5 | 费 |

---

## W2 · P0  uv + 现代 Python

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 安装 uv；`uv init p0-cli-chat`；pyproject 阅读 | 5 | 馈 |
| 二 | 类型标注、Pydantic、pathlib 练习 | 5 | 边 |
| 三 | OpenAI SDK 直连：非流式对话 | 5 | 馈 |
| 四 | 流式输出 + token 计数 | 5 | 心 |
| 五 | LangChain `init_chat_model` 双 provider | 4 | 联 |
| 六 | Message 类型 + Prompt Template | 4 | 心 |
| 日 | 周复盘 | 1.5 | 馈 |

---

## W3 · P0  CLI 对话项目

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | CLI 框架（typer/rich）；多轮历史 | 5 | 边 |
| 二 | `/reset` `/model` 命令；配置加载 | 5 | 馈 |
| 三 | 流式渲染；错误重试 | 5 | 馈 |
| 四 | `.env.example`；README 运行文档 | 4 | 馈 |
| 五 | 费曼文章：temperature / max_tokens | 3 | 费 |
| 六 | P0 总验收；代码整理 push | 4 | 费 |
| 日 | Weekly Review | 1.5 | 馈 |

---

## W4 · P1  Tool 与 Agent 入门

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `@tool` 规范；docstring 实验 | 5 | 心 |
| 二 | `create_agent` 最小 loop | 5 | 心 |
| 三 | LangSmith 接入与第一次 trace | 4 | 馈 |
| 四 | `p1-weather-agent` 骨架 | 5 | 边 |
| 五 | weather 项目完善 + 评测 | 4 | 馈 |
| 六 | `recursion_limit` 实验 | 3 | 馈 |
| 日 | Review | 1.5 | 馈 |

---

## W5 · P1  SQL Agent

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | SQLite 样例库准备 | 4 | 联 |
| 二 | text-to-SQL tool 设计 | 5 | 边 |
| 三 | 错误 SQL 自我纠错 | 5 | 馈 |
| 四 | Structured Output 表格化结果 | 5 | 边 |
| 五 | `p1-sql-agent` 联调 | 4 | 馈 |
| 六 | 写一篇 tool docstring 最佳实践 | 3 | 心 |
| 日 | Review | 1.5 | 馈 |

---

## W6 · P1  多工具助理 + Middleware 入门

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 多 tool 路由实验 | 5 | 心 |
| 二 | `p1-multi-tool-agent` 核心 | 5 | 边 |
| 三 | 继续 multi-tool；边界 case | 5 | 馈 |
| 四 | Middleware 阅读 + 最小自定义 | 5 | 心 |
| 五 | P1 三项目 README + demo 录屏 | 4 | 费 |
| 六 | P1 验收 | 3 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W7 · P2  RAG 基础

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 文档加载 + 清洗 | 5 | 心 |
| 二 | 分块策略 A/B 实验 | 5 | 馈 |
| 三 | Embedding + Chroma 入库 | 5 | 边 |
| 四 | Retriever 调参 top-k | 4 | 馈 |
| 五 | `create_retriever_tool` | 4 | 整 |
| 六 | 检索质量人工评估 10 题 | 3 | 馈 |
| 日 | Review | 1.5 | 馈 |

---

## W8 · P2  RAG Agent 组装

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | Agent + RAG 串联 | 5 | 整 |
| 二 | Citation 引用机制 | 5 | 馈 |
| 三 | Hybrid 检索调研/最小实现 | 5 | 边 |
| 四 | Conversation Memory 策略 | 4 | 心 |
| 五 | `p2-rag-qa` 功能闭环 | 4 | 边 |
| 六 | 幻觉 case 分析与修复 | 3 | 馈 |
| 日 | Review | 1.5 | 馈 |

---

## W9 · P2  评测与 P2 验收

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | Golden set 20 题编写 | 5 | 馈 |
| 二 | 批量评测脚本 | 5 | 馈 |
| 三 | 准确率基线 + 改进一轮 | 5 | 馈 |
| 四 | 费曼：RAG vs 微调 vs 长上下文 | 3 | 费 |
| 五 | README + 可复现文档 | 4 | 馈 |
| 六 | P2 验收 | 4 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W10 · P3  LangGraph 基础

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `StateGraph` 最小图 | 5 | 心 |
| 二 | conditional_edge 分支 | 5 | 心 |
| 三 | State reducer 实验 | 4 | 心 |
| 四 | Docker Postgres 起 checkpoint | 5 | 馈 |
| 五 | `compile(checkpointer=...)` | 4 | 馈 |
| 六 | 子图概念阅读 + 草图 | 3 | 整 |
| 日 | Review | 1.5 | 馈 |

---

## W11 · P3  HITL 研究流

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `p3-research-graph` 骨架：搜索节点 | 5 | 边 |
| 二 | 摘要节点 + 条件边 | 5 | 边 |
| 三 | `interrupt_before` 人工审批 | 5 | 边 |
| 四 | 写报告节点 + END | 5 | 馈 |
| 五 | stream 事件消费 | 4 | 馈 |
| 六 | checkpoint 恢复测试 | 3 | 馈 |
| 日 | Review | 1.5 | 馈 |

---

## W12 · P3  对比实验与验收

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 同任务 Agent 版实现 | 5 | 联 |
| 二 | 对比报告：可控性/可观测/代码量 | 4 | 联 |
| 三 | 时间旅行调试练习 | 4 | 馈 |
| 四 | state 转移图绘制 | 3 | 费 |
| 五 | 项目打磨 + 文档 | 5 | 馈 |
| 六 | P3 验收 | 5 | 费 |
| 日 | Review | 1.5 | 馈 |

---

## W13 · P4  Supervisor 模式

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | Supervisor 架构阅读 + 草图 | 4 | 心 |
| 二 | researcher 子 Agent | 5 | 整 |
| 三 | writer 子 Agent | 5 | 整 |
| 四 | critic 子 Agent | 5 | 整 |
| 五 | Handoff 串联 | 4 | 边 |
| 六 | 路由失败 case 调试 | 3 | 馈 |
| 日 | Review | 1.5 | 馈 |

---

## W14 · P4  Middleware + 并行

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 自定义 logging middleware | 5 | 边 |
| 二 | 限流 middleware | 5 | 边 |
| 三 | fan-out / fan-in 实验 | 5 | 边 |
| 四 | `p4-supervisor` 整合 | 5 | 边 |
| 五 | Token 成本统计 | 4 | 馈 |
| 六 | Trajectory 评测脚本 | 3 | 馈 |
| 日 | Review | 1.5 | 馈 |

---

## W15 · P4  验收

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 端到端内容流水线跑通 | 5 | 馈 |
| 二 | 失败 trace 分析 ×3 | 5 | 馈 |
| 三 | README + 架构图 | 4 | 整 |
| 四 | 评测报告整理 | 4 | 馈 |
| 五 | P4 验收答辩（自问自答） | 4 | 费 |
| 六 | 缓冲/补课 | 4 | 边 |
| 日 | Review | 1.5 | 馈 |

---

## W16 · P5  DeepAgents 入门

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | 阅读 ecosystem map + decision tree | 3 | 心 |
| 二 | `create_deep_agent` hello world | 5 | 馈 |
| 三 | 规划工具行为观察（LangSmith） | 5 | 心 |
| 四 | `subagents` 配置实验 | 5 | 边 |
| 五 | 文件系统 backend 读写 | 5 | 边 |
| 六 | best-practices 笔记对照 | 3 | 心 |
| 日 | Review | 1.5 | 馈 |

---

## W17 · P5  深代理项目

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `p5-deep-research` 骨架 | 5 | 边 |
| 二 | Skills 目录 + MCP tool | 5 | 联 |
| 三 | `interrupt_on` 敏感 tool | 4 | 馈 |
| 四 | `stream.subagents` 联调 | 5 | 馈 |
| 五 | 长任务端到端测试 | 5 | 馈 |
| 六 | 费曼：Deep Agent 四支柱 | 3 | 费 |
| 日 | P5 验收 + Review | 2.5 | 馈 |

---

## W18 · P6  API 化

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | FastAPI 基础 + health | 5 | 边 |
| 二 | Session 管理 + Agent 路由 | 5 | 边 |
| 三 | SSE 流式响应 | 5 | 馈 |
| 四 | 限流 / 超时 | 4 | 馈 |
| 五 | Prompt injection 防护清单 | 3 | 边 |
| 六 | Docker Compose 联调 | 4 | 馈 |
| 日 | Review | 1.5 | 馈 |

---

## W19 · P6  作品集收官

| 日 | 任务 | h | 理论 |
|----|------|---|------|
| 一 | `p6-agent-platform` 核心功能 | 5 | 边 |
| 二 | 继续平台；集成 P3/P5 资产 | 5 | 整 |
| 三 | ADR 文档 | 4 | 整 |
| 四 | 作品集 README + 截图 | 4 | 馈 |
| 五 | 博客：Shallow → Deep Agent | 4 | 费 |
| 六 | 模拟面试 + 全计划复盘 | 4 | 费 |
| 日 | 毕业验收 | 1.5 | 费 |
