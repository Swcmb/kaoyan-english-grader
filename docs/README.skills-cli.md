# 使用通用技能安装工具

本仓库将标准 Agent Skill 放在 skills/kaoyan-english-grader 目录中。通用技能安装工具可以将它安装到多种编程 Agent 的技能目录，无需手动复制平台文件。

## 交互式安装

需要 Node.js 22.20 或更高版本。

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader
~~~

根据提示选择一个或多个 Agent，以及项目级或用户级安装范围。

## 指定 Agent 安装

~~~bash
npx skills add Swcmb/kaoyan-english-grader \
  --skill kaoyan-english-grader \
  --agent claude-code \
  --agent codex \
  --agent cursor \
  --agent opencode \
  --agent gemini-cli \
  --agent antigravity \
  --agent kimi-code-cli
~~~

添加 -g 参数可安装到用户级目录。

## 更新

~~~bash
npx skills update kaoyan-english-grader
~~~

## 支持的平台

安装工具支持的 Agent 名单会持续变化，请查看其维护文档：

[查看 Agent 支持列表](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

## 验证安装

在目标 Agent 中查看已安装技能，或直接要求它批改英语一/英语二的翻译或作文。确认 Agent 能够读取对应的题型规则文件。
