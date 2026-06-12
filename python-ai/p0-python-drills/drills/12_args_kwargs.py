"""
练习 12 · *args 与 **kwargs

任务：
1. sum_all(*args) → 所有数字之和
2. merge_config(base: dict, **overrides) → 合并字典，overrides 覆盖 base

运行：python drills/12_args_kwargs.py
"""


def sum_all(*args: int) -> int:
    # TODO: 累加 args    
    if(not args):
        return 0
    sumed :int =  sum(args)
    return sumed
    raise NotImplementedError


def merge_config(base: dict, **overrides) -> dict:
    # TODO: 返回新 dict，overrides 优先
    if(not overrides):
        return base
    return {**base,**overrides}    
    
    raise NotImplementedError


if __name__ == "__main__":
    assert sum_all(1, 2, 3) == 6
    assert sum_all() == 0
    assert merge_config({"a": 1, "b": 2}, b=9, c=3) == {"a": 1, "b": 9, "c": 3}
    print("PASS: 12_args_kwargs")
