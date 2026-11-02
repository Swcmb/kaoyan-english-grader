<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# WorkBuddy 桌面端安装与使用

WorkBuddy 支持从技能市场安装技能，也支持上传本地技能包、查找技能和创建自定义技能。本仓库适合通过本地技能包导入。

## 准备技能包

从 Gitee 克隆仓库：

~~~bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
~~~

进入以下目录：

~~~text
kaoyan-english-grader/skills/kaoyan-english-grader/
├── SKILL.md
└── references/
    ├── english1_essay_major.md
    ├── english1_essay_minor.md
    ├── english1_translation.md
    ├── english2_essay_major.md
    ├── english2_essay_minor.md
    └── english2_translation.md
~~~

将整个 kaoyan-english-grader 技能文件夹压缩为 ZIP。确保 ZIP 内的 SKILL.md 和 references/ 同级，不要仅压缩 SKILL.md。

## 从 WorkBuddy 上传

1. 打开 WorkBuddy 桌面客户端并登录。
2. 在左侧边栏打开 **专家·技能·连接器**。
3. 点击 **添加技能**。
4. 选择 **上传技能**。
5. 拖入准备好的 ZIP，或点击选择文件。
6. 等待 WorkBuddy 导入并自动配置。
7. 在技能列表中确认技能出现，再按当前客户端的启用状态设置启用。

WorkBuddy 也提供“查找技能”和“创建技能”入口。查找方式适合在技能库寻找已有能力；创建方式适合将一段任务说明封装成新技能。

## 使用

在对话中直接提出批改要求，WorkBuddy 可根据任务描述自动匹配技能。需要明确指定时，在技能管理面板中选择本技能，再开始对话。

建议先测试：

~~~text
请使用考研英语 AI 批改技能，批改下面这道英语一翻译题。
请逐句解释失分点，并读取对应的题型规则。
~~~

然后再用英语二大作文图表题做一次独立验证，避免只测试主指令文件。

## 用户级与项目级

WorkBuddy 的具体作用范围以当前客户端所提供的上传/工作区选项为准。若界面显示用户级或项目级选项：
- 用户级适合在所有工作区复用；
- 项目级适合只在当前仓库或工作区启用。

官方技能帮助页描述的是本地技能包上传和管理界面。不同版本的底层目录可能调整，不建议在未经确认时手动依赖内部存储路径。

## 更新与卸载

需要更新时，重新从最新 Gitee 仓库准备完整 ZIP，再按客户端技能管理页面提供的更新或重新导入流程操作。删除技能时，在已安装列表中选择本技能并卸载；不要删除其他技能。

## 安全检查

第三方 Skill 可能包含脚本、外部 API 请求或数据传输指令。启用前检查来源、脚本内容和权限范围。批改 Skill 主要使用 Markdown 规则文件，但仍应确认上传包来自本项目官方仓库或其镜像。

## 官方资料

- [WorkBuddy：技能安装与管理](https://cloud.tencent.com/document/product/1831/134432)
