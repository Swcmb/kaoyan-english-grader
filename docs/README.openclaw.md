<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# OpenClaw：安装与使用

OpenClaw 支持标准 Agent Skills。Skill 可安装到当前工作区或本机全局目录，实际运行在 OpenClaw Gateway/Agent 所在主机。手机消息渠道主要提供远程交互入口。

## 从 Gitee 克隆并安装

OpenClaw 本地目录安装要求源目录根部直接包含 `SKILL.md`。本仓库将技能放在 `skills/` 子目录，因此需要指定该目录：

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
openclaw skills install ./skills/kaoyan-english-grader
```

默认安装到当前工作区的 `skills/kaoyan-english-grader/`。

全局安装：

```bash
openclaw skills install ./skills/kaoyan-english-grader --global
```

全局目录为 `~/.openclaw/skills/`。若 Agent 配置了技能 allowlist，还需确认本 Skill 在允许列表中。

## 使用 Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent openclaw
```

用户级安装按 CLI 当前版本增加全局选项，并检查 OpenClaw 实际读取的目录。

## 检查与调用

```bash
openclaw skills list
openclaw skills check
openclaw skills info kaoyan-english-grader
```

在消息渠道提交批改任务，并分别测试英语一翻译和英语二图表作文。确认 Agent 能读取 `references/english2_essay_major.md` 等对应文件。

工作区安装时，确认当前 Agent 使用同一工作区；全局安装时检查 `agents.defaults.skills` 或 `agents.entries` 的技能可见性设置。

## 更新与卸载

本地目录安装不属于 ClawHub 跟踪安装，`openclaw skills update` 不会自动从 Gitee 拉取。更新流程：

1. 进入仓库执行 `git pull`。
2. 重新安装工作区副本：

   ```bash
   openclaw skills install ./skills/kaoyan-english-grader --force
   ```

3. 全局副本按需增加 `--global`，并确认目标路径。
4. 执行 `openclaw skills list` 与 `openclaw skills check` 验证。

卸载时只删除相应作用范围下的 `kaoyan-english-grader/`。

## 手机端与安全

手机连接 Gateway 后，调用的是主机上已加载的 Skill，不是在手机 App 本地安装。Android Termux 自托管属于独立部署，需要单独核对 OpenClaw 安装要求和 Android 兼容性。

安装前检查来源、`SKILL.md`、脚本、网络请求和文件访问范围。不要为了跳过未知风险提示而盲目使用 `--force`。本仓库核心规则是 Markdown 文件，仍需检查实际下载内容。

## 官方资料

- [OpenClaw：Skills 系统与安装](https://docs.openclaw.ai/skills)
- [OpenClaw：Skills CLI](https://docs.openclaw.ai/cli/skills)
- [OpenClaw：Skills 安全与自动化 FAQ](https://docs.openclaw.ai/help/faq/skills-and-automation)
- [Skills CLI：OpenClaw 目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
