# 考研英语 AI 批改 Skill

<p align="center">
  <strong>kaoyan-english-grader</strong><br>
  面向考研英语一、英语二的跨平台 AI 写作与翻译批改技能
</p>

<p align="center">
  <a href="https://github.com/Swcmb/kaoyan-english-grader">GitHub 仓库</a> ·
  <a href="#安装">安装</a> ·
  <a href="#使用">使用</a> ·
  <a href="#支持题型">支持题型</a>
</p>

本项目将考研英语阅卷练习规则封装为标准 **Agent Skill**，可安装到 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Antigravity、Kimi Code 等 AI Agent 环境。

它帮助你批改翻译与作文、定位失分原因、修正表达，并积累可以在考场复用的词组、句式和写作思路。

> **评分声明：** 本项目的评分标准和模拟采分点仅用于学习练习，不是官方阅卷标准，不代表真实考试成绩。不同年份、题目和阅卷尺度可能影响实际得分。

## 功能特点

- **六类题型独立批改：** 英语一、英语二的翻译、大作文、小作文分别使用对应规则。
- **先审题，再评分：** 优先核查任务要求、核心寓意、必答要点和图表信息，避免语言流畅但内容偏题。
- **区分错误与优化：** 标记【必须修改】和【可选优化】，不把正确但简单的表达判错。
- **保留考生原意：** 优先修改必要错误，尽量保留原有论证思路和正确句式。
- **逐项解释得失分：** 翻译采用模拟采分点，明确哪些信息表达准确、哪些内容误译或遗漏。
- **关注图表准确性：** 核对对象、时间、单位、数值、比例、排序和趋势，不编造数据。
- **支持手写图片：** 先转录再批改；无法辨认处请求确认，避免把 OCR 错误当作考生错误。
- **提供复盘材料：** 整理薄弱点、实用表达、写作框架和具体练习建议。
- **跨平台分发：** 采用标准 Skill 目录，配套多个 Agent 的原生安装入口。

## 支持题型

| 考试 | 题型 | 满分 | 批改重点 |
|---|---|---:|---|
| 英语一 | 大作文（B 节） | 20 分 | 图画寓意、切题性、论证、语言与结构 |
| 英语一 | 小作文（A 节） | 10 分 | 身份、对象、目的、任务要点、格式与语气 |
| 英语一 | 翻译 | 10 分 | 5 个划线句、模拟采分点、准确性与完整性 |
| 英语二 | 大作文 | 15 分 | 图表描述、数据准确性、趋势、评论与切题性 |
| 英语二 | 小作文 | 10 分 | 交际任务、必答要点、格式、语言与语气 |
| 英语二 | 翻译 | 15 分 | 句子或意群评分、误译漏译、中文表达 |

## 安装

### 推荐：使用 Skills CLI

安装前请确保本地已安装 Node.js 和 npm。Skills CLI 会引导你选择目标 Agent 与安装范围。

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader
~~~

一次安装到多个 Agent：

~~~bash
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
~~~

全局安装：

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader -g
~~~

更新已安装的 Skill：

~~~bash
npx skills update kaoyan-english-grader
~~~

