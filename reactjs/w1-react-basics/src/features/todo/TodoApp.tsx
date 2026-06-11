import { useMemo, useState } from 'react'
import type { Todo, TodoFilter } from '../../types/todo'

function createTodo(text: string): Todo {
  return { id: crypto.randomUUID(), text, completed: false }
}

const FILTERS: { value: TodoFilter; label: string }[] = [
  { value: 'all', label: '全部' },
  { value: 'active', label: '进行中' },
  { value: 'completed', label: '已完成' },
]

export function TodoApp() {
  const [todos, setTodos] = useState<Todo[]>([
    { id: '1', text: '读完 vue-react-map.md', completed: true },
    { id: '2', text: '完成 W1 Todo 对比笔记', completed: false },
  ])
  const [draft, setDraft] = useState('')
  const [filter, setFilter] = useState<TodoFilter>('all')

  const visibleTodos = useMemo(() => {
    if (filter === 'active') return todos.filter((t) => !t.completed)
    if (filter === 'completed') return todos.filter((t) => t.completed)
    return todos
  }, [filter, todos])

  function addTodo() {
    const text = draft.trim()
    if (!text) return
    setTodos((prev) => [...prev, createTodo(text)])
    setDraft('')
  }

  function toggleTodo(id: string) {
    setTodos((prev) =>
      prev.map((t) => (t.id === id ? { ...t, completed: !t.completed } : t)),
    )
  }

  function removeTodo(id: string) {
    setTodos((prev) => prev.filter((t) => t.id !== id))
  }

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
      <div className="flex gap-2">
        <input
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && addTodo()}
          placeholder="添加待办…"
          className="flex-1 rounded-lg border border-slate-300 px-3 py-2 text-sm outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200"
        />
        <button
          type="button"
          onClick={addTodo}
          className="rounded-lg bg-indigo-600 px-4 py-2 text-sm font-medium text-white hover:bg-indigo-700"
        >
          添加
        </button>
      </div>

      <div className="mt-3 flex gap-2">
        {FILTERS.map((item) => (
          <button
            key={item.value}
            type="button"
            onClick={() => setFilter(item.value)}
            className={`rounded-full px-3 py-1 text-xs font-medium ${
              filter === item.value
                ? 'bg-indigo-600 text-white'
                : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
            }`}
          >
            {item.label}
          </button>
        ))}
      </div>

      <ul className="mt-4 space-y-2">
        {visibleTodos.length === 0 ? (
          <li className="text-sm text-slate-500">暂无待办</li>
        ) : (
          visibleTodos.map((todo) => (
            <li key={todo.id} className="flex items-center gap-3 rounded-lg bg-slate-50 px-3 py-2">
              <input
                type="checkbox"
                checked={todo.completed}
                onChange={() => toggleTodo(todo.id)}
                className="h-4 w-4 rounded border-slate-300"
              />
              <span
                className={`flex-1 text-sm ${todo.completed ? 'text-slate-400 line-through' : 'text-slate-800'}`}
              >
                {todo.text}
              </span>
              <button
                type="button"
                onClick={() => removeTodo(todo.id)}
                className="text-xs text-rose-600 hover:text-rose-700"
              >
                删除
              </button>
            </li>
          ))
        )}
      </ul>

      <p className="mt-3 text-xs text-slate-500">
        剩余 {todos.filter((t) => !t.completed).length} 项 · React 版：事件驱动，无 v-model
      </p>
    </div>
  )
}
