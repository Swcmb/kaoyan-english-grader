<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Kimi Code 安装与使用

Kimi Code CLI 支持标准 Agent Skills，也支持通过插件系统安装仓库插件。国内网络优先使用 Gitee + Skills CLI。

## 方式一：通过 Gitee 安装标准 Skill

在项目目录执行：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent kimi-code-cli
~~~

默认安装到项目级通用 .agents/skills/。添加 -g 安装到用户级：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent kimi-code-cli \
  -g
~~~

## 方式二：手动安装

Kimi Code CLI 支持以下目录：

| 作用范围 | 路径 |
|---|---|
| 用户级 Kimi 专属目录 | ~/.kimi-code/skills/kaoyan-english-grader/ |
| 用户级通用目录 | ~/.agents/skills/kaoyan-english-grader/ |
| 项目级 Kimi 专属目录 | .kimi-code/skills/kaoyan-english-grader/ |
| 项目级通用目录 | .agents/skills/kaoyan-english-grader/ |

如果设置了 KIMI_CODE_HOME，Kimi 专属用户目录会随该变量变化；通用 ~/.agents/skills/ 不随其迁移。

## 方式三：通过 Kimi 插件安装

本仓库提供 Kimi 插件清单。插件路径使用 GitHub 仓库地址：

~~~text
/plugins install https://github.com/Swcmb/kaoyan-english-grader
/plugins list
/reload
~~~

插件安装到用户管理目录并对所有项目生效，目前插件安装范围与独立 Skill 的项目级/用户级目录不同。插件修改后执行 /plugins reload 或开启新会话。此插件入口使用 GitHub URL；如需 Gitee 源，请使用前面的 Skills CLI。

## 验证

1. 运行 /plugins list 检查插件，或在 / 技能列表中检查 kaoyan-english-grader。
2. 请求批改英语一翻译，确认能读取英语一翻译规则。
3. 请求批改英语二图表作文，确认能读取英语二大作文规则。
4. 若新技能未出现，开启新会话或重载插件。

## 更新与卸载

通过 Skills CLI 安装的技能使用 npx skills update。插件通过 /plugins 管理器更新或重新安装。卸载时只删除对应的技能或插件条目。

## 官方资料

- [Kimi Code：Using Skills](https://www.kimi.ai/help/plugins-and-skills/use-skills-in-code)
- [Kimi Code：Plugins 命令](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/plugins.html)
- [Skills CLI：Kimi Code CLI 安装目录](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
