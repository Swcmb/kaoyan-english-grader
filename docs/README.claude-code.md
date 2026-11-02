# Claude Code 安装指南

本仓库提供 Claude Code 插件入口，也提供可独立安装的标准 Agent Skill。

## 作为插件安装

在 Claude Code 中执行：

~~~text
/plugin marketplace add Swcmb/kaoyan-english-grader
/plugin install kaoyan-english-grader@kaoyan-english-grader
~~~

安装后重新启动 Claude Code 会话。

## 作为独立 Skill 安装

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent claude-code
~~~

默认安装到当前项目的技能目录。添加 -g 参数可安装到用户级目录。

## 验证

要求 Claude Code 批改一道英语一或英语二翻译/作文题，检查它是否读取对应题型规则并按中文要求输出。
