"""
练习 17 · 同目录模块 import

任务：
从 drill_helpers 导入 greet 和 add，实现：
  formal_greet(name) → greet(name) + "!"   （用已导入的 greet）
  sum_pair(a, b)     → 调用 drill_helpers.add

提示：drill_helpers.py 与本文件同在 drills/ 目录。

运行（请在 p0-python-drills 目录下）：
  python drills/17_import_module.py
"""


def formal_greet(name: str) -> str:
    # TODO: from drill_helpers import greet

    from drill_helpers import greet 
    return greet(name)+"!"

    raise NotImplementedError


def sum_pair(a: int, b: int) -> int:
    # TODO: 使用 drill_helpers.add

    from drill_helpers import add
    return add(a,b)
    
    raise NotImplementedError


if __name__ == "__main__":
    assert formal_greet("Ada") == "Hello, Ada!"
    assert sum_pair(2, 3) == 5
    print("PASS: 17_import_module")
