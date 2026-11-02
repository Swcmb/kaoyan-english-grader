# Codex 安装指南

本仓库提供通用插件清单、Codex 兼容清单和仓库级插件市场入口。

## 作为插件安装

将 GitHub 仓库添加为插件市场：

~~~bash
codex plugin marketplace add Swcmb/kaoyan-english-grader
~~~

随后打开 Codex，执行 /plugins，找到 kaoyan-english-grader 插件市场并安装插件。安装后开启新会话。

更新插件市场元数据：

~~~bash
codex plugin marketplace upgrade kaoyan-english-grader
~~~

## 作为独立 Skill 安装

Codex 会从项目级 .agents/skills 目录或用户级 ~/.agents/skills 目录发现技能。使用通用安装工具：

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent codex
~~~

添加 -g 参数可安装到用户级目录。

## 验证

要求 Codex 批改一道具体题目，确认其读取 skills/kaoyan-english-grader/references/ 下对应的中文规则文件。
