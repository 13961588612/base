"""
练习 10 · 默认参数

任务：
实现 greet(name, loud=False)：
  loud=False → "Hello, {name}"
  loud=True  → 全大写版本

运行：python drills/10_default_args.py
"""


def greet(name: str, loud: bool = False) -> str:
    # TODO: 注意默认参数 loud=False
    if(not loud):
      return f"hello,{name}"
    else:
      return name.upper();  
      
    raise NotImplementedError


if __name__ == "__main__":
    assert greet("Ada") == "Hello, Ada"
    assert greet("Ada", loud=True) == "HELLO, ADA"
    print("PASS: 10_default_args")
