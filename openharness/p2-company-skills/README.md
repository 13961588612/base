# p2-company-skills · 公司 Skills 库

W4 专用。建立 **≥3 个** 符合 `SKILL.md` 规范的公司流程技能包。

## 格式（兼容 anthropics/skills）

```
p2-company-skills/
├── README.md
└── skills/
    ├── incident-response/
    │   └── SKILL.md
    ├── release-checklist/
    │   └── SKILL.md
    └── security-baseline/
        └── SKILL.md
```

## SKILL.md 最小结构

```markdown
---
name: incident-response
description: Use when handling production incidents. Step-by-step runbook.
---

# Incident Response

## When to use
- P0/P1 alert fired
- User reports widespread outage

## Steps
1. ...
2. ...

## Do NOT
- Do not restart prod without approval
```

## 安装到 Harness

```bash
# 用户级
mkdir -p ~/.openharness/skills
cp -r skills/* ~/.openharness/skills/

# 或项目级（在 git 仓库根）
mkdir -p .openharness/skills
cp -r skills/* .openharness/skills/
```

## 验收

- [ ] `/skills` 能列出 3 个 skill 及来源
- [ ] 至少 1 个 skill 可作为 slash 命令直接调用
- [ ] README 说明版本发布流程（tag）

## 通过后

W5：`../p3-mcp-integration`
