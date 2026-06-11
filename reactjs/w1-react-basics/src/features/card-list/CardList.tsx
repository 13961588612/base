import { LEARNING_CARDS } from '../../data/cards'
import { LearningCard } from './LearningCard'

export function CardList() {
  return (
    <section className="space-y-4">
      <div>
        <h3 className="text-lg font-semibold text-slate-900">W1 知识卡片</h3>
        <p className="mt-1 text-sm text-slate-500">周五任务：纯 Tailwind 响应式卡片列表</p>
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {LEARNING_CARDS.map((card) => (
          <LearningCard key={card.id} card={card} />
        ))}
      </div>
    </section>
  )
}
