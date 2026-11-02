<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# OpenAI Codex：安装与使用

Codex 支持 Agent Skills。项目级技能随仓库共享；用户级技能可在多个工作区复用。完整安装必须保留主文件和六份题型规则。

## 安装方式

### 使用 Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent codex
```

用户级安装增加 `-g`。

### 手动安装

将完整技能目录复制到：

| 范围 | 路径 |
| --- | --- |
| 项目级 | `.agents/skills/kaoyan-english-grader/` |
| 用户级 | `~/.agents/skills/kaoyan-english-grader/` |
| Windows 用户级 | `%USERPROFILE%/.agents/skills/kaoyan-english-grader/` |

不要只复制 `SKILL.md`；`references/` 下的六份规则是批改流程的一部分。

### 通过 Codex 对话获取

```text
请从以下 Git 仓库安装考研英语批改 Skill：
https://gitee.com/ianwusb/kaoyan-english-grader.git

只安装 kaoyan-english-grader，保留 references 子目录。
安装后报告实际路径，并验证六份题型规则。
```

下载能力取决于当前环境的网络和文件权限。要求 Codex 检查实际文件，不要只凭对话回复判断成功。

## 调用与验证

开启新会话后使用 `/skills` 查看技能，或使用 `$kaoyan-english-grader` 调用。分别测试英语一翻译与英语二大作文，确认题型路由、分值和引用规则正确。

## 更新与卸载

Skills CLI 安装使用 `npx skills update kaoyan-english-grader`。手动安装时完整替换目标目录。删除项目级副本会影响使用该仓库的团队成员；删除用户级副本只影响当前用户。

## 参考资料

- [Codex：构建 Skills](https://learn.chatgpt.com/docs/build-skills)
- [Skills CLI：Agent 与目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
