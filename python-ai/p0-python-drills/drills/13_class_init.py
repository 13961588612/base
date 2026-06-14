"""
练习 13 · class 与 __init__

任务：
定义类 Message：
  __init__(self, role: str, content: str)
  属性：role, content

运行：python drills/13_class_init.py
"""


class Message:
    # TODO: 实现 __init__ 并保存 role、content
    def __init__(self, role: str, content: str) -> None:
        self.role = role
        self.content = content

        #raise NotImplementedError


if __name__ == "__main__":
    m = Message("user", "hi")
    assert m.role == "user"
    assert m.content == "hi"
    print("PASS: 13_class_init")
