<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# Google Antigravity 安装与使用

Antigravity 的 App、IDE 与 CLI 都支持 Agent Skills。项目级目录适合与仓库共享；用户级目录用于跨工作区复用。

## 方式一：通过 Gitee 安装

在项目根目录打开终端：

~~~bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent antigravity
~~~

默认安装到项目级 .agents/skills/。项目级路径可供 Antigravity App、IDE 和 CLI 识别。

## 方式二：手动安装标准 Skill

克隆仓库：

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
~~~

将完整技能目录复制到：

- 项目级：项目根目录/.agents/skills/kaoyan-english-grader/
- 用户级：~/.gemini/config/skills/kaoyan-english-grader/

独立 Antigravity IDE 还兼容旧目录 ~/.gemini/antigravity/skills/。Antigravity CLI 也读取 ~/.gemini/antigravity-cli/skills/ 和 ~/.gemini/skills/；这些目录不一定被 App 端读取。跨端共享优先采用项目级 .agents/skills/ 或官方当前文档列出的全局配置目录。

## 方式三：作为插件安装

仓库提供 Antigravity 插件清单。插件方式使用 GitHub 仓库地址：

~~~bash
agy plugin install https://github.com/Swcmb/kaoyan-english-grader
agy plugin list
~~~

如果已将仓库克隆到本地：

~~~bash
agy plugin validate --strict ./kaoyan-english-grader
agy plugin install ./kaoyan-english-grader
~~~

Gitee 地址用于标准 Skill 的 CLI 安装；Antigravity 插件安装命令按官方说明使用 GitHub URL 或本地插件目录。

## 查看与验证

- Antigravity App：在 Agent 侧边栏打开 Customizations，检查技能列表。
- Antigravity IDE：在 Agent 侧边栏的 Customizations 中检查技能。
- Antigravity CLI：输入 /kaoyan-english-grader，或执行 /skills reload 重新扫描。

提交英语一翻译和英语二大作文两个测试任务，确认 references 目录可读。

## 更新与卸载

标准 Skill 通过 Skills CLI 更新，或用新版本完整替换目录。插件更新使用 agy plugin 对应的更新/重新安装流程。卸载时只移除 kaoyan-english-grader 对应目录或插件，不删除同级其他技能。

## 官方资料

- [Google Antigravity：Agent Skills](https://antigravity.google/docs/skills?app=antigravity)
- [Google Antigravity：Plugins](https://www.antigravity.google/docs/plugins)
- [Skills CLI：Antigravity 目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
