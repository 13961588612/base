"""
练习 20 · JSON 综合

任务：
读取 messages JSON 列表，统计每个 role 出现次数。
返回 dict，例如 {"user": 3, "assistant": 1, "tool": 1}

数据文件：drills/data/messages.json

运行（在 p0-python-drills 目录）：
  python drills/20_json_stats.py
"""

import json
from pathlib import Path


def count_roles(path: Path) -> dict[str, int]:
    # TODO: json.loads + 遍历统计
    raise NotImplementedError


if __name__ == "__main__":
    data_file = Path(__file__).parent / "data" / "messages.json"
    counts = count_roles(data_file)
    assert counts == {"user": 3, "assistant": 1, "tool": 1}
    print("PASS: 20_json_stats")
