"""
练习 02 · list 基础

任务：
1. 在列表末尾追加 "done"
2. 返回新列表（不要修改原列表以外的逻辑错误）

运行：python drills/02_list_basics.py
"""


def append_done(items: list[str]) -> list[str]:
    # TODO: 复制或操作列表，使结果包含原元素 + "done"
    items.append("done")
    return items
    raise NotImplementedError


if __name__ == "__main__":
    assert append_done(["a", "b"]) == ["a", "b", "done"]
    assert append_done([]) == ["done"]
    print("PASS: 02_list_basics")
