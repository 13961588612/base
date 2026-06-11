import type { Product } from '../../types/product'

interface ProductRowProps {
  product: Product
}

export function ProductRow({ product }: ProductRowProps) {
  const nameClass = product.stocked ? 'text-slate-800' : 'text-rose-600'

  return (
    <tr>
      <td className={`px-3 py-2 text-sm ${nameClass}`}>{product.name}</td>
      <td className="px-3 py-2 text-sm text-slate-600">{product.price}</td>
    </tr>
  )
}
