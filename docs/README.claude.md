<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Claude 网页版与 Desktop：上传自定义 Skill

Claude 网页版和 Claude Desktop 通过 ZIP 上传自定义 Skill。该方式与 Claude Code 本地目录安装相互独立。

## 使用条件

Claude 帮助中心列出的自定义 Skill 上传适用于 Pro、Max、Ultra、Team 和 Enterprise 计划，并要求启用代码执行功能。Team/Enterprise 的组织共享受管理员设置控制；个人上传的 Skill 默认由个人使用。

## 准备 ZIP

从 Gitee 克隆仓库：

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
```

将 `skills/kaoyan-english-grader/` 目录内的文件打包。ZIP 根部应直接包含：

```text
SKILL.md
references/
├── english1_essay_major.md
├── english1_essay_minor.md
├── english1_translation.md
├── english2_essay_major.md
├── english2_essay_minor.md
└── english2_translation.md
```

保持 `SKILL.md` 与 `references/` 同级。

## 在 Claude 中上传

1. 打开 Claude 网页版或 Desktop。
2. 进入 **Customize → Skills**。
3. 点击 **+ → Create skill → Upload a skill**。
4. 上传 ZIP 并等待导入。
5. 在 Skills 列表确认技能出现，并启用开关。

组织策略关闭自定义 Skill 或代码执行时，联系组织管理员。

## 使用与验证

在新对话中输入：

```text
请使用考研英语 AI 批改技能，按英语一翻译规则批改下面的译文。
```

再测试英语二图表作文。检查分值、评分依据和题型引用，确认六份规则完整。

## 更新与移除

更新时重新打包最新版本并上传，按管理页流程替换旧版本。移除前核对名称，再关闭或删除对应技能。

## 与 Claude Code 的区别

| 产品 | 安装方式 | 管理位置 |
| --- | --- | --- |
| Claude 网页版/Desktop | Customize → Skills 上传 ZIP | Claude 账号的 Skill 管理页 |
| Claude Code | 用户级或项目级目录安装 | 本机文件系统 |

两种安装副本分别管理，不会自动同步。

## 官方资料

- [Claude：使用 Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Claude：创建自定义 Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Claude Code：Agent Skills 概览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
