<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 使用通用技能安装工具

本仓库将标准 Agent Skill 放在 `skills/kaoyan-english-grader` 目录中。通用技能安装工具可以将它安装到多种编程 Agent 的技能目录。

## 国内推荐：Gitee 镜像

国内网络环境优先使用 Gitee 镜像。需要 Node.js 22.20 或更高版本。

直接从 Gitee 安装：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader
```

根据提示选择一个或多个 Agent，以及项目级或用户级安装范围。

指定 Agent 安装：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent claude-code \
  --agent codex \
  --agent cursor \
  --agent opencode \
  --agent gemini-cli \
  --agent antigravity \
  --agent kimi-code-cli \
  --agent qoder \
  --agent trae-cn
```

网络环境无法直接访问 Gitee Git 地址时，先克隆仓库，再从本地目录安装：

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
```

添加 `-g` 参数可安装到用户级目录。

## 备用：GitHub

也可以从 GitHub 安装：

```bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader.git --skill kaoyan-english-grader
```

## 更新

```bash
npx skills update kaoyan-english-grader
```

## 支持的平台

除上面的常用 Agent 外，当前 Skills CLI 也提供 `qoder` 与 `trae-cn` 目标，可分别安装到 Qoder 和中文 Trae 的技能目录。WorkBuddy、豆包、QwenWork 等产品优先使用各自的本地技能导入入口，详见[国内平台与手机端 Skill 安装指南](README.domestic-platforms.md)。

安装工具支持的 Agent 名单会持续变化，请查看其维护文档：

[查看 Agent 支持列表](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

当前 CLI 支持任意 Git URL。Gitee 的安装方式属于标准 Git 源安装，不需要额外的 Gitee 专用 CLI。

## 验证安装

在目标 Agent 中查看已安装技能，或直接要求它批改英语一/英语二的翻译或作文。确认 Agent 能够读取对应的题型规则文件。
