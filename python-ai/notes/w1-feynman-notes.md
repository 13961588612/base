# W1 费曼笔记 · list / dict / import / 函数与类

> W1 验收口述题参考答案。用自己的话能讲出来，才算过关。

---

## 1. list vs dict 何时用？

**一句话**：list 管「有序的一串同类东西」；dict 管「按名字查值的映射」。

### 用 list

- 需要 **顺序**（第几条、先后来回）
- 元素是 **同一类东西**，主要靠 **位置** 区分
- 常见操作：追加、遍历、排序、切片

**例子**：

```python
# 对话历史：按时间顺序一条条往下加
messages = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好！"},
]

# Todo 列表：多条待办，list_items() 按 id 排序后遍历
for item in store.list_items():
    print(item)
```

选 list 不是因为「里面可以放 dict」，而是因为 **整体是有序集合**。

### 用 dict

- 需要 **按键快速查找**（O(1)），不关心顺序或顺序不重要
- 每个键有 **语义**（名字有意义），不是「第 0 个、第 1 个」
- 常见操作：按 key 读写、合并配置、JSON 序列化

**例子**：

```python
# 配置：按名字取 API Key、模型名
config = {"openai_api_key": "...", "default_model": "gpt-4o-mini"}

# 统计：每个 role 出现几次（练习 20_json_stats）
counts = {"user": 3, "assistant": 1, "tool": 1}

# 持久化：TodoItem.to_dict() → JSON 里的一条记录
{"id": 1, "title": "学 Python", "done": true}
```

### 怎么选（速查）

| 场景 | 选什么 | 原因 |
|------|--------|------|
| 聊天 message 历史 | list | 有顺序，一条条追加 |
| 环境变量 / 配置项 | dict | 按名字查 `OPENAI_API_KEY` |
| 检索结果列表 | list | 多条结果，常按序号或分数排序 |
| role → 出现次数 | dict | 键是 role，值是计数 |
| 单条 Todo 存盘 | dict | 固定字段 id/title/done，键有含义 |

**误区**：「多条记录」不一定用 list。若每条结构固定、且总要按 `id` 查某一条，可以用 `dict[id → item]`；Todo 项目用 list + 遍历查找，是因为条目少、写法简单，W1 足够。

---

## 2. `import` 模块 vs 用路径读文件，有什么区别？

**一句话**：`import` 是加载 **Python 代码模块**；路径读文件是打开 **磁盘上的任意文件**（文本、JSON、图片等）。

### `import` 模块

- 加载的是 **`.py` 模块**（或已安装的包），由 Python **导入系统** 解析
- 得到的是模块里的 **函数、类、变量**（可复用的代码）
- 路径由 **包结构 + `sys.path`** 决定，不是随便写绝对路径
- 典型写法：`from storage import TodoStore`、`from drill_helpers import greet`

```python
from storage import TodoStore   # Python 在 sys.path 里找 storage.py

store = TodoStore()             # 用的是「代码能力」
```

和 Agent 的关系：后面会 `from langchain_openai import ChatOpenAI`——这是在 **复用别人写好的代码**。

### 用路径读文件

- 打开的是 **具体文件路径** 上的 **数据**（内容在磁盘上）
- 用 `pathlib.Path` 或 `open()`，配合 `read_text()` / `json.load()` 等
- 路径可以是相对路径（相对当前脚本或工作目录）或绝对路径
- 读到的是 **字符串、字节、JSON 解析后的 dict/list** 等 **数据**，不是可执行的 Python 模块

```python
from pathlib import Path

path = Path(__file__).parent / "todos.json"   # 数据文件在哪
data = path.read_text(encoding="utf-8")       # 读的是「文件内容」
items = json.loads(data)                        # 再解析成 Python 对象
```

Todo 项目里两者同时出现：

- `main.py` **import** `TodoStore` → 用 Python 类提供的逻辑
- `TodoStore` 用 **Path** 读 `todos.json` → 用磁盘上的持久化数据

### 对比表

| | `import` 模块 | 路径读文件 |
|--|---------------|------------|
| 对象 | `.py` 代码 | `.json` / `.txt` / `.env` 等 |
| 得到什么 | 函数、类、变量 | 文件内容（再解析） |
| 路径含义 | 模块搜索路径 | 文件在磁盘上的位置 |
| 典型用途 | 复用代码、调库 | 配置、持久化、读数据集 |
| Todo 例子 | `from storage import TodoStore` | `DATA_FILE.read_text()` |

**口述要点**：import 是「找代码来执行」；读文件是「找数据来解析」。`.env`、`.json` 用路径读；`langchain`、`storage` 用 import。

---

## 3. 函数 vs 类、什么时候用 dict？

### 函数 vs 类

**函数**：做 **一件事**，输入 → 输出，不需要长期记住「状态」。

```python
def truncate(text: str, max_len: int = 100) -> str:
    return text[:max_len]

def count_roles(path: Path) -> dict[str, int]:
  ...
```

适合：纯计算、一次性转换、drills 里大部分小题。

**类**：把 **数据 + 行为** 绑在一起，需要 **多个相关字段** 和 **多步操作同一份数据**。

```python
class TodoItem:
    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done

    def to_dict(self) -> dict: ...
    def __str__(self) -> str: ...
```

适合：

- 有固定字段（id、title、done）且要带方法（序列化、格式化显示）
- 多个对象并存（很多条 Todo），每条结构相同
- 后面 W2 的 Pydantic 模型、Agent 里的 Message 类，都是同一思路

**口述要点**：

- 只有输入输出、无状态 → **函数**
- 多条「同一种东西」、要封装字段 + 方法 → **类**
- Todo 用 `TodoItem` 而不是三个散落的变量，是因为一条待办是 **一个整体**

### 什么时候用 dict（而不是类）？

**用 dict**：

- 结构 **简单、临时**，或 **键不固定**（半结构化 JSON）
- 主要为了 **序列化**（`json.dumps` 天然支持 dict）
- 只是 **中间数据**，不需要自定义方法
- 配置、统计结果、API 返回的 JSON

```python
{"id": 1, "title": "学 Python", "done": False}   # 存盘、网络传输
{"user": 3, "assistant": 1}                        # 统计结果
```

**用类（或 W2 的 Pydantic 模型）**：

- 字段固定，要在多处保证类型一致
- 需要方法：`to_dict()`、`from_dict()`、`__str__()`
- 业务里会长期维护这个「实体」（Todo、Message、User）

**口述要点**：dict 是「一袋键值对数据」；类是「有名字、有行为的对象」。持久化时类常通过 `to_dict()` 变成 dict 再写 JSON——Todo 的 `save()` / `load()` 就是这套模式。

### 三者关系（一张图）

```
磁盘 todos.json  ──read──►  dict  ──from_dict──►  TodoItem（类）
                              ▲                        │
                              │      to_dict()         │
                              └────────────────────────┘
```

---

## W1 验收自测（合上笔记能答）

1. **list vs dict**：有序同类用 list；按名字查、配置、计数用 dict。
2. **import vs 读文件**：import 加载 Python 代码；Path/open 读磁盘上的数据文件。
3. **函数 vs 类 vs dict**：无状态逻辑用函数；固定字段 + 行为用类；简单/临时/可 JSON 的数据用 dict。

---

## 关联练习

- list / dict：`drills/02_list_basics.py`、`03_dict_basics.py`、`06_for_loop.py`
- 读文件 / JSON：`drills/19_file_read.py`、`20_json_stats.py`
- import：`drills/17_import_module.py`
- 类：`drills/13_class_init.py`、`todo/storage.py`
