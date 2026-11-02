# Gemini CLI 与 Qwen Code 安装指南

仓库包含 Gemini CLI 扩展清单，以及用于加载标准 Skill 的 GEMINI.md 入口文件。

## Gemini CLI

从 GitHub 安装：

~~~bash
gemini extensions install https://github.com/Swcmb/kaoyan-english-grader
~~~

安装后重新启动 Gemini CLI。更新扩展：

~~~bash
gemini extensions update
~~~

查看已安装扩展：

~~~text
/extensions list
~~~

## Qwen Code

通过扩展命令安装：

~~~bash
qwen extensions install Swcmb/kaoyan-english-grader
~~~

安装后重新启动 Qwen Code。可使用其扩展管理命令查看已安装扩展。

## 作为独立 Skill 安装

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent gemini-cli
~~~

## 验证

要求 Agent 批改一道具体题目，检查它是否读取对应的中文题型规则。
