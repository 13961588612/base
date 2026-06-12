"""
练习 16 · 标准库 import

任务：
使用 math 模块实现：
  circle_area(radius) → π * r²（用 math.pi）

运行：python drills/16_stdlib_import.py
"""


def circle_area(radius: float) -> float:
    # TODO: import math 并计算面积
    import math
    return math.pi*math.pow(radius,2)
    
    raise NotImplementedError


if __name__ == "__main__":
    import math

    assert abs(circle_area(1) - math.pi) < 1e-9
    assert abs(circle_area(2) - 4 * math.pi) < 1e-9
    print("PASS: 16_stdlib_import")
