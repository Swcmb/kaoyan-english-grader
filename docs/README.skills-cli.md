<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 使用 Skills CLI 安装考研英语批改 Skill

Skills CLI 可以从 Git 仓库读取标准 Agent Skill，并写入目标 Agent 的项目级或用户级技能目录。本仓库优先提供 Gitee 安装源，适合国内网络环境。

## 1. 环境要求

- Node.js：22.20 或更高版本。
- Git：能够访问目标仓库。
- 目标 Agent：已安装并能读取其 Skills 目录。

先检查环境：

~~~bash
node --version
npm --version
git --version
~~~

Node.js 版本低于要求时，先升级 Node.js，再执行安装。

## 2. 一条命令安装

默认交互式安装：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git
~~~

只安装本仓库的批改技能：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
~~~

命令运行后，按交互提示选择 Agent、安装范围和复制/链接策略。不要只看命令退出码；安装后还要在目标 Agent 中确认技能是否发现。

## 3. 指定 Agent 安装

在项目根目录打开终端，执行以下命令。每个 -a 参数对应一个目标 Agent：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  -a claude-code \
  -a codex \
  -a cursor \
  -a opencode \
  -a gemini-cli \
  -a antigravity \
  -a kimi-code-cli \
  -a qwen-code \
  -a qoder \
  -a trae-cn \
  -a openclaw
~~~

如果只需要一个产品，把上面其他 -a 参数删除即可。Skills CLI 的 Agent 标识和目录映射可能随版本增加；完整清单以其官方 agents 文档为准。

## 4. 项目级与用户级安装

**项目级**技能只对当前项目生效，适合团队共享。进入目标项目目录后执行普通安装命令：

~~~bash
cd /path/to/your/project
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  -a codex
~~~

**用户级**技能对当前用户的多个项目生效，增加 -g：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  -a codex \
  -g
~~~

项目级和用户级路径由所选 Agent 决定。例如 Codex 使用项目级 .agents/skills/ 与用户级 ~/.agents/skills/；Claude Code 使用项目级 .claude/skills/ 与用户级 ~/.claude/skills/。

## 5. 从本地克隆安装

网络环境无法稳定访问 Gitee Git 地址时，可以先克隆，再安装本地目录：

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
~~~

从本地安装可以让 CLI 交互选择目标 Agent。若只给指定 Agent 安装，追加对应 -a 参数。

备用 GitHub 源：

~~~bash
git clone https://github.com/Swcmb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
~~~

## 6. 安装结构与引用文件

CLI 应安装 skills/kaoyan-english-grader 这一整个技能目录。安装后的结构必须保持：

~~~text
kaoyan-english-grader/
├── SKILL.md
└── references/
    ├── english1_essay_major.md
    ├── english1_essay_minor.md
    ├── english1_translation.md
    ├── english2_essay_major.md
    ├── english2_essay_minor.md
    └── english2_translation.md
~~~

这六份引用规则决定题型对应的分值、评价维度、采分点和修改流程。只安装 SKILL.md 会造成规则不完整。

## 7. 查看、更新和卸载

查看命令：

~~~bash
npx skills list
~~~

更新已安装技能：

~~~bash
npx skills update
~~~

更新后在目标 Agent 中启动新会话并重新验证。卸载时使用 Skills CLI 的移除/管理交互，或删除对应安装目录下的 kaoyan-english-grader 文件夹。删除前确认路径，避免影响同目录其他技能。

## 8. 安装故障排查

| 现象 | 检查方法 |
|---|---|
| Node.js 版本不满足 | 执行 node --version，升级到 22.20 或更高版本 |
| Git 克隆失败 | 检查 Gitee 网络连接；使用先 clone 再本地安装方式 |
| CLI 没有识别目标 Agent | 使用最新 Skills CLI，查看 agents 清单中的 agent id |
| Agent 没有发现 Skill | 检查目标目录是否存在 kaoyan-english-grader/SKILL.md |
| 批改时找不到题型规则 | 检查 references/ 六个 Markdown 文件是否完整保留 |
| 安装后仍使用旧规则 | 开启新会话或重新加载技能，并检查当前安装路径 |

## 9. 平台原生导入入口

有些平台可以直接上传 ZIP 或 SKILL.md，不需要使用 CLI：

- [Claude 网页版 / Desktop](README.claude.md)：Customize → Skills → Create skill → Upload a skill。
- [Qoder IDE](README.qoder.md)：Extensions → Skills → Add Skills → Upload Skill。
- [Trae](README.trae.md)：设置 → 技能与命令 → 创建 → 导入本地技能。
- [WorkBuddy](README.workbuddy.md)：专家·技能·连接器 → 添加技能 → 上传技能。
- [千问办公](README.qwenwork.md)：扩展 → 技能 → 添加 → 上传技能。

使用原生导入时，推荐将 SKILL.md 和 references/ 六份文件打包在同一个 ZIP 中。

## 官方资料

- [Skills CLI：命令文档](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Skills CLI：支持的 Agent 与目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [Node.js 官方下载](https://nodejs.org/en/download)
