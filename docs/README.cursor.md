<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Cursor 安装与使用

Cursor 自动发现标准 Agent Skills。项目级技能适合随代码仓库共享；用户级技能保存在本机。

## 方式一：通过 Gitee 安装

在项目根目录打开 Cursor Agent 终端：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent cursor
~~~

默认安装到项目级目录。添加 -g 安装到用户级：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent cursor \
  -g
~~~

## 方式二：手动安装

将完整技能目录复制到以下任一位置：

| 作用范围 | 目录 |
|---|---|
| 项目级（通用） | .agents/skills/kaoyan-english-grader/ |
| 项目级（Cursor） | .cursor/skills/kaoyan-english-grader/ |
| 用户级（通用） | ~/.agents/skills/kaoyan-english-grader/ |
| 用户级（Cursor） | ~/.cursor/skills/kaoyan-english-grader/ |

Windows 用户可使用 %USERPROFILE%/.cursor/skills/kaoyan-english-grader/ 作为用户级 Cursor 路径。

保持 SKILL.md 与 references/ 位于同一技能目录。不要只复制主文件。

## 在 Cursor 中查看与调用

1. 打开 Cursor。
2. 在侧边栏打开 Customize → Skills。
3. 检查 kaoyan-english-grader 是否出现在列表。
4. 在 Agent 输入框中输入 /，从技能列表中选择；也可以直接描述批改任务。
5. 分别测试英语一翻译和英语二图表作文。

## Cloud Agents 注意事项

本机的 ~/.cursor/skills/ 可以通过 Settings → Agents → Sync Skills for Cloud Agents 同步到 Cloud Agents。项目级 .agents/skills/ 或 .cursor/skills/ 更适合提交到仓库，让其他环境也能发现该技能。未同步的个人技能不会自动出现在远程 Agent 或自托管 Worker 中。

## 更新与卸载

再次执行相同的 Skills CLI 安装命令，按提示更新；手动安装时替换完整技能目录。移除对应的 kaoyan-english-grader 文件夹即可卸载。

## 官方资料

- [Cursor：Agent Skills](https://cursor.com/docs/skills)
- [Cursor：管理个人 Skills 与 Cloud Agents](https://cursor.com/help/customization/skills)
