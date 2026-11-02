<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# OpenClaw：安装与使用

OpenClaw 支持标准 Agent Skills。Skill 在 Gateway/Agent 所在主机加载；手机消息渠道提供远程交互入口。

## 安装与使用

### 从 Gitee 克隆并安装

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
openclaw skills install ./skills/kaoyan-english-grader
```

默认安装到当前工作区。全局安装：

```bash
openclaw skills install ./skills/kaoyan-english-grader --global
```

### 使用 Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent openclaw
```

### 检查状态

```bash
openclaw skills list
openclaw skills check
openclaw skills info kaoyan-english-grader
```

## 能力边界

本地目录安装不一定属于 ClawHub 跟踪安装，更新方式取决于来源。若 Agent 配置 allowlist，确认本 Skill 在允许列表。手机连接 Gateway 后使用的是主机 Skill，不是在手机端安装。

## 验收

检查 Agent 能发现并加载技能，再分别测试英语一翻译和英语二大作文，确认对应规则可读取、评分分值正确、输出结构完整。

## 官方资料

- [OpenClaw：Skills 系统与安装](https://docs.openclaw.ai/skills)
- [OpenClaw：Skills CLI](https://docs.openclaw.ai/cli/skills)
- [OpenClaw：Skills 安全 FAQ](https://docs.openclaw.ai/help/faq/skills-and-automation)
- [Skills CLI：Agent 映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
