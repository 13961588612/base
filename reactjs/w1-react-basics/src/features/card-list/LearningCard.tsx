import type { CardItem } from '../../types/card'
import { TagList } from '../../components/TagList'

interface LearningCardProps {
  card: CardItem
}

const accentBorder: Record<CardItem['accent'], string> = {
  indigo: 'border-t-indigo-500',
  emerald: 'border-t-emerald-500',
  amber: 'border-t-amber-500',
  rose: 'border-t-rose-500',
}

export function LearningCard({ card }: LearningCardProps) {
  return (
    <article
      className={`flex flex-col rounded-xl border border-slate-200 border-t-4 bg-white p-5 shadow-sm transition hover:shadow-md ${accentBorder[card.accent]}`}
    >
      <h3 className="text-lg font-semibold text-slate-900">{card.title}</h3>
      <p className="mt-2 flex-1 text-sm leading-relaxed text-slate-600">{card.description}</p>
      <div className="mt-4">
        <TagList tags={card.tags} />
      </div>
    </article>
  )
}
