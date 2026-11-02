<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Claude 网页版与 Desktop：上传自定义 Skill

Claude 网页版和 Desktop 的自定义 Skill 上传由账号内 Skills 管理界面完成，与 Claude Code 本地目录安装相互独立。

## 安装与使用

### 准备 ZIP

将 `skills/kaoyan-english-grader/` 整个目录打包，ZIP 内保留该目录作为根目录：

```text
kaoyan-english-grader.zip
└── kaoyan-english-grader/
    ├── SKILL.md
    └── references/
        ├── english1_essay_major.md
        ├── english1_essay_minor.md
        ├── english1_translation.md
        ├── english2_essay_major.md
        ├── english2_essay_minor.md
        └── english2_translation.md
```

### 上传

1. 打开 Claude 网页版或 Desktop。
2. 进入 **Customize → Skills**。
3. 点击 **+ → Create skill → Upload a skill**。
4. 上传 ZIP，等待导入完成。
5. 在 Skills 列表确认技能出现并启用。

## 能力边界

自定义 Skill 上传的账号计划、代码执行设置和组织策略以当前帮助中心及账号界面为准。ZIP 必须保留主文件和引用目录。Claude Code 的本地 Skill 目录由另一套机制管理。

## 验收

检查技能是否出现在目标产品中，并分别测试英语一翻译和英语二大作文。核对题型路由、评分档位、引用规则和输出要求。上传或保存成功不能替代真实任务验证。

## 官方资料

- [Claude：使用 Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Claude：创建自定义 Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Claude Code：Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
