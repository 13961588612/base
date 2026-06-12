"""
练习 14 · 实例方法

任务：
在 Message 上实现 preview(self, max_len: int = 40) -> str
返回格式："[{role}] {content前max_len字符}..."（若 content 更长则加 ...）

运行：python drills/14_class_methods.py
"""


class Message:
    def __init__(self, role: str, content: str) -> None:
        self.role = role
        self.content = content

    def preview(self, max_len: int = 40) -> str:
        # TODO: 实现预览字符串
        raise NotImplementedError


if __name__ == "__main__":
    short = Message("user", "hi")
    assert short.preview() == "[user] hi"

    long = Message("assistant", "a" * 50)
    assert long.preview(5) == "[assistant] aaaaa..."
    print("PASS: 14_class_methods")
