"""
练习 03 · dict 基础

任务：
给定 user = {"name": "Bob", "role": "admin"}
1. 读取 name
2. 新增键 "active": True
3. 返回更新后的 dict

运行：python drills/03_dict_basics.py
"""


def activate_user(user: dict) -> dict:
    # TODO: 基于 user 返回带 active=True 的新字典（可 copy 后修改）
    aCopy = {}
    for key,value in user.items():
        aCopy[key] = value
    aCopy["active"] = True
    return aCopy
    
    raise NotImplementedError


if __name__ == "__main__":
    original = {"name": "Bob", "role": "admin"}
    result = activate_user(original)
    assert result == {"name": "Bob", "role": "admin", "active": True}
    assert "active" not in original, "不要意外修改入参"
    print("PASS: 03_dict_basics")
