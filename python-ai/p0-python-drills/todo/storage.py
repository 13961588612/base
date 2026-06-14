"""
Todo 数据模型与 JSON 持久化。

数据文件：todo/todos.json（与本文件同级，运行时生成）
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "todos.json"


class TodoItem:
    """单条待办。"""

    def __init__(self, id: int, title: str, done: bool = False) -> None:
        # TODO: 保存 id、title、done
        self.id = id
        self.title =title
        self.done = done
        #raise NotImplementedError

    def to_dict(self) -> dict:
        # TODO: 返回 {"id": ..., "title": ..., "done": ...}
        return {"id":self.id,"title":self.title,"done":self.done}
        #raise NotImplementedError

    @classmethod
    def from_dict(cls, data: dict) -> "TodoItem":
        # TODO: 从 dict 构造 TodoItem
        return TodoItem(data["id"],data["title"],data["done"])
        #raise NotImplementedError

    def __str__(self) -> str:
        if self.done:
            return f"[{self.id}] ✓ {self.title}"
        return f"[{self.id}] {self.title}"


class TodoStore:
    """管理 Todo 列表：加载、保存、增删改。"""

    def __init__(self, path: Path = DATA_FILE) -> None:
        self.path = path
        self.items: list[TodoItem] = []
        self.load()
        # TODO: 启动时调用 self.load()

    def load(self) -> None:
        # TODO: 若 path 不存在 → items 为空列表
        #       若存在 → json.loads 后转为 TodoItem 列表
        #       JSON 损坏时用 try/except 给出友好提示
        try:
            if self.path.exists():
                content = self.path.read_text(encoding="utf-8")
                json_text:list[dict] = json.loads(content)
                self.items = [TodoItem.from_dict(item) for item in json_text if item["id"] and item["title"]]
                """
                for item in json:
                    if(item["id"] and item["title"]):
                        toItemDone = False
                        if(item["done"]==True or item["done"]==False):
                            toItemDone = item["done"]
                        toItem = TodoItem(item["id"],item["title"],toItemDone)
                        self.items.append(toItem)
                """
            else:
                self.items = []
        except FileNotFoundError as e:
            self.items = []        
        except json.JSONDecodeError as e:
            print(f"JSON 损坏: {self.path}")
            self.items = []
        #raise NotImplementedError

    def save(self) -> None:
        # TODO: 把 self.items 写成 JSON 数组写入 self.path
        #       提示：json.dump(..., indent=2, ensure_ascii=False)

        json_data = [item.to_dict() for item in self.items]
        content:str = json.dumps(json_data,indent=2,ensure_ascii=False)
        self.path.write_text(content,encoding="utf-8")

        #raise NotImplementedError

    def add(self, title: str) -> TodoItem:
        # TODO: 新 id = 当前最大 id + 1（无条目时从 1 开始）
        #       追加到 items，调用 save()，返回新条目
        if(not self.items):
            maxId = 0;
        else:    
            maxId = max(self.items,key = lambda  x:x.id).id

        new_item = TodoItem(maxId + 1, title, False)
        self.items.append(new_item)
        self.save()
        return new_item

    def list_items(self) -> list[TodoItem]:
        # TODO: 返回 items（可按 id 排序）
        return sorted(self.items, key=lambda x: x.id)

    def mark_done(self, id: int) -> bool:
        # TODO: 找到对应 id，设 done=True，save()，找到返回 True，否则 False
        for item in self.items:
            if(item.id) == id:
                item.done = True
                self.save()
                return True
        return False
