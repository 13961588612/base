import type { ReactNode } from 'react'
import type { Product } from '../../types/product'
import { ProductCategoryRow } from './ProductCategoryRow'
import { ProductRow } from './ProductRow'

interface ProductTableProps {
  products: Product[]
}

export function ProductTable({ products }: ProductTableProps) {
  const rows: ReactNode[] = []
  let lastCategory: string | null = null

  products.forEach((product) => {
    if (product.category !== lastCategory) {
      lastCategory = product.category
      rows.push(<ProductCategoryRow key={product.category} category={product.category} />)
    }
    rows.push(<ProductRow key={product.name} product={product} />)
  })

  return (
    <table className="w-full overflow-hidden rounded-lg border border-slate-200">
      <thead>
        <tr className="bg-white">
          <th className="px-3 py-2 text-left text-sm font-medium text-slate-600">名称</th>
          <th className="px-3 py-2 text-left text-sm font-medium text-slate-600">价格</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  )
}
