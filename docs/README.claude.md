<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Claude 网页版与 Claude Desktop：导入自定义 Skill

Claude 的消费级应用支持以 ZIP 上传自定义 Skill。此入口与 Claude Code 的本地目录安装方式不同。

## 适用条件

官方帮助中心列出的自定义 Skill 上传适用于 Pro、Max、Ultra、Team 和 Enterprise 计划，并要求启用代码执行功能。Team/Enterprise 的组织共享还受组织管理设置影响；个人上传的 Skill 默认归个人使用。

## 准备 ZIP

从 Gitee 克隆仓库：

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
~~~

将以下目录内容打包为 ZIP：

~~~text
kaoyan-english-grader/
├── SKILL.md
└── references/
    ├── english1_essay_major.md
    ├── english1_essay_minor.md
    ├── english1_translation.md
    ├── english2_essay_major.md
    ├── english2_essay_minor.md
    └── english2_translation.md
~~~

建议 ZIP 根部直接包含 SKILL.md 和 references/，确保 Claude 导入后仍能读取相对路径文件。

## 在 Claude 中上传

1. 打开 Claude 网页版或 Claude Desktop。
2. 在左侧点击 **Customize**。
3. 进入 **Skills**。
4. 点击 **+**，选择 **Create skill**。
5. 选择 **Upload a skill**。
6. 上传准备好的 ZIP。
7. 等待技能导入，在 Skills 列表中确认技能已出现。
8. 检查技能开关处于启用状态。

若组织管理员关闭了自定义 Skill 或代码执行功能，先联系组织管理员确认计划和策略权限。

## 使用与验证

在新对话输入：

~~~text
请使用考研英语 AI 批改技能，按英语一翻译规则批改下面的译文。
~~~

再单独测试英语二图表作文。检查评分依据、分值和题型引用是否正确。该验证尤其重要，因为本 Skill 依赖 references/ 中的辅助文件。

## 更新与移除

更新时重新打包最新版本并上传；在 Skills 管理页关闭或移除旧技能，再确认新技能处于启用状态。删除技能前确认目标名称。

## 与 Claude Code 的区别

- Claude 网页版/Desktop：在 Customize → Skills 上传 ZIP。
- Claude Code：把 Skill 文件夹放在 ~/.claude/skills/ 或项目级 .claude/skills/。
- 两条安装路径管理的技能副本相互独立，不会自动同步。

## 官方资料

- [Claude：使用 Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Claude：创建自定义 Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Claude Code：Agent Skills 概览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
