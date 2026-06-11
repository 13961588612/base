import type { User } from '../types/user'
import { RoleBadge } from './StatusBadge'

interface UserCardProps {
  user: User
  onSelect?: (id: number) => void
}

export function UserCard({ user, onSelect }: UserCardProps) {
  return (
    <article className="flex items-center gap-3 rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <div className="flex h-10 w-10 items-center justify-center rounded-full bg-indigo-100 text-sm font-medium text-indigo-700">
        {user.name.slice(0, 1)}
      </div>
      <div className="flex-1 text-left">
        <h3 className="font-medium text-slate-900">{user.name}</h3>
        <RoleBadge role={user.role} />
      </div>
      {onSelect ? (
        <button
          type="button"
          onClick={() => onSelect(user.id)}
          className="rounded-md bg-indigo-600 px-3 py-1.5 text-sm text-white hover:bg-indigo-700"
        >
          查看
        </button>
      ) : null}
    </article>
  )
}
