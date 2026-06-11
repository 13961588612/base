import type { Product } from '../types/product'

export const PRODUCTS: Product[] = [
  { category: '水果', price: '$1', stocked: true, name: '苹果' },
  { category: '水果', price: '$1', stocked: true, name: '奇异果' },
  { category: '水果', price: '$2', stocked: false, name: '山竹' },
  { category: '水果', price: '$2', stocked: true, name: '榴莲' },
  { category: '蔬菜', price: '$2', stocked: true, name: '菠菜' },
  { category: '蔬菜', price: '$4', stocked: false, name: '南瓜' },
  { category: '蔬菜', price: '$1', stocked: true, name: '豌豆' },
]
