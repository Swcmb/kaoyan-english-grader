<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 考研英语 AI 批改

**面向考研英语（一）（二）主观题的完整 Agent Skill。** 覆盖翻译、大作文和小作文六类题型，依据题型专属规则完成审题、模拟评分、逐句批改、全文修订和针对性复盘。

[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPL--3.0--or--later-blue.svg)](LICENSE)
[![GitHub Releases](https://img.shields.io/github/v/release/Swcmb/kaoyan-english-grader?display_name=tag)](https://github.com/Swcmb/kaoyan-english-grader/releases)
[![GitHub Actions](https://github.com/Swcmb/kaoyan-english-grader/actions/workflows/publish.yml/badge.svg)](https://github.com/Swcmb/kaoyan-english-grader/actions/workflows/publish.yml)

> 所有分数均为备考训练用的模拟评价，不代表官方阅卷结果、官方评分细则或真实考试分数预测。

## 覆盖六类主观题

| 考试 | 题型 | 模拟满分 |
| --- | --- | ---: |
| 英语一 | 翻译（5 个划线句） | 10 分 |
| 英语一 | 大作文（B 节） | 20 分 |
| 英语一 | 小作文（A 节应用文） | 10 分 |
| 英语二 | 翻译 | 15 分 |
| 英语二 | 大作文（通常为图表作文） | 15 分 |
| 英语二 | 小作文（应用文） | 10 分 |

每种题型使用独立评分档位、审题要求和输出流程，英语一与英语二分别执行。

## 批改输出

一次完整批改包括审题与任务核查、模拟评分及依据、逐句问题定位、修改建议、完整修订稿和针对性复盘。翻译按句子或意群划分模拟采分点；作文先核查任务完成度和切题性，再评价语言、结构、格式与语气。

## 安装

### 推荐：通过 Agent 自动安装

将下列指令交给支持标准 Agent Skills 的助手：

```text
请安装 Git 仓库中的「考研英语 AI 批改」Skill。

GitHub：https://github.com/Swcmb/kaoyan-english-grader
Gitee：https://gitee.com/ianwusb/kaoyan-english-grader

安装 skills/kaoyan-english-grader/ 完整目录，保留 SKILL.md 和 references/ 下六份评分规则。
先检查目标目录是否存在同名技能，再使用当前 Agent 支持的安装方式。
安装后验证主文件、六份规则和技能发现状态，并报告实际路径。
不要只给教程，不要覆盖来源不明的同名目录。
```

也可以让 Agent 直接读取 [INSTALL.md](INSTALL.md)。

### 使用 Skills CLI

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader
```

指定 Codex：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader --agent codex
```

用户级安装增加 `-g`。详细步骤见 [Skills CLI 安装指南](docs/installation/skills-cli.md)。

### 单文件完整版本

只接受单个 `SKILL.md` 的导入入口，可使用[内嵌六类评分规则的完整单文件版本](dist/kaoyan-english-grader-single-file/SKILL.md)。该文件不依赖外部 `references/`。支持标准目录的 Agent 应优先安装完整目录版。

### 其他平台

- [安装渠道总览](docs/installation/README.md)
- [Claude 网页版与 Desktop](docs/installation/platforms/claude.md)
- [Trae](docs/installation/platforms/trae.md)
- [Qoder](docs/installation/platforms/qoder.md)
- [QwenWork](docs/installation/platforms/qwenwork.md)
- [WorkBuddy](docs/installation/platforms/workbuddy.md)
- [手机端渠道](docs/installation/mobile-apps.md)

## 使用示例

英语一翻译：

```text
请使用考研英语 AI 批改 Skill。

考试：英语一
题型：翻译
英文原文：（粘贴完整原文及上下文）
我的译文：（按题号粘贴译文）

请按英语一翻译规则模拟评分，逐句解释失分点，
提供完整修改版和针对性复盘。
```

英语二大作文：

```text
请使用考研英语 AI 批改 Skill。

考试：英语二
题型：大作文
题目与图表：（粘贴题目或上传清晰图片）
我的作文：（粘贴作文）

请先核实图表对象、时间、单位和主要数据，再检查切题性，
给出模拟评分、逐句修改、完整修订稿和复盘。
```

## 评分边界

- 评分档位和翻译采分点均为训练用途的模拟参考。
- 翻译按英文原文和上下文判断，不因措辞不同于参考译文而直接扣分。
- 每项重要评价和扣分应对应题目、原文、译文或图表证据。
- 正确、自然且符合语境的表达可以保留。
- 图像、题目或上下文不完整时，明确说明评价范围和不确定性。
- 不猜测手写内容，不编造图表数据、经历或原文没有的信息。

## 项目结构

```text
kaoyan-english-grader/
├── skills/kaoyan-english-grader/
│   ├── SKILL.md
│   └── references/                 # 六类题型规则
├── dist/kaoyan-english-grader-single-file/
│   └── SKILL.md                    # 内嵌完整规则
├── docs/
│   ├── installation/
│   ├── standards/
│   └── releasing.md
├── .github/workflows/publish.yml
├── INSTALL.md
├── GEMINI.md
├── LICENSE
└── README.md
```

## 文档

- [文档中心](docs/README.md)
- [安装与使用渠道](docs/installation/README.md)
- [GitHub 内容写作与 Markdown 排版规范](docs/standards/github-content-writing.md)
- [公开开源项目文档规范](docs/standards/open-source-docs.md)
- [本机与私有项目文档规范](docs/standards/local-dev-docs.md)
- [第三方内容与许可证审查规范](docs/standards/third-party-license-review.md)
- [GitHub Releases 发布说明](docs/releasing.md)

## GitHub Releases

推送符合格式的版本标签后，GitHub Actions 创建 Release，并附加完整源码 ZIP、TAR.GZ 和 SHA-256 校验文件。

[查看 Releases](https://github.com/Swcmb/kaoyan-english-grader/releases) · [发布工作流](.github/workflows/publish.yml)

## License

本仓库原创内容采用 [GNU GPL-3.0-or-later](LICENSE)。第三方材料保留各自版权声明、许可证和必要通知。
