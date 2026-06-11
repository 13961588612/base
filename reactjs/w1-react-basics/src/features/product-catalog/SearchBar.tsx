interface SearchBarProps {
  filterText: string
  inStockOnly: boolean
  onFilterTextChange: (value: string) => void
  onInStockOnlyChange: (value: boolean) => void
}

export function SearchBar({
  filterText,
  inStockOnly,
  onFilterTextChange,
  onInStockOnlyChange,
}: SearchBarProps) {
  return (
    <form className="flex flex-col gap-3 sm:flex-row sm:items-center">
      <input
        type="text"
        value={filterText}
        placeholder="搜索商品…"
        onChange={(e) => onFilterTextChange(e.target.value)}
        className="flex-1 rounded-lg border border-slate-300 px-3 py-2 text-sm outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200"
      />
      <label className="flex items-center gap-2 text-sm text-slate-700">
        <input
          type="checkbox"
          checked={inStockOnly}
          onChange={(e) => onInStockOnlyChange(e.target.checked)}
          className="h-4 w-4 rounded border-slate-300"
        />
        仅显示有货
      </label>
    </form>
  )
}
