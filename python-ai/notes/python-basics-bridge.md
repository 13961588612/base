# Python 基础桥接笔记（Python 1/5 → Agent 可读码）

> **W1 专用**。本周目标不是「学会 Python」，而是「能读懂并改 Agent 项目里的常见代码」。

## 学习顺序（按天）

### Day 1–2：数据与流程

| 主题 | 要会什么 | Agent 里常见场景 |
|------|----------|------------------|
| 变量与类型 | `str` `int` `float` `bool` | tool 参数类型 |
| 容器 | `list` `dict` 增删查改、切片 | message 列表、config dict |
| 流程 | `if` `for` `while` `break` | 遍历 tool 结果 |
| 推导式 | `[x for x in ...]`、`{k: v}` | 快速转换检索结果 |

**练习**：给定 `messages = [{"role": "user", "content": "hi"}]`，用循环打印每条 content。

### Day 3：函数

```python
def greet(name: str, loud: bool = False) -> str:
    text = f"Hello, {name}"
    return text.upper() if loud else text
```

| 必会 | 说明 |
|------|------|
| `def` + 参数 + `return` | 每个 tool 都是函数 |
| 默认参数 | 可选参数 |
| `*args` / `**kwargs` | 读库代码时见到不慌 |
| f-string | 拼 prompt 最常用 |

**练习**：写 `def truncate(text: str, max_len: int = 100) -> str`。

### Day 4：类与模块

```python
# user.py
class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def preview(self) -> str:
        return f"[{self.role}] {self.content[:40]}..."
```

| 必会 | 说明 |
|------|------|
| `class` / `__init__` / `self` | Pydantic 模型底层思维 |
| `import` / `from x import y` | 项目分文件 |
| `if __name__ == "__main__":` | 脚本入口 |

**练习**：把 Message 拆到 `models.py`，`main.py` 里 import 使用。

### Day 5：异常与文件

```python
from pathlib import Path
import json

def load_config(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {path}") from e
```

| 必会 | 说明 |
|------|------|
| `try/except/raise` | API 失败、tool 出错 |
| `with open(...)` 或 `Path` | 读配置、写日志 |
| `json.load` / `json.dump` | 持久化对话、drills 答案 |

**练习**：Todo 列表存 `todos.json`，启动时加载。

### Day 6–7：装饰器（只读级理解）

Agent 代码里到处是 `@tool`、`@app.get`。W1 **不要求会写**，但要能读：

```python
def tool(func):
    func.is_tool = True
    return func

@tool
def search(query: str) -> str:
    """Search the web."""
    return "..."
```

理解：`@tool` = 把下面的函数交给 `tool` 处理后再用。

W2 写 `@tool` 时回来对照本节。

---

## W1 验收对照

- [ ] 独立完成 `p0-python-drills` ≥16/20
- [ ] 命令行 Todo：add / list / done / save
- [ ] 能口述：函数 vs 类、何时用 dict

## 推荐资源

- [Python 官方教程](https://docs.python.org/3/tutorial/) — 第 1–9 章（本周主线）
- 遇卡壳：搜「Real Python + 关键词」作补充，**不要**换语言或跳去写 Agent

## 常见误区（Python 1/5）

| 误区 | 正确做法 |
|------|----------|
| W1 就想跑 LangChain | W1 零 LLM；先把 drills 做完 |
| 背语法不写字 | 每天至少 2h 在 `.py` 文件里敲 |
| 深入 asyncio 源码 | W1–W3 只需「能认出 async 函数」 |
| 同时学 Django/FastAPI | P6 再学 FastAPI；W1 只做脚本 |

---

*学完后在此记录薄弱点，W2 前复习：*

- 薄弱 1：
- 薄弱 2：
