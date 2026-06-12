"""
练习 05 · if / elif / else

任务：
根据分数返回等级：
  >= 90 → "A"
  >= 80 → "B"
  >= 60 → "C"
  否则   → "F"

运行：python drills/05_if_else.py
"""


def grade(score: int) -> str:
    # TODO: 用 if/elif/else 实现
    if(score >= 90):
        return "A"
    elif(score >= 80):
        return "B"
    elif(score >= 60):
        return "C"
    else:
        return "F"
    raise NotImplementedError


if __name__ == "__main__":
    assert grade(95) == "A"
    assert grade(80) == "B"
    assert grade(60) == "C"
    assert grade(59) == "F"
    print("PASS: 05_if_else")
