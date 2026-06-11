interface TagListProps {
  tags: string[]
  emptyText?: string
}

export function TagList({ tags, emptyText = '暂无标签' }: TagListProps) {
  if (tags.length === 0) {
    return <p className="text-sm text-slate-500">{emptyText}</p>
  }

  return (
    <ul className="flex flex-wrap gap-2">
      {tags.map((tag) => (
        <li
          key={tag}
          className="rounded-full bg-slate-100 px-3 py-1 text-sm text-slate-700"
        >
          {tag}
        </li>
      ))}
    </ul>
  )
}
