"""
练习 19 · 文件读取

任务：
用 pathlib.Path 读取文件，返回非空行列表（去掉首尾空白，跳过空行）。

数据文件：drills/data/sample.txt（与本文件相对路径）

运行（在 p0-python-drills 目录）：
  python drills/19_file_read.py
"""

from pathlib import Path


def read_nonempty_lines(path: Path) -> list[str]:
    # TODO: path.read_text(encoding="utf-8") 并按行处理
    raise NotImplementedError


if __name__ == "__main__":
    data_file = Path(__file__).parent / "data" / "sample.txt"
    lines = read_nonempty_lines(data_file)
    assert lines == ["line one", "line two", "line three"]
    print("PASS: 19_file_read")
