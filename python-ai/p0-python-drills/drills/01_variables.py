"""
练习 01 · 变量与 f-string

任务：
1. 用变量 name（str）、age（int）拼出句子
2. 返回格式："{name} is {age} years old"（name、age 用实际值替换）

运行：python drills/01_variables.py
"""


def build_intro(name: str, age: int) -> str:
    # TODO: 使用 f-string 返回介绍语
    return f"{name} is {age} years old"
    
    raise NotImplementedError


if __name__ == "__main__":
    result = build_intro("Ada", 28)
    assert result == "Ada is 28 years old", f"got: {result!r}"
    print("PASS: 01_variables")
