import { useState } from 'react'
import { Counter } from './components/Counter'
import { Greeting } from './components/Greeting'
import { TagList } from './components/TagList'
import { UserCard } from './components/UserCard'
import { CardList } from './features/card-list/CardList'
import { ProductFilterTable } from './features/product-catalog/ProductFilterTable'
import { TodoApp } from './features/todo/TodoApp'
import type { User } from './types/user'

const demoUsers: User[] = [
  { id: 1, name: '小林', role: 'admin' },
  { id: 2, name: '阿杰', role: 'editor' },
  { id: 3, name: '小美', role: 'viewer' },
]

const W1_TABS = [
  { id: 'day2', label: '周二·组件' },
  { id: 'day3', label: '周三·Todo' },
  { id: 'day4', label: '周四·拆分' },
  { id: 'day5', label: '周五·卡片' },
] as const

type TabId = (typeof W1_TABS)[number]['id']

function App() {
  const [tab, setTab] = useState<TabId>('day2')

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <header className="border-b border-slate-200 bg-white">
        <div className="mx-auto max-w-3xl px-4 py-6">
          <p className="text-sm font-medium text-indigo-600">W1 · P0 · Vue → React</p>
          <h1 className="mt-1 text-2xl font-bold">第一周学习沙盒</h1>
          <p className="mt-2 text-sm text-slate-600">点击下面四个标签切换每日练习</p>

          <nav className="mt-4 flex flex-wrap gap-2" aria-label="W1 每日练习">
            {W1_TABS.map((item) => (
              <button
                key={item.id}
                type="button"
                onClick={() => setTab(item.id)}
                className={`rounded-full px-3 py-1.5 text-sm font-medium transition ${
                  tab === item.id
                    ? 'bg-indigo-600 text-white shadow-sm'
                    : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                }`}
              >
                {item.label}
              </button>
            ))}
          </nav>
        </div>
      </header>

      <main className="mx-auto max-w-3xl space-y-8 px-4 py-8">
        {tab === 'day2' && (
          <>
            <section className="space-y-3">
              <h2 className="text-lg font-semibold">周二 · 5 个函数组件</h2>
              <Greeting name="学习者" subtitle="从 Vue 迁移到 React 18" />
              <div className="grid gap-3 sm:grid-cols-2">
                {demoUsers.map((user) => (
                  <UserCard key={user.id} user={user} onSelect={(id) => console.log('select', id)} />
                ))}
              </div>
              <TagList tags={['React', 'TypeScript', 'Tailwind']} />
            </section>
            <section className="space-y-3">
              <h2 className="text-lg font-semibold">计数器（与 Vue 对比用）</h2>
              <Counter />
            </section>
          </>
        )}

        {tab === 'day3' && (
          <section className="space-y-3">
            <h2 className="text-lg font-semibold">周三 · React Todo</h2>
            <TodoApp />
          </section>
        )}

        {tab === 'day4' && (
          <section className="space-y-3">
            <h2 className="text-lg font-semibold">周四 · Thinking in React</h2>
            <ProductFilterTable />
          </section>
        )}

        {tab === 'day5' && <CardList />}
      </main>
    </div>
  )
}

export default App
