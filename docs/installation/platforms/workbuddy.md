<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# WorkBuddy 桌面端：安装与使用

WorkBuddy 支持技能市场、技能搜索和自定义技能，也支持上传本地技能包。本仓库依赖六份引用规则，推荐通过 ZIP 导入。

## 准备技能 ZIP

克隆仓库：

```bash
git clone https://gitee.com/ianwusb/kaoyan-english-grader.git
```

将 `skills/kaoyan-english-grader/` 整个目录压缩为 ZIP。包内应包含：

```text
kaoyan-english-grader/
├── SKILL.md
└── references/
    ├── english1_essay_major.md
    ├── english1_essay_minor.md
    ├── english1_translation.md
    ├── english2_essay_major.md
    ├── english2_essay_minor.md
    └── english2_translation.md
```

确保主文件与引用目录同级，不要只压缩 `SKILL.md`。

## 在 WorkBuddy 中上传

1. 打开 WorkBuddy 桌面客户端并登录。
2. 在侧边栏进入 **专家·技能·连接器**。
3. 点击 **添加技能 → 上传技能**。
4. 拖入 ZIP，或从文件选择器中选取。
5. 等待导入完成，在技能列表确认技能出现并启用。

WorkBuddy 还提供“查找技能”和“创建技能”入口：查找用于发现已有能力；创建用于封装自定义任务流程。

## 使用与验证

在对话中描述考研英语翻译或作文批改任务，WorkBuddy 可根据任务匹配技能。需要明确指定时，在技能管理面板选择本技能后再开始对话。

先测试英语一翻译，再测试英语二大作文，确认六份规则可以读取。

## 安装范围、更新与卸载

技能作用范围以当前客户端提供的选项为准。若界面提供用户级或项目级选择，用户级适合多个工作区复用，项目级适合限定在当前仓库或工作区。

更新时从最新 Gitee 仓库重新准备完整 ZIP，按客户端管理页的更新或重新导入流程操作。卸载时在已安装列表中选择本技能，不要删除其他技能。

## 安全与官方资料

启用前检查来源、权限和文件内容。第三方 Skill 可能包含脚本、外部 API 请求或数据传输行为；本仓库以 Markdown 规则为核心，仍应核对下载包来源。

- [WorkBuddy：技能安装与管理](https://cloud.tencent.com/document/product/1831/134432)
