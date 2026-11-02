<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Qoder 安装与使用

Qoder IDE 与 Qoder CLI 支持标准 Agent Skills。可通过 Skills CLI、IDE 本地上传或目录放置安装。

## 方式一：通过 Gitee 与 Skills CLI 安装

在 Qoder IDE 终端或 Qoder CLI 中执行：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent qoder
~~~

默认安装到项目级 .qoder/skills/。添加 -g 可安装到用户级 ~/.qoder/skills/：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent qoder \
  -g
~~~

## 方式二：通过 Qoder IDE 上传

1. 打开 Qoder IDE。
2. 进入 **Extensions → Skills**。
3. 选择 **Add Skills → Upload Skill**。
4. 上传本仓库完整技能 ZIP；也可以上传单个 SKILL.md。
5. 等待导入完成，在 Installed 列表中确认技能出现。

本仓库必须使用包含辅助文件的 ZIP。只上传 SKILL.md 会遗漏六份题型规则。

ZIP 内容应保持：

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

## 方式三：手动放置

| 作用范围 | 路径 |
|---|---|
| 用户级 | ~/.qoder/skills/kaoyan-english-grader/ |
| 项目级 | .qoder/skills/kaoyan-english-grader/ |

Qoder 也会发现 ~/.agents/skills/ 中的用户级技能。项目级和用户级同名时，项目级技能优先。

## 验证与调用

1. 在 Extensions → Skills → Installed 中检查技能。
2. 在新任务输入框中输入 /，检查 kaoyan-english-grader 是否出现在建议列表。
3. 调用技能进行英语一翻译批改。
4. 再提交英语二大作文，确认 Agent 读取了正确的 references 文件。

Qoder CLI 若已运行，可按当前版本执行 /skills reload；IDE 导入后也可以开启新任务重新加载技能。

## 安全与权限

导入前检查技能说明、脚本和引用资源。第三方 Skill 可能包含可执行脚本或外部请求；本仓库核心内容是 Markdown 规则文件，仍应检查实际下载包并确认来源。

## 官方资料

- [Qoder IDE：Skills](https://docs.qoder.com/extensions/skills)
- [Qoder CLI：Skills](https://docs.qoder.com/cli/Skills)
- [Skills CLI：Qoder 安装目录](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
