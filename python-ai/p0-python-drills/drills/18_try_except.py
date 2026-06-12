"""
练习 18 · 异常处理

任务：
safe_divide(a, b)：
  b == 0 时返回 None（不抛异常）
  否则返回 a / b

运行：python drills/18_try_except.py
"""


def safe_divide(a: float, b: float) -> float | None:
    # TODO: 用 try/except 或 if 实现
    try:
      return a/b
    except ZeroDivisionError:
      return  None

    raise NotImplementedError


if __name__ == "__main__":
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None
    print("PASS: 18_try_except")
