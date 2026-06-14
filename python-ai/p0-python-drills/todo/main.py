"""
命令行 Todo · W1 项目

用法（在 p0-python-drills 目录）：
  python todo/main.py add "学 Python"
  python todo/main.py list
  python todo/main.py done 1
  python todo/main.py save

验收：四项命令可用；数据写入 todo/todos.json；至少一个自定义 class（见 storage.py）
"""

import argparse
import sys

from storage import TodoStore

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="命令行 Todo")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="列出所有待办")

    add_p = sub.add_parser("add", help="添加待办")
    add_p.add_argument("title", help="待办标题")

    done_p = sub.add_parser("done", help="标记完成")
    done_p.add_argument("id", type=int, help="待办 id")

    sub.add_parser("save", help="显式保存到 todos.json")

    return parser


def cmd_list(store: TodoStore) -> None:
    # TODO: 遍历 store.list_items()，print 每条；空列表时提示「暂无待办」
    items = store.list_items()
    if(not items):
        print("暂无待办")
    else:
        for item in items:
            print(item)    
    #raise NotImplementedError


def cmd_add(store: TodoStore, title: str) -> None:
    # TODO: store.add(title)，打印「已添加: ...」
    store.add(title)
    print(f"已添加: {title}")
    #raise NotImplementedError


def cmd_done(store: TodoStore, id: int) -> None:
    # TODO: store.mark_done(id)；成功/失败各打印一行提示
    if store.mark_done(id):
        print(f"成功")
    else:
        print(f"失败")
    #raise NotImplementedError


def cmd_save(store: TodoStore) -> None:
    # TODO: store.save()，打印「已保存」
    #       若 add/done 已自动 save，此命令仍应能显式调用
    store.save()
    print("已保存")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    store = TodoStore()

    if args.command == "list":
        cmd_list(store)
    elif args.command == "add":
        cmd_add(store, args.title)
    elif args.command == "done":
        cmd_done(store, args.id)
    elif args.command == "save":
        cmd_save(store)
    else:
        print(f"未知命令: {args.command}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
