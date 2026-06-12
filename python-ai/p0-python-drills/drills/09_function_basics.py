"""
练习 09 · 函数基础

任务：
实现 truncate(text, max_len=100)：
  若 len(text) <= max_len，原样返回
  否则返回前 max_len 个字符 + "..."

运行：python drills/09_function_basics.py
"""


def truncate(text: str, max_len: int = 100) -> str:
    # TODO: 实现截断逻辑
    if(len(text)<=max_len):
      return text
    else:
      return text[:max_len] +"..." 
      
    raise NotImplementedError


if __name__ == "__main__":
    assert truncate("short") == "short"
    assert truncate("abcdef", max_len=3) == "abc..."
    assert truncate("x" * 100, max_len=100) == "x" * 100
    print("PASS: 09_function_basics")
