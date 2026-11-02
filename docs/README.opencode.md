# OpenCode 安装指南

OpenCode 原生支持 Agent Skills 格式。它可以从项目级 .agents/skills/、.opencode/skills/，以及用户级 ~/.agents/skills/、~/.config/opencode/skills/ 目录发现技能。

## 推荐安装方式

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent opencode
~~~

添加 -g 参数可安装到用户级目录。

## 手动安装

将完整技能目录（包括 references 文件夹）复制到以下任一位置：

- 项目级：.agents/skills/kaoyan-english-grader/
- 项目原生目录：.opencode/skills/kaoyan-english-grader/
- 用户级：~/.config/opencode/skills/kaoyan-english-grader/
- 通用用户级：~/.agents/skills/kaoyan-english-grader/

请确保 SKILL.md 与 references/ 位于同一技能目录结构中。

## 验证

在 OpenCode 中请求批改英语一或英语二题目，确认技能已加载且能读取对应规则。
