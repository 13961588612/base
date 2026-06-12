# p0-harness-lab · Harness 本地实验

W1–W2 专用。**不写公司 Plugin**；只做安装、dry-run、源码阅读与实验记录。

## 前置

- 完成或并行 `python-ai` W2（能读 Python + 懂 LLM 流式概念）
- Python 3.12+

## 初始化

```bash
# 安装 CLI
pip install openharness-ai

# Windows PowerShell 使用 openh 而非 oh
openh setup

# 安全预览（不调用模型、不执行 Tool）
openh --dry-run
openh --dry-run -p "Explain this repository" --output-format json
```

## 本目录用途

```
p0-harness-lab/
├── README.md
├── experiments/
│   ├── 01-dry-run-notes.md      # dry-run 输出解读
│   ├── 02-provider-switch.md    # profile 切换记录
│   ├── 03-stream-json.md        # 非交互输出实验
│   └── 04-engine-reading.md     # engine 源码读书笔记
└── prompts/
    └── smoke-test.txt             # 冒烟 prompt
```

## 实验清单

| # | 实验 | 验收 |
|---|------|------|
| 1 | `--dry-run` 三种 readiness | 能解释 blocked 的 next actions |
| 2 | 配置 2 个 provider 并切换 | 同 prompt 换后端 |
| 3 | `-p "..." --output-format stream-json` | 能识别 tool_use 事件 |
| 4 | TUI `/skills` `/plan` `/resume` | 截图或文字记录 |
| 5 | 精读 engine loop | 能手绘 while 循环 |

## 验收

见 `../LEARNING_PLAN.md` P0 章节。

## 通过后

进入 W3：`../p1-custom-tool`
