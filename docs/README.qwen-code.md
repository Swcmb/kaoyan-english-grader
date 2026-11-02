<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Qwen Code 安装与使用

Qwen Code 原生支持 Agent Skills，可从项目目录、用户目录和扩展中发现技能。此文档对应开发者工具 Qwen Code，不是千问手机 App 或千问办公（QwenWork）。

## 方式一：通过 Gitee 安装

在项目根目录打开 Qwen Code 终端：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent qwen-code
~~~

默认安装到项目级 .qwen/skills/。添加 -g 安装到用户级：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent qwen-code \
  -g
~~~

## 方式二：手动安装

将完整技能目录复制到：

| 作用范围 | 首选目录 | 兼容目录 |
|---|---|---|
| 项目级 | .qwen/skills/kaoyan-english-grader/ | .agents/skills/kaoyan-english-grader/ |
| 用户级 | ~/.qwen/skills/kaoyan-english-grader/ | ~/.agents/skills/kaoyan-english-grader/ |

如果项目中的 .qwen/skills/ 与 .agents/skills/ 同时存在同名技能，Qwen Code 优先使用 .qwen/skills/。用户级同样优先使用 ~/.qwen/skills/。

请保留 SKILL.md 和 references/ 六份规则文件的相对位置。

## 查看和调用

1. 在 Qwen Code 中输入 /skills，查看可调用技能。
2. 输入 /kaoyan-english-grader，或直接描述批改需求。
3. 先提交英语一翻译，再提交英语二图表作文。
4. 确认 Agent 能分别读取 references/english1_translation.md 和 references/english2_essay_major.md。

如果技能没有显示，检查目录深度：必须是“技能根目录/SKILL.md”，不能把整个仓库再多嵌套一层。

## 更新与卸载

CLI 安装后执行 npx skills update。手动安装时覆盖整个技能文件夹。删除相应的 kaoyan-english-grader 目录即可卸载。

## 官方资料

- [Qwen Code：Agent Skills](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/)
- [Skills CLI：Qwen Code 目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
