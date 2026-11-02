<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 考研英语 AI 批改

面向考研英语备考的跨平台 AI 批改 Skill，覆盖英语一、英语二的翻译、大作文和小作文，共六类题型。支持 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Antigravity、Kimi Code、Trae、Qoder 等 Agent，并提供豆包、WorkBuddy、千问办公等国内平台的导入指南。

> **评分说明：** 本项目提供基于练习评分参考的模拟评价，不是官方阅卷标准、官方采分点或真实考试分数预测。所有评分仅供备考训练使用。

## 功能一览

- **六类题型独立批改：** 英语一、英语二的翻译、大作文、小作文分别使用独立规则。
- **先审题，再评分：** 作文优先核查题目要求、交际任务、图画寓意或图表信息，再评价语言和结构。
- **强化切题检查：** 识别主题偷换、论证空泛、任务遗漏，以及看似相关但没有回应题目的内容。
- **翻译模拟采分：** 按句子或意群划分模拟采分点，解释每项得分和失分，不冒充官方评分细则。
- **区分错误与优化：** 使用【必须修改】和【可选优化】标注问题，保留正确、自然、有效的简单表达。
- **完整修改与复盘：** 提供逐句讲解、修改后全文、实用表达积累和针对性练习建议。
- **支持手写图片：** 先转录再批改；无法辨认的内容会请求确认，不将识别错误当成考生错误。
- **跨平台使用：** 采用标准 Agent Skill 结构，评分规则集中维护，不依赖特定编辑器。

## 支持的题型

| 考试 | 题型 | 满分 | 规则文件 |
|---|---|---:|---|
| 英语一 | 大作文（B 节） | 20 分 | [英语一大作文](skills/kaoyan-english-grader/references/english1_essay_major.md) |
| 英语一 | 小作文（A 节） | 10 分 | [英语一小作文](skills/kaoyan-english-grader/references/english1_essay_minor.md) |
| 英语一 | 翻译（5 个划线句） | 10 分 | [英语一翻译](skills/kaoyan-english-grader/references/english1_translation.md) |
| 英语二 | 大作文（通常为图表作文） | 15 分 | [英语二大作文](skills/kaoyan-english-grader/references/english2_essay_major.md) |
| 英语二 | 小作文 | 10 分 | [英语二小作文](skills/kaoyan-english-grader/references/english2_essay_minor.md) |
| 英语二 | 翻译 | 15 分 | [英语二翻译](skills/kaoyan-english-grader/references/english2_translation.md) |

## 安装

### 国内推荐：使用 Gitee 镜像

国内网络环境优先使用 Gitee 镜像安装。需要 Node.js 22.20 或更高版本。

**直接安装：**

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git --skill kaoyan-english-grader
```

根据提示选择目标 Agent，以及项目级或用户级安装范围。

**指定多个 Agent：**

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  -a claude-code \
  -a codex \
  -a cursor \
  -a opencode \
  -a gemini-cli \
  -a antigravity \
  -a kimi-code-cli \
  -a qoder \
  -a trae-cn \
  -a qwen-code \
  -a github-copilot \
  -a trae \
  -a windsurf \
  -a cline
```

