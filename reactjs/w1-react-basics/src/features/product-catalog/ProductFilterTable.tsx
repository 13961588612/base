import { useMemo, useState } from 'react'
import { PRODUCTS } from '../../data/products'
import { ProductTable } from './ProductTable'
import { SearchBar } from './SearchBar'

export function ProductFilterTable() {
  const [filterText, setFilterText] = useState('')
  const [inStockOnly, setInStockOnly] = useState(false)

  const filteredProducts = useMemo(() => {
    return PRODUCTS.filter((product) => {
      if (inStockOnly && !product.stocked) return false
      const q = filterText.trim().toLowerCase()
      if (!q) return true
      return product.name.toLowerCase().includes(q)
    })
  }, [filterText, inStockOnly])

  return (
    <div className="space-y-4 rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
      <div>
        <h3 className="font-semibold text-slate-900">商品目录</h3>
        <p className="mt-1 text-sm text-slate-500">
          Thinking in React：先拆组件，state 提升到父组件，props 向下传
        </p>
      </div>
      <SearchBar
        filterText={filterText}
        inStockOnly={inStockOnly}
        onFilterTextChange={setFilterText}
        onInStockOnlyChange={setInStockOnly}
      />
      <ProductTable products={filteredProducts} />
    </div>
  )
}
