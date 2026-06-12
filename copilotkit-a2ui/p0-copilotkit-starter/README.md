# p0-copilotkit-starter · CopilotKit v2 + Next.js

W1–W2 专用。跑通 **Runtime + Provider + CopilotChat**。

## 初始化

```bash
# 推荐（A2UI 模板）
npx copilotkit@latest create p0-copilotkit-starter --framework a2ui

# 或在 monorepo 内手动
cd copilotkit-a2ui/p0-copilotkit-starter
pnpm install
cp ../.env.example .env.local
pnpm dev
```

## 最小文件清单

```
p0-copilotkit-starter/
├── app/
│   ├── layout.tsx              # CopilotKitProvider
│   ├── page.tsx                # CopilotChat
│   └── api/copilotkit/route.ts # createCopilotRuntimeHandler
├── .env.local
└── package.json
```

## layout 要点

```tsx
import { CopilotKitProvider } from "@copilotkit/react";

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <CopilotKitProvider runtimeUrl="/api/copilotkit">
          {children}
        </CopilotKitProvider>
      </body>
    </html>
  );
}
```

## 实验目录

```
experiments/
├── 01-sse-network.md       # DevTools 看 AG-UI 事件
├── 02-sidebar-layout.md
└── 03-env-audit.md         # 确认无 Key 泄漏到 client
```

## 验收

见 `../LEARNING_PLAN.md` P0。

## 通过后

W3：`../p1-ag-ui-app`
