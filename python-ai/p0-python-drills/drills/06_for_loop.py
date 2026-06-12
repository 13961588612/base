"""
练习 06 · for 循环

任务：
给定 messages = [{"role": "...", "content": "..."}, ...]
返回所有 content 组成的列表（保持顺序）。

运行：python drills/06_for_loop.py
"""


def extract_contents(messages: list[dict]) -> list[str]:
    # TODO: 用 for 循环收集每条 message 的 "content"
    contents = []
    for message  in messages:
        if message["content"] is not None:
            contents.append(message["content"])
    return contents
    
    raise NotImplementedError


if __name__ == "__main__":
    data = [
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "hello"},
    ]
    assert extract_contents(data) == ["hi", "hello"]
    assert extract_contents([]) == []
    print("PASS: 06_for_loop")