Skills CLI 支持更多 Agent，完整名单请查看 [Agent Skills 支持列表](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

### 各平台原生安装

| 平台 | 安装方式 |
|---|---|
| Claude Code | 使用 Plugin Marketplace，或通过 Skills CLI 安装 |
| Codex | 使用 Plugin Marketplace，或通过 Skills CLI 安装 |
| Cursor | 使用 Cursor Plugin，或通过 Skills CLI 安装 |
| OpenCode | 使用标准 Agent Skill，或通过 Skills CLI 安装 |
| Gemini CLI | 使用 Gemini Extension，或通过 Skills CLI 安装 |
| Qwen Code | 使用 Qwen Extension，或通过 Skills CLI 安装 |
| Antigravity | 使用 Antigravity Plugin，或通过 Skills CLI 安装 |
| Kimi Code | 使用 Kimi Plugin，或通过 Skills CLI 安装 |
| Trae | 通过 Skills CLI 安装 |
| Windsurf | 通过 Skills CLI 安装 |
| Cline | 通过 Skills CLI 安装 |
| GitHub Copilot | 通过 Skills CLI 安装 |

各平台详细说明：

- [Skills CLI 通用安装](docs/README.skills-cli.md)
- [Claude Code](docs/README.claude-code.md)
- [Codex](docs/README.codex.md)
- [Cursor](docs/README.cursor.md)
- [Gemini CLI 与 Qwen Code](docs/README.gemini-cli.md)
- [OpenCode](docs/README.opencode.md)
- [Antigravity](docs/README.antigravity.md)
- [Kimi Code](docs/README.kimi-code.md)

> 不同 Agent 的插件机制和命令可能随版本变化。请优先参考对应平台文档中的最新安装步骤。

## 使用

安装后，直接告诉 Agent 你要批改的考试和题型，并提供题目与答案。

### 英语一大作文

~~~text
批改我的考研英语一大作文。
题目及图画：[提供完整题目或上传图片]
我的作文：[粘贴作文或上传清晰照片]
~~~

### 英语一小作文

~~~text
批改我的考研英语一小作文。
题目及写作要求：[提供身份、对象和任务]
我的作文：[粘贴作文或上传图片]
~~~

### 英语一翻译

~~~text
批改我的考研英语一翻译，共 5 个划线句。
英文原文：[提供完整原文和上下文]
我的译文：[按题号填写]
参考译文：[可选]
~~~

### 英语二大作文

~~~text
批改我的考研英语二图表大作文。
题目：[提供题干]
图表：[上传清晰图表或提供数据]
我的作文：[粘贴作文或上传图片]
~~~

### 英语二小作文

~~~text
批改我的考研英语二小作文。
题目及写作要求：[提供完整题目]
我的作文：[粘贴作文或上传图片]
~~~

### 英语二翻译

~~~text
批改我的考研英语二翻译。
英文原文：[提供完整原文和上下文]
我的译文：[粘贴译文]
参考译文：[可选]
~~~

支持直接上传题目、图画、图表、手写作文和手写译文。图片内容无法辨认时，Agent 应先请求确认。

## 批改原则

### 作文

- 先核查题目、身份、对象、目的、必答要点和字数要求，再进行综合评分。
- 重点评估内容切题与任务完成度、语言准确性与丰富性、结构与衔接。
- 英语一大作文核查图画寓意和论证主题是否一致，避免把相关话题偷换成核心话题。
- 英语一、英语二小作文核查交际目的与具体任务，避免空泛套话替代必要信息。
- 英语二大作文核查图表数据、趋势、对比和评论，区分图表事实与合理推测。
- 不因使用常见句型、简单词汇或模板本身扣分；空泛且缺乏切题价值的内容会影响内容评价。

### 翻译

- 按句子或意群划分模拟采分点，并明确说明这是练习用的模拟划分。
- 意思准确、信息完整且符合上下文即可得分，不要求与参考译文完全一致。
- 重点检查词义、句子主干、修饰关系、指代、否定和逻辑关系。
- 局部误译或漏译按对应信息点处理，避免重复扣分。
- 参考译文仅用于对照，最终判断以英文原文和上下文为准。

### 手写与缺失信息

- 先转录手写内容，尽量保留原拼写、语法和分段。
- 无法辨认或存在歧义时，请用户确认，不猜测、不擅自纠错。
- 缺少题目、图表或上下文时，说明评价范围与不确定性。
- 信息不足以评价内容完成度时，可以先批改语言，暂不提供确定总分。

## 仓库结构

~~~text
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
├── docs/
└── LICENSE
~~~

规范 Skill 源目录为 **skills/kaoyan-english-grader/**。各平台清单和安装入口围绕这一份内容组织，评分规则集中维护，避免多份提示词逐渐产生差异。

## 评分说明

- 所有分数均为练习估分，不代表官方评分或实际考试结果。
- 作文中的内容、语言、结构等权重属于辅助判断思路，不是官方固定扣分表。
- 翻译采分点属于模拟划分，不冒充官方评分细则。
- 不同题型使用各自的评分规则，避免混用满分、错别字扣分或评分档位。

## 参与贡献

欢迎提交 Issue 或 Pull Request，建议优先提供评分规则改进、Agent 安装兼容性问题、可复现的批改错误案例及文档优化。提交批改案例时，请尽量隐去个人信息。

## 许可证

本项目采用 [MIT License](LICENSE)。
