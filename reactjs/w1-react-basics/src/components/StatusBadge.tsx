import type { User } from '../types/user'

type BadgeTone = 'neutral' | 'success' | 'warning'

interface StatusBadgeProps {
  label: string
  tone?: BadgeTone
}

const toneClass: Record<BadgeTone, string> = {
  neutral: 'bg-slate-100 text-slate-700',
  success: 'bg-emerald-100 text-emerald-800',
  warning: 'bg-amber-100 text-amber-800',
}

export function StatusBadge({ label, tone = 'neutral' }: StatusBadgeProps) {
  return (
    <span className={`inline-flex rounded-full px-2.5 py-0.5 text-xs font-medium ${toneClass[tone]}`}>
      {label}
    </span>
  )
}

const roleTone: Record<User['role'], BadgeTone> = {
  admin: 'warning',
  editor: 'success',
  viewer: 'neutral',
}

const roleLabel: Record<User['role'], string> = {
  admin: '管理员',
  editor: '编辑',
  viewer: '访客',
}

interface RoleBadgeProps {
  role: User['role']
}

export function RoleBadge({ role }: RoleBadgeProps) {
  return <StatusBadge label={roleLabel[role]} tone={roleTone[role]} />
}
