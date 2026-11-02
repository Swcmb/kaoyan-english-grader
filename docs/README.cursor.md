<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Cursor 安装指南

本仓库包含通用插件清单 plugin.json 和 Cursor 专用清单 .cursor-plugin/plugin.json。

## 本地安装插件

克隆仓库：

~~~bash
git clone https://github.com/Swcmb/kaoyan-english-grader.git
~~~

将完整仓库复制到 Cursor 本地插件目录：

- macOS/Linux：~/.cursor/plugins/local/kaoyan-english-grader
- Windows：%USERPROFILE%\.cursor\plugins\local\kaoyan-english-grader

请保留 plugin.json、.cursor-plugin/plugin.json、skills/ 和其他仓库文件的相对位置。重启 Cursor，或执行 Developer: Reload Window，然后在 Customize 中检查插件。

## 作为独立 Skill 安装

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent cursor
~~~

添加 -g 参数可安装到用户级目录。

## 验证

要求 Cursor 批改一份考研英语作文或翻译，确认其能读取对应题型规则。
