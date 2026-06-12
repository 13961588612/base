"""
练习 04 · 类型转换

任务：
将字符串列表转为整数列表；无法转换的项跳过（不抛异常）。

示例：["1", "2", "x", "3"] → [1, 2, 3]

运行：python drills/04_type_convert.py
"""


from cgi import parse_header


def parse_ints(values: list[str]) -> list[int]:
    # TODO: 遍历 values，能 int() 的留下，不能的跳过
    parsed= []
    for value in values:
        try:
            parsed.append(int(value))
        except ValueError:
            continue
    return parsed
    
    raise NotImplementedError


if __name__ == "__main__":
    assert parse_ints(["1", "2", "x", "3"]) == [1, 2, 3]
    assert parse_ints(["10"]) == [10]
    assert parse_ints(["a", "b"]) == []
    print("PASS: 04_type_convert")
