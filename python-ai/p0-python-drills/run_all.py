"""
批量运行 20 道练习。在 p0-python-drills 目录执行：

    python run_all.py

全部通过则退出码 0；有失败则列出并退出码 1。
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

DRILLS_DIR = Path(__file__).parent / "drills"
DRILL_FILES = sorted(DRILLS_DIR.glob("[0-9][0-9]_*.py"))


def main() -> int:
    passed: list[str] = []
    failed: list[tuple[str, str]] = []

    for path in DRILL_FILES:
        result = subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent,
        )
        name = path.name
        if result.returncode == 0:
            passed.append(name)
            print(f"  OK  {name}")
        else:
            err = (result.stderr or result.stdout or "unknown error").strip()
            failed.append((name, err))
            print(f"  FAIL {name}")

    print()
    print(f"通过 {len(passed)}/{len(DRILL_FILES)}")
    if failed:
        print("\n失败详情：")
        for name, err in failed:
            print(f"--- {name} ---")
            print(err[:500])
        return 1
    print("全部通过，可进入 W2。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
