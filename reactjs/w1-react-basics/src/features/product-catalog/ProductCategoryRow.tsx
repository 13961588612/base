interface ProductCategoryRowProps {
  category: string
}

export function ProductCategoryRow({ category }: ProductCategoryRowProps) {
  return (
    <tr>
      <th colSpan={2} className="bg-slate-100 px-3 py-2 text-left text-sm font-semibold text-slate-700">
        {category}
      </th>
    </tr>
  )
}
