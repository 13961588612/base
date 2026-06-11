# p0-python-drills · Python 基础练习

W1 专用。**不安装 LangChain，不用 uv 也行**（系统 Python 即可）。

## 目录建议

```
p0-python-drills/
├── README.md
├── drills/
│   ├── 01_variables.py      # 自填答案区
│   ├── 02_functions.py
│   ├── ...
│   └── 20_dict_merge.py
├── todo/
│   ├── main.py              # 命令行 Todo
│   ├── storage.py           # JSON 持久化
│   └── todos.json           # 运行时生成
└── answers/                 # 做完后再对照（可选）
```

## 20 道小题主题分布

| 编号 | 主题 |
|------|------|
| 01–04 | 变量、类型、list/dict 操作 |
| 05–08 | if/for、推导式 |
| 09–12 | 函数、默认参数、返回值 |
| 13–15 | class 基础 |
| 16–17 | import 与模块 |
| 18–19 | 异常处理 |
| 20 | 综合：读 JSON 文件并统计 |

每题文件顶部有题目说明，在 `# TODO:` 下写代码。用 `python drills/01_variables.py` 自测。

## Todo 项目要求（W1 后半）

```bash
python todo/main.py add "学 Python"
python todo/main.py list
python todo/main.py done 1
```

- 子命令用 `sys.argv` 或 `argparse`（二选一）
- 数据写入 `todo/todos.json`
- 至少 1 个自定义 `class` 或 `@dataclass`（W2 会学 Pydantic，此处先用原生 class）

## 验收

- ≥16/20 小题通过（自己写测试或 print 断言）
- Todo 四项命令可用
- 见 `../notes/python-basics-bridge.md` W1 验收

## 通过后

进入 W2：`cd ../p0-cli-chat` 用 **uv** 初始化 LLM 项目。
