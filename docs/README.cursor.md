<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Cursor：安装与使用

Cursor 支持标准 Agent Skills。项目级技能可随仓库共享；用户级技能保存在本机，并可按同步设置用于 Cloud Agents。

## 通过 Skills CLI 安装

在项目根目录的 Cursor Agent 终端执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent cursor
```

添加 `-g` 可安装到用户级。

## 手动安装

将完整技能目录放在以下位置之一：

| 范围 | 路径 |
| --- | --- |
| 项目级通用 | `.agents/skills/kaoyan-english-grader/` |
| 项目级 Cursor | `.cursor/skills/kaoyan-english-grader/` |
| 用户级通用 | `~/.agents/skills/kaoyan-english-grader/` |
| 用户级 Cursor | `~/.cursor/skills/kaoyan-english-grader/` |
| Windows 用户级 | `%USERPROFILE%/.cursor/skills/kaoyan-english-grader/` |

保留主文件和引用目录的相对位置。

## 查看与调用

1. 打开 Cursor。
2. 进入 Customize → Skills，检查技能是否出现。
3. 在 Agent 输入框输入 `/` 并选择技能，或直接描述任务。
4. 测试英语一翻译和英语二图表作文。

## Cloud Agents

本机的 `~/.cursor/skills/` 可通过 Settings → Agents → Sync Skills for Cloud Agents 同步。项目级 `.agents/skills/` 或 `.cursor/skills/` 可随仓库共享。未同步的个人技能不会自动出现在远程 Agent 或自托管 Worker 中。

## 更新与卸载

再次运行 Skills CLI 安装命令并按提示更新，或手动替换完整目录。卸载时只删除目标范围下的 `kaoyan-english-grader/`。

## 官方资料

- [Cursor：Agent Skills](https://cursor.com/docs/skills)
- [Cursor：个人 Skills 与 Cloud Agents](https://cursor.com/help/customization/skills)
