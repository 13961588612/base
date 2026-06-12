"""
练习 11 · 多返回值

任务：
对整数列表返回 (最小值, 最大值, 平均值)。
平均值为 float；空列表返回 (None, None, None)。

运行：python drills/11_return_multiple.py
"""


def stats(numbers: list[int]) -> tuple[int | None, int | None, float | None]:
    # TODO: 用 min/max/sum 实现
    if(not numbers):
        return (None,None,None);

    return (min(numbers),max(numbers),sum(numbers)/len(numbers))

    raise NotImplementedError


if __name__ == "__main__":
    lo, hi, avg = stats([1, 2, 3, 4])
    assert lo == 1 and hi == 4 and avg == 2.5
    assert stats([]) == (None, None, None)
    print("PASS: 11_return_multiple")
