interface GreetingProps {
  name: string
  subtitle?: string
}

export function Greeting({ name, subtitle }: GreetingProps) {
  return (
    <div className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <h2 className="text-lg font-semibold text-slate-900">你好，{name}</h2>
      {subtitle ? <p className="mt-1 text-sm text-slate-600">{subtitle}</p> : null}
    </div>
  )
}
