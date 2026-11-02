<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 千问办公（QwenWork）安装与使用

千问办公支持从技能广场安装技能、在对话中搜索安装，也支持上传本地 SKILL.md 或 ZIP。由于本仓库依赖六份辅助规则文件，推荐 ZIP 导入。

## 方式一：上传本地 ZIP（推荐）

1. 从 Gitee 克隆项目：

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
~~~

2. 进入技能目录：

~~~text
kaoyan-english-grader/skills/kaoyan-english-grader/
├── SKILL.md
└── references/
    ├── english1_essay_major.md
    ├── english1_essay_minor.md
    ├── english1_translation.md
    ├── english2_essay_major.md
    ├── english2_essay_minor.md
    └── english2_translation.md
~~~

3. 将技能目录内容打包为 ZIP，保证 ZIP 根部可以直接看到 SKILL.md 和 references/。
4. 打开千问办公，点击左侧 **扩展 → 技能**。
5. 点击 **添加 → 上传技能**，选择 ZIP 文件。
6. 等待解析和安装完成，在“已安装”区域检查技能状态。

官方帮助中心也列出根级 skill.md 文件上传方式。对于含有多个引用文件的项目，ZIP 更适合保留目录结构。不要只上传主文件。

## 方式二：在对话中搜索安装

在千问办公对话框输入：

~~~text
请查找并安装考研英语 AI 批改 Skill。
如果技能库中没有，请告知我，不要自行创建一个不完整版本。
~~~

如果技能库找到目标技能，确认卡片信息后安装。

## 方式三：从仓库地址安装

官方文档说明可以将开源社区的仓库地址发给 QwenWork，并要求它下载到本地技能目录。Gitee 地址的可访问性取决于 QwenWork 当前运行环境；如下载失败，使用方式一上传 ZIP。

可发送：

~~~text
请从这个仓库获取考研英语批改 Skill：
https://gitee.com/ianwusb/kaoyan-english-grader.git

只安装 skills/kaoyan-english-grader 这一个技能。
必须保留 SKILL.md 和 references/ 下的全部题型规则。
完成后告诉我实际安装位置，并检查六份规则文件是否存在。
~~~

## 使用与验证

- 自动调用：直接提出“批改我的考研英语一翻译”。
- 手动调用：在输入框输入 /，从技能列表中选中本技能。
- 技能管理：在扩展 → 技能 → 已安装区域检查启用状态。

分别用英语一翻译和英语二大作文做测试，确认规则文件可以读取。

## 更新与卸载

在扩展 → 技能管理中按当前版本提供的更新/卸载操作管理。若是从本地 ZIP 导入，更新时重新打包最新技能目录再上传。删除本技能前确认选中的名称，避免误删其他技能。

## 官方资料

- [千问办公：技能帮助文档](https://qwenwork.cn/docs/features/skills)
- [阿里云帮助中心：千问办公 Skill](https://www.alibabacloud.com/help/zh/qwenwork/skills)
