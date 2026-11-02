<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Google Antigravity：安装与使用

Antigravity 支持 Agent Skills，并提供 App、IDE 与 CLI 工作流。项目级目录适合随项目共享；用户级目录用于跨工作区复用。

## 安装标准 Skill

### 使用 Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent antigravity
```

用户级安装增加 `-g`。

### 手动安装

将完整的 `skills/kaoyan-english-grader/` 复制到：

| 范围 | 路径 |
| --- | --- |
| 项目级通用 | `.agents/skills/kaoyan-english-grader/` |
| 用户级 Antigravity | `~/.gemini/antigravity/skills/kaoyan-english-grader/` |

Skills CLI 的 Antigravity 目标使用 `~/.gemini/antigravity/skills/`。Antigravity CLI 另有独立的 `~/.gemini/antigravity-cli/skills/` 路径；不要假设 App/IDE 与 CLI 自动共享目录。跨端共享时优先使用项目级通用目录，并按当前客户端文档核对发现范围。

## 作为插件安装

仓库提供 Antigravity 插件清单。插件命令使用 GitHub 地址：

```bash
agy plugin install https://github.com/Swcmb/kaoyan-english-grader
agy plugin list
```

本地克隆后可以先验证：

```bash
agy plugin validate --strict ./kaoyan-english-grader
agy plugin install ./kaoyan-english-grader
```

标准 Skill 可通过 Gitee/Skills CLI 安装；插件命令使用官方支持的 GitHub URL 或本地目录。

## 验证、更新与卸载

在 App/IDE 的 Agent 侧边栏打开 Customizations，检查技能列表。若当前 CLI 支持重新扫描，可按官方命令 reload。分别测试英语一翻译和英语二大作文，确认对应引用文件可读。

Skills CLI 安装使用 `npx skills update kaoyan-english-grader`。插件使用 `agy plugin` 管理命令更新或重新安装。卸载时只移除本技能对应目录或插件。

## 参考资料

- [Google Antigravity：Agent Skills](https://antigravity.google/docs/skills?app=antigravity)
- [Google Antigravity：Plugins](https://www.antigravity.google/docs/plugins)
- [Skills CLI：Antigravity 目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
