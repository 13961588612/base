"""
练习 15 · 继承初识

任务：
1. ToolMessage 继承 Message，多一个属性 tool_name: str
2. __init__(self, tool_name, content) 内部 role 固定为 "tool"

运行：python drills/15_inheritance.py
"""


class Message:
    def __init__(self, role: str, content: str) -> None:
        self.role = role
        self.content = content


class ToolMessage(Message):
    # TODO: 调用 super().__init__，并设置 tool_name
    def __init__(self, tool_name: str, content: str) -> None:
        super().__init__("tool",content)
        self.tool_name = tool_name

        #raise NotImplementedError


if __name__ == "__main__":
    t = ToolMessage("search", "result data")
    assert t.role == "tool"
    assert t.tool_name == "search"
    assert t.content == "result data"
    print("PASS: 15_inheritance")
