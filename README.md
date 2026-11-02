# kaoyan-english-grader

跨平台考研英语 AI 批改 Skill，覆盖中国研究生招生考试英语一、英语二的翻译、大作文和小作文，共六种题型。项目采用标准 Agent Skill 目录结构，并提供 Claude Code、Codex、Cursor、Gemini CLI、OpenCode、Antigravity、Kimi Code 等平台的原生安装入口。

所有评分均为练习参考，不是官方阅卷结果，也不保证与实际考试分数一致。

## Features

- **Six independent grading modules**：英语一/英语二翻译、大作文、小作文分别采用独立评分规则。
- **Task-first essay grading**：先审题与任务完成度，再综合评价语言、结构、格式和语气。
- **Relevance checks**：英语一大作文核对图画寓意与论证；英语一小作文核对身份、对象、目的和必答事项。
- **Chart verification**：英语二大作文核对图表对象、时间、单位、数值、比例、排序和趋势，区分数据事实与合理推测。
- **Point-based translation scoring**：模拟采分点，逐项解释得分和失分，不冒充官方评分点。
- **Error vs. improvement**：区分【必须修改】与【可选优化】，保留正确、自然的简单表达。
- **Handwriting-aware**：先转录再批改；无法辨认处要求确认，不把识别错误当成考生错误。
- **Portable Agent Skill**：一份规范内容，多平台发现；不依赖 MCP、外部 API、shell 脚本或运行时 Hook。

## Six task types

| Exam | Task | Score | Reference |
|---|---|---:|---|
| English I | Major essay (B section) | 20 | skills/kaoyan-english-grader/references/english1_essay_major.md |
| English I | Minor essay (A section) | 10 | skills/kaoyan-english-grader/references/english1_essay_minor.md |
| English I | Translation (5 underlined sentences) | 10 | skills/kaoyan-english-grader/references/english1_translation.md |
| English II | Major essay (usually chart-based) | 15 | skills/kaoyan-english-grader/references/english2_essay_major.md |
| English II | Minor essay | 10 | skills/kaoyan-english-grader/references/english2_essay_minor.md |
| English II | Translation | 15 | skills/kaoyan-english-grader/references/english2_translation.md |

## Installation

### Recommended: Agent Skills CLI

Install the skill into one or more supported agents. Requires Node.js 22.20 or later.

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader
~~~

The installer lets you choose the target agent(s) and project/global scope.

Install to selected agents directly:

~~~bash
npx skills add Swcmb/kaoyan-english-grader \
  --skill kaoyan-english-grader \
  -a claude-code \
  -a codex \
  -a cursor \
  -a opencode \
  -a gemini-cli \
  -a antigravity \
  -a kimi-code-cli
~~~

Add -g or --global for user-wide installation. Update an installed skill with npx skills update kaoyan-english-grader.

The CLI supports many additional agents. See [the supported agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

### Native plugin installation

| Agent | Native installation |
|---|---|
| Claude Code | /plugin marketplace add Swcmb/kaoyan-english-grader, then /plugin install kaoyan-english-grader@kaoyan-english-grader |
| Codex | codex plugin marketplace add Swcmb/kaoyan-english-grader, then open /plugins and install the plugin |
| Cursor | Copy the repository into ~/.cursor/plugins/local/kaoyan-english-grader, reload Cursor, and inspect Customize |
| Gemini CLI | gemini extensions install https://github.com/Swcmb/kaoyan-english-grader |
| Qwen Code | qwen extensions install Swcmb/kaoyan-english-grader |
| Antigravity CLI | agy plugin install https://github.com/Swcmb/kaoyan-english-grader |
| Kimi Code | /plugins install https://github.com/Swcmb/kaoyan-english-grader, then /reload or start a new session |
| OpenCode | Install with npx skills add ... -a opencode, or copy the skill folder into .agents/skills/ or ~/.config/opencode/skills/ |

Detailed steps:

- [Agent Skills CLI](docs/README.skills-cli.md)
- [Claude Code](docs/README.claude-code.md)
- [Codex](docs/README.codex.md)
- [Cursor](docs/README.cursor.md)
- [Gemini CLI and Qwen Code](docs/README.gemini-cli.md)
- [OpenCode](docs/README.opencode.md)
- [Antigravity](docs/README.antigravity.md)
- [Kimi Code](docs/README.kimi-code.md)

## Usage

Tell the agent the exam and task type, then provide the complete prompt and your response.

**English I major essay**

> 批改我的考研英语一大作文。题目和图画：[提供题目]。我的作文：[粘贴作文或上传清晰照片]。

**English I minor essay**

> 批改我的英语一小作文。题目要求：[提供身份、对象和任务]。我的作文：[粘贴作文]。

**English I translation**

> 批改英语一翻译，共 5 个划线句。英文原文：[提供完整原文和上下文]。我的译文：[按题号填写]。

**English II major essay**

> 批改英语二图表大作文。题目：[提供题干]。图表：[上传清晰图片或提供数据]。我的作文：[粘贴作文]。

**English II minor essay**

> 批改英语二小作文。题目：[提供题干]。我的作文：[粘贴作文]。

**English II translation**

> 批改英语二翻译。英文原文：[提供完整原文]。我的译文：[粘贴译文]。参考译文：[可选]。

也可以直接上传题目、图画、图表、手写作文或译文照片。无法辨认的内容会先请求确认。

## Repository structure

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

The canonical skill lives in skills/kaoyan-english-grader. Platform manifests point to that directory; grading rules are maintained once and shared across agents.

## Scoring boundaries

- Score bands and grading details are user-oriented practice references, not official marking rubrics.
- Essay weighting references (50% task/content, 30% language, 20% organization/format) are non-official judgment aids, not a mechanical formula.
- Translation scoring points are simulated to explain the score; they are not official scoring points.
- Missing prompts, unclear charts, or unreadable handwriting limit content scoring. The agent must state uncertainty rather than invent information.
- Rules specific to a task type take precedence over global guidance. Scores and typo deductions must never be mixed across different modules.

## License

[MIT License](LICENSE)
