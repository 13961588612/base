"""
练习 08 · 推导式

任务：
1. 用列表推导式保留偶数
2. 用字典推导式将 words 转为 {word: len(word)}

运行：python drills/08_comprehension.py
"""


def keep_even(numbers: list[int]) -> list[int]:
    # TODO: 列表推导式
    return [x for x in numbers  if x%2==0 ]

    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    # TODO: 字典推导式
    return { word:len(word) for word in words}
    raise NotImplementedError


if __name__ == "__main__":
    assert keep_even([1, 2, 3, 4, 5]) == [2, 4]
    assert word_lengths(["hi", "py"]) == {"hi": 2, "py": 2}
    print("PASS: 08_comprehension")
