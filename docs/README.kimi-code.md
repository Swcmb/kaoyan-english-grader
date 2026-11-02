<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Kimi Code CLI：安装与使用

Kimi Code CLI 支持标准 Agent Skills，也提供插件系统。本仓库的标准 Skill 目录和插件清单是两种独立安装对象。国内网络优先使用 Gitee 安装标准 Skill。

## 通过 Skills CLI 安装

在项目目录执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent kimi-code-cli
```

用户级安装增加 `-g`。

## 手动安装目录

| 范围 | 路径 |
| --- | --- |
| 用户级 Kimi 专属 | `~/.kimi-code/skills/kaoyan-english-grader/` |
| 用户级通用 | `~/.agents/skills/kaoyan-english-grader/` |
| 项目级 Kimi 专属 | `.kimi-code/skills/kaoyan-english-grader/` |
| 项目级通用 | `.agents/skills/kaoyan-english-grader/` |

Kimi Code CLI 按 Project → User 优先级加载。默认 `KIMI_CODE_HOME` 为 `~/.kimi-code`；修改该变量会移动 Kimi 专属用户目录，通用目录不随之迁移。

## 通过 Kimi 插件安装

仓库提供 Kimi 插件清单。插件命令使用 GitHub URL：

```text
/plugins install https://github.com/Swcmb/kaoyan-english-grader
/plugins list
/reload
```

插件安装范围为用户管理目录，与独立 Skill 的项目级/用户级目录不同。更新后按当前版本执行 `/plugins reload` 或开启新会话。插件入口使用 GitHub URL；需要 Gitee 源时使用 Skills CLI。

## 验证、更新与卸载

使用 `/plugins list` 检查插件；独立 Skill 使用 `/skill:kaoyan-english-grader` 调用，或直接提交批改任务。分别测试英语一翻译和英语二大作文，确认对应引用文件可读。

Skills CLI 安装使用 `npx skills update`。插件通过 Kimi 插件管理命令更新或重装。卸载时只移除对应 Skill 或插件条目。

## 官方资料

- [Kimi Code：Using Skills](https://www.kimi.ai/help/plugins-and-skills/use-skills-in-code)
- [Kimi Code：Plugins 命令](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/plugins.html)
- [Skills CLI：Kimi Code CLI 目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
