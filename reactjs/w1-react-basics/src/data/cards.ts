import type { CardItem } from '../types/card'

export const LEARNING_CARDS: CardItem[] = [
  {
    id: 1,
    title: '组件思维',
    description: 'UI 是状态的函数。用 Props 输入、JSX 输出，单向数据流。',
    tags: ['React', 'P0'],
    accent: 'indigo',
  },
  {
    id: 2,
    title: 'Tailwind 布局',
    description: 'utility-first：在 JSX 里用 class 组合 Flex/Grid，快速搭响应式页面。',
    tags: ['CSS', 'Tailwind'],
    accent: 'emerald',
  },
  {
    id: 3,
    title: 'TypeScript Props',
    description: 'interface 描述 Props，联合类型表达变体，避免 any。',
    tags: ['TS', '类型'],
    accent: 'amber',
  },
  {
    id: 4,
    title: 'Vue 迁移',
    description: '没有 v-model：表单用受控组件。没有 watch：优先事件与派生值。',
    tags: ['Vue', '对比'],
    accent: 'rose',
  },
]
