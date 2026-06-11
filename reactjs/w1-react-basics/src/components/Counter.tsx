import { useState } from 'react'

/** W1 周三：与 Vue ref 计数器对比用 */
export function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <p className="mb-3 font-mono text-2xl text-slate-900">{count}</p>
      <div className="flex gap-2">
        <button
          type="button"
          onClick={() => setCount((c) => c - 1)}
          className="rounded-md border border-slate-300 px-3 py-1.5 text-sm hover:bg-slate-50"
        >
          −
        </button>
        <button
          type="button"
          onClick={() => setCount((c) => c + 1)}
          className="rounded-md bg-indigo-600 px-3 py-1.5 text-sm text-white hover:bg-indigo-700"
        >
          +
        </button>
      </div>
    </div>
  )
}
