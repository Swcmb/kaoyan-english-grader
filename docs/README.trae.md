<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Trae / Trae CN 安装与使用

Trae 支持以 SKILL.md 定义的技能，并提供全局、项目两种安装范围。官方 IDE 文档展示了本地导入和技能市场安装流程。

## 方式一：通过 Gitee 与 Skills CLI 安装

在项目根目录打开终端：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent trae-cn
~~~

默认安装到项目级 .trae/skills/。添加 -g 安装到用户级 ~/.trae-cn/skills/：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent trae-cn \
  -g
~~~

## 方式二：通过 Trae IDE 导入

1. 在 Trae 中打开 **设置 → 技能与命令**。
2. 在“技能”区域选择 **创建**。
3. 选择技能范围：全局或项目。
4. 选择“导入本地技能”。
5. 上传包含 SKILL.md 的文件；需要保留本仓库引用规则时，上传完整技能 ZIP。
6. 检查自动识别的名称、描述和指令，确认创建。

本仓库 ZIP 的根目录应包含 SKILL.md 和 references/：

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

压缩时可将上述目录内容直接放在 ZIP 根目录，也可以保留最外层目录；导入后应检查 Trae 最终生成的技能目录中是否存在 references/。

## 方式三：手动安装

| 作用范围 | 路径 |
|---|---|
| 项目级 | .trae/skills/kaoyan-english-grader/ |
| 用户级 macOS/Linux | ~/.trae-cn/skills/kaoyan-english-grader/ |
| 用户级 Windows | %USERPROFILE%/.trae-cn/skills/kaoyan-english-grader/ |

将整个目录放到目标位置，不要只放 SKILL.md。

## 验证

1. 打开设置 → 技能与命令，分别查看全局或项目技能列表。
2. 在 Agent 对话中输入 /，检查技能是否出现。
3. 执行英语一翻译和英语二大作文测试，确认引用规则文件可读取。

## 模式与版本说明

当前公开的 Trae IDE 技能文档描述的是设置、导入、项目/全局目录和技能市场流程，没有将基础 Skill 能力限定为 SOLO 模式。不同客户端产品线（TraeCode、TraeWork）和版本的菜单可能不同，应以当前客户端的技能管理页面为准。

## 官方资料

- [Trae：技能（Skill）](https://docs.trae.cn/ide_skills)
- [Skills CLI：Trae 与 Trae CN 路径](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
