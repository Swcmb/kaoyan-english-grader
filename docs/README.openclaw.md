<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# OpenClaw 安装与使用

OpenClaw 支持标准 Agent Skills。技能可以安装到当前工作区，也可以安装到所有本地 Agent 共用的全局目录。它适合有自托管 Gateway、命令行和服务器管理经验的用户。

## 方式一：从 Gitee 克隆后安装（推荐）

OpenClaw 的本地目录安装要求源目录根部直接包含 SKILL.md。本仓库把技能放在仓库的 skills/ 子目录，因此先克隆，再指定该目录。

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
openclaw skills install ./skills/kaoyan-english-grader
~~~

默认安装到当前 OpenClaw 工作区的 skills/kaoyan-english-grader/。

如需让所有本地 Agent 共用，执行：

~~~bash
openclaw skills install ./skills/kaoyan-english-grader --global
~~~

全局托管目录为 ~/.openclaw/skills/。当某个 Agent 配置了技能 allowlist 时，还需要确认 kaoyan-english-grader 在允许列表中。

## 方式二：使用 Skills CLI 安装

如果希望统一用 Skills CLI 管理多种 Agent：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent openclaw
~~~

需要用户级安装时添加 -g。安装完成后，确认实际目标路径是当前 OpenClaw 版本读取的目录。

## 验证和调用

~~~bash
openclaw skills list
openclaw skills check
openclaw skills info kaoyan-english-grader
~~~

随后在 OpenClaw 对话渠道中提交任务：

~~~text
请使用 kaoyan-english-grader 批改以下考研英语一翻译。
请按英语一翻译规则逐意群分析，并给出模拟分数和修改建议。
~~~

再提交英语二图表作文，确认技能可以读取 references/english2_essay_major.md。若技能只出现在工作区，检查当前 Agent 是否使用了同一工作区；全局安装则检查 agents.defaults.skills 或 agents.entries 的技能可见性配置。

## 更新与卸载

OpenClaw 的本地目录安装不是 ClawHub 跟踪安装，openclaw skills update 不会自动从 Gitee 拉取该本地副本。更新步骤：

1. 进入本地仓库并执行 git pull。
2. 再次执行 openclaw skills install ./skills/kaoyan-english-grader --force，覆盖工作区副本。
3. 全局安装时使用 --global，并确认目标为全局托管目录。
4. 执行 openclaw skills list 和 openclaw skills check 验证。

卸载时删除工作区 skills/ 或全局 ~/.openclaw/skills/ 下的 kaoyan-english-grader 文件夹。

## 手机端与 Gateway 的关系

OpenClaw 的 Skill 安装发生在运行 Gateway/Agent 的主机或服务器上。手机端聊天 App、消息渠道或配套客户端主要作为远程交互入口；连接到 Gateway 后，可以调用该 Agent 已加载的技能。手机端远程聊天不等同于手机本地安装 Skill。

若在 Android 上自行使用 Termux 部署 OpenClaw，需按照 OpenClaw 当前官方安装要求和 Android 环境兼容性单独配置。此方式属于自托管部署，不是面向普通用户的一键手机 App 技能安装流程。

## 安全

OpenClaw 的安装策略可能在安装过程中检查技能并提示风险。安装前检查来源、SKILL.md、引用脚本、网络请求和文件访问范围。不要使用 --force 或忽略策略警告来跳过未理解的安全问题。对本仓库而言，核心功能依赖 Markdown 规则文件；仍需检查下载的实际文件内容。

## 官方资料

- [OpenClaw：Skills 系统与安装方式](https://docs.openclaw.ai/skills)
- [OpenClaw：Skills CLI](https://docs.openclaw.ai/cli/skills)
- [OpenClaw：技能安全与自动化 FAQ](https://docs.openclaw.ai/help/faq/skills-and-automation)
- [Skills CLI：OpenClaw 目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
