<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 考研英语 AI 批改与开源合规 Skills

一组面向 AI 编程助手的跨平台 Agent Skills：提供考研英语一、英语二翻译与作文六类题型的模拟批改，以及第三方代码、Skill、Prompt 和配置的许可证审查与署名完整性检查。支持通过通用技能安装工具或各 Agent 的原生插件、扩展机制安装。

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
- **第三方许可证审查：** 在复制、改编、vendor 或发布第三方内容前，核对文件级授权、许可证文本、NOTICE 和来源标识。
- **署名完整性测试：** 对第三方许可证原文、NOTICE 和改编文件的来源声明建立自动化回归测试。

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

### 方式一：使用通用技能安装工具（推荐）

需要 Node.js 22.20 或更高版本。

```bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader
```

根据提示选择目标 Agent，以及项目级或用户级安装范围。

指定多个 Agent 安装：

```bash
npx skills add Swcmb/kaoyan-english-grader \
  --skill kaoyan-english-grader \
  -a claude-code \
  -a codex \
  -a cursor \
  -a opencode \
  -a gemini-cli \
  -a antigravity \
  -a kimi-code-cli \
  -a qwen-code \
  -a github-copilot \
  -a trae \
  -a windsurf \
  -a cline
```

添加 -g 参数可安装到用户级目录。支持的 Agent 名单请查看[安装工具文档](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

### 安装第三方许可证审查 Skill

该 Skill 用于在复制、改编、翻译、vendor 或发布第三方材料前审查文件级许可证，并验证来源和署名不会在重命名、移动或重新打包时丢失。

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill check-the-licence-before-you-copy
~~~

### 方式二：使用平台原生安装方式

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

各平台的完整步骤：

- [通用技能安装工具](docs/README.skills-cli.md)
- [Claude Code](docs/README.claude-code.md)
- [Codex](docs/README.codex.md)
- [Cursor](docs/README.cursor.md)
- [Gemini CLI 与 Qwen Code](docs/README.gemini-cli.md)
- [OpenCode](docs/README.opencode.md)
- [Antigravity](docs/README.antigravity.md)
- [Kimi Code](docs/README.kimi-code.md)

不同平台的命令、插件格式和安装范围由对应平台决定。通用安装工具与原生安装方式是两条独立路径，选择其中一种即可。

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
│   ├── kaoyan-english-grader/
│   │   ├── SKILL.md
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
├── LICENSES/
│   └── Apache-2.0.txt
├── NOTICE
├── COPYING
├── tests/
│   └── test_third_party_attribution.py
├── .github/workflows/
│   └── test-third-party-attribution.yml
├── docs/
│   ├── github-content-writing.md
│   ├── third-party-license-review.md
│   └── README.*.md
└── LICENSE
```

考研英语批改 Skill 位于 skills/kaoyan-english-grader，六份题型规则放在其 references 目录中。第三方许可审查 Skill 位于 skills/check-the-licence-before-you-copy。平台清单负责让不同 Agent 发现和安装仓库中的 Skill。

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

本仓库原创内容采用 [GNU 通用公共许可证 v3.0 或更高版本（GPL-3.0-or-later）](LICENSE)，完整文本同时保存在 [COPYING](COPYING)。

第三方改编 Skill [check-the-licence-before-you-copy](skills/check-the-licence-before-you-copy/SKILL.md) 保留上游 Apache-2.0 许可，完整文本位于 [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt)，来源和修改说明见 [NOTICE](NOTICE)。其他第三方文件可能保留独立许可证、版权声明和 NOTICE，具体以对应文件及其来源证据为准。