**网络环境不支持直接安装时，先克隆再从本地安装：**

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
cd kaoyan-english-grader
npx skills add . --skill kaoyan-english-grader
```

添加 `-g` 参数可安装到用户级目录。通用技能安装工具支持任意 Git URL，详见[命令文档](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)。

### 备用：从 GitHub 安装

```bash
npx skills add https://github.com/Swcmb/kaoyan-english-grader.git --skill kaoyan-english-grader
```

### 使用平台原生安装方式

| 平台 | 安装方式 |
|---|---|
| Claude Code | 添加插件市场并安装插件，或使用通用技能安装工具 |
| Codex | 添加插件市场后，在 /plugins 中安装；也可作为独立 Skill 安装 |
| Cursor | 安装本地插件，或使用通用技能安装工具 |
| OpenCode | 原生发现 Agent Skill，或使用通用技能安装工具 |
| Gemini CLI | 通过扩展命令安装 |
| Qwen Code | 通过扩展命令安装 |
| Antigravity | 通过插件命令安装 |
| Kimi Code | 通过 /plugins install 安装插件 |
| Trae / TraeCode | 通过 Skills CLI 安装，或在「设置 → 技能与命令」导入 `SKILL.md` / ZIP |
| Qoder | 通过 Skills CLI 安装，或放入用户级/项目级 Skills 目录 |
| 豆包工作任务模式 | 通过工作任务模式创建自定义技能；开发者可通过开放平台提交 ZIP 技能包，个人本地文件导入以客户端版本为准 |
| 腾讯元宝 | 支持安装技能市场中的服务技能；普通用户端未确认可直接导入本仓库的 `SKILL.md` |
| WorkBuddy | 通过「专家·技能·连接器」导入本地技能包；手机端可经 SkillHub 获取技能 |
| 千问办公（QwenWork） | 通过「扩展 → 技能」上传 `SKILL.md` 及辅助文件，或在对话中搜索安装 |

各平台的完整步骤：

- [国内平台与手机端 Skill 安装指南](docs/README.domestic-platforms.md)
- [通用技能安装工具（含 Gitee 国内源）](docs/README.skills-cli.md)
- [Claude Code](docs/README.claude-code.md)
- [Codex](docs/README.codex.md)
- [Cursor](docs/README.cursor.md)
- [Gemini CLI 与 Qwen Code](docs/README.gemini-cli.md)
- [OpenCode](docs/README.opencode.md)
- [Antigravity](docs/README.antigravity.md)
- [Kimi Code](docs/README.kimi-code.md)

不同平台的原生插件市场可能要求其支持的仓库托管平台。手机 App 中的技能市场通常只提供平台技能安装，和导入任意第三方 `SKILL.md` 是两种能力；各产品的支持边界与手机端入口见[国内平台与手机端指南](docs/README.domestic-platforms.md)。国内网络环境优先使用上面的 Gitee 通用 Skill 安装方式。

## 使用方法

安装后，直接告诉 Agent 考试类型和题型，并提供题目及自己的作答。也可以上传题目、图画、图表、手写作文或译文的清晰图片。

**英语一大作文**

```text
请批改我的考研英语一大作文。
题目及图画：……
我的作文：……
```

**英语一小作文**

```text
请批改我的考研英语一小作文。
题目及写作要求：……
我的作文：……
```

**英语一翻译**

```text
请批改英语一翻译，共 5 个划线句。
英文原文及上下文：……
我的译文：……
参考译文：……（可选）
```

**英语二大作文**

```text
请批改我的考研英语二图表大作文。
题目及写作要求：……
图表：……
我的作文：……
```

**英语二小作文**

```text
请批改我的考研英语二小作文。
题目及写作要求：……
我的作文：……
```

**英语二翻译**

```text
请批改我的考研英语二翻译。
英文原文：……
我的译文：……
参考译文：……（可选）
```

## 项目结构

```text
kaoyan-english-grader/
├── skills/
│   └── kaoyan-english-grader/
│       ├── SKILL.md
│       └── references/
│           ├── english1_essay_major.md
│           ├── english1_essay_minor.md
│           ├── english1_translation.md
│           ├── english2_essay_major.md
│           ├── english2_essay_minor.md
│           └── english2_translation.md
├── .claude-plugin/
├── .codex-plugin/
├── .cursor-plugin/
├── .antigravity-plugin/
├── .agents/plugins/marketplace.json
├── plugin.json
├── gemini-extension.json
├── kimi.plugin.json
├── GEMINI.md
├── COPYING
├── docs/
│   ├── github-content-writing.md
│   ├── third-party-license-review.md
│   └── README.*.md
├── LICENSE
└── README.md
```

规范 Skill 位于 `skills/kaoyan-english-grader`，六份题型规则放在其 `references` 目录中。平台清单负责让不同 Agent 发现和安装同一份技能内容。

## 评分原则与边界

1. 各题型以对应规则文件为准，不混用英语一、英语二的分值和评分档位。
2. 作文的内容、语言、结构等权重属于辅助判断，不是官方固定扣分表，也不机械换算。
3. 翻译采分点属于模拟划分，用于解释得分依据，不代表官方采分点。
4. 缺少题目、上下文或图表时，明确说明评价边界；能判断的部分可以继续批改。
5. 不猜测模糊手写内容，不编造图表数据、题目要求、事实或因果关系。
6. 同一错误不重复扣分；正确但可以优化的表达不直接判错。

## 参与贡献

提交 Issue、Pull Request 或维护技术文档时，遵循以下规范：

- [GitHub 内容写作与 Markdown 排版规范](docs/github-content-writing.md)
- [第三方内容与许可证审查规范](docs/third-party-license-review.md)

涉及复制、改编、翻译或再分发第三方材料时，先完成文件级授权审查，再进行修改和发布。

## 许可证

本仓库原创内容采用 [GNU 通用公共许可证 v3.0 或更高版本（GPL-3.0-or-later）](LICENSE)，完整文本同时保存在 [COPYING](COPYING)。今后引入的第三方文件如采用独立许可证，将保留其文件级标识、许可证文本和适用的 NOTICE。

