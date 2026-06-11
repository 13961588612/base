# PostgreSQL 环境约定

## 本地开发（W10 一）

```bash
# docker-compose.yml 最小配置
# services:
#   postgres:
#     image: postgres:16
#     ports: ["5432:5432"]
#     environment:
#       POSTGRES_USER: dev
#       POSTGRES_PASSWORD: dev
#       POSTGRES_DB: app
```

`.env`：

```
DATABASE_URL="postgresql://dev:dev@localhost:5432/app"
```

Prisma `schema.prisma`：

```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}
```

## 常用命令

```bash
npx prisma migrate dev --name init
npx prisma db seed          # 若配置了 seed
npx prisma studio           # 可视化浏览
```

## 生产部署（W10 日 / 作品集）

| 平台 | 说明 |
|------|------|
| [Neon](https://neon.tech) | Serverless PG，Vercel 常用 |
| [Supabase](https://supabase.com) | PG + 可选 Auth/Storage |
| Vercel Postgres | 底层 Neon，集成简单 |

上线时仅替换 `DATABASE_URL`，Prisma schema 不变。

## 学习要点（配合 CHECKLIST）

- [ ] `relation` / 外键 / `onDelete`
- [ ] 索引：何处加 `@@index`
- [ ] 原生 SQL：`$queryRaw` 仅必要时使用
- [ ] 连接池：Serverless 环境注意 `pgbouncer` / Prisma `directUrl`
