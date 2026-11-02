<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# OpenAI Codex：安装与使用

Codex 支持 Agent Skills。项目级技能随仓库共享；用户级技能适用于多个项目。

## 通过 Skills CLI 安装

在目标项目目录执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent codex
```

用户级安装增加 `-g`。

## 手动安装

将完整技能目录复制到：

| 范围 | 路径 |
| --- | --- |
| 项目级 | `.agents/skills/kaoyan-english-grader/` |
| 用户级 | `~/.agents/skills/kaoyan-english-grader/` |
| Windows 用户级 | `%USERPROFILE%/.agents/skills/kaoyan-english-grader/` |

保留 `SKILL.md` 和 `references/` 六份规则，不要只复制主文件。

## 让 Codex 从仓库获取

在 Codex 对话中请求：

```text
请从以下 Git 仓库安装考研英语批改 Skill：
https://gitee.com/ianwusb/kaoyan-english-grader.git

只安装 kaoyan-english-grader，保留 references 子目录。
安装后报告实际路径，并验证六份题型规则。
```

下载能力取决于当前环境的网络和文件权限。要求 Codex 检查实际目标目录，不要只凭对话回复判断成功。

## 调用与验证

开启新会话后使用 `/skills` 查看技能，或使用 `$kaoyan-english-grader` 调用。分别测试英语一翻译与英语二大作文，确认题型路由和评分规则正确。

## 更新与卸载

CLI 安装后按 Skills CLI 流程执行 `npx skills update`。手动安装时完整替换目标目录。删除项目级副本会影响使用该仓库的团队成员；删除用户级副本只影响当前用户。

## 官方资料

- [Codex：构建 Skills](https://learn.chatgpt.com/docs/build-skills)
- [Skills CLI：Agent 与目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
