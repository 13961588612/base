"""
练习 07 · while 循环

任务：
用 while 将 n 每次减半（整除 //2），统计一共减半几次直到 n < 1。
示例：n=10 → 10→5→2→1→0，返回 4

运行：python drills/07_while_loop.py
"""


def halving_steps(n: int) -> int:
    # TODO: while n >= 1 时计数，n 用 //= 2 更新
    count = 0
    while n>=1 :
        count +=1
        n//=2

    return count   
    
    raise NotImplementedError


if __name__ == "__main__":
    assert halving_steps(10) == 4
    assert halving_steps(1) == 1
    assert halving_steps(0) == 0
    print("PASS: 07_while_loop")
