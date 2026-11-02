<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Gemini CLI：安装与使用

Gemini CLI 支持标准 Agent Skills，可从工作区、用户目录和扩展中加载技能。本指南对应 Gemini CLI，不是千问 App 或 QwenWork。

## 通过 Skills CLI 安装

在项目根目录运行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent gemini-cli
```

用户级安装增加 `-g`。

## 使用 Gemini CLI 原生命令

先克隆仓库：

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
```

安装到当前工作区：

```bash
gemini skills install ./skills/kaoyan-english-grader --scope workspace
```

安装到用户级：

```bash
gemini skills install ./skills/kaoyan-english-grader --scope user
```

检查安装：

```bash
gemini skills list
```

## 手动安装路径

| 范围 | 路径 |
| --- | --- |
| 项目级通用 | `.agents/skills/kaoyan-english-grader/` |
| 项目级 Gemini | `.gemini/skills/kaoyan-english-grader/` |
| 用户级通用 | `~/.agents/skills/kaoyan-english-grader/` |
| 用户级 Gemini | `~/.gemini/skills/kaoyan-english-grader/` |

复制完整目录，保留 `SKILL.md` 和 `references/`。

## 调用与验证

使用 `/skills` 查看技能，输入 `/kaoyan-english-grader` 调用，或直接提交考研英语批改任务。测试英语一翻译和英语二大作文，确认引用规则可读。

若当前会话未发现新技能，按当前版本执行 `/skills reload`（如支持）或开启新会话。

## 更新与卸载

Skills CLI 安装使用 `npx skills update`。原生命令卸载：

```bash
gemini skills uninstall kaoyan-english-grader --scope workspace
gemini skills uninstall kaoyan-english-grader --scope user
```

手动安装时，替换或删除目标路径下的 `kaoyan-english-grader/`。

## 官方资料

- [Gemini CLI：Skills 命令与管理](https://geminicli.com/docs/cli/skills/)
- [Gemini CLI：Managing Agent Skills](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md)
- [Skills CLI：Gemini CLI 目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
