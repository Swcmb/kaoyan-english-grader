<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# QwenWork：安装与使用

QwenWork 提供技能广场、对话搜索、开源仓库获取和本地文件上传。完整目录版可以保留引用规则；单文件版本适用于只上传一个 `SKILL.md` 的入口。

## 安装与使用

### 本地目录版上传

1. 打开 QwenWork。
2. 进入 **扩展 → 技能**。
3. 点击 **Install Skill** 或当前页面中的上传入口。
4. 上传 `SKILL.md` 及其辅助文件；目录版同时提供 `references/` 六份规则。
5. 等待导入完成，在已安装区域检查状态。

### 单文件版

只接收单个文件时，上传[内嵌全部规则的 SKILL.md](../../../dist/kaoyan-english-grader-single-file/SKILL.md)。

### 从仓库获取

```text
请从这个仓库获取考研英语批改 Skill：
https://gitee.com/ianwusb/kaoyan-english-grader.git

只安装 skills/kaoyan-english-grader。
保留 SKILL.md 和 references/ 下全部题型规则。
完成后报告实际路径，并检查六份文件。
```

也可以在技能广场搜索并安装平台已有条目。

## 能力边界

技能广场安装的是平台收录条目；本地上传和从仓库获取是独立渠道。目录版必须连同所有辅助文件导入。单文件版可独立使用，不依赖引用目录。

## 验收

确认技能出现在目标产品的已安装列表，并分别测试英语一翻译和英语二大作文，核对对应规则、分值和输出要求。

## 本仓库的 Skill 版本选择

若当前导入入口能保留完整目录或 ZIP 内的相对路径，使用标准版 `skills/kaoyan-english-grader/`，确保 `SKILL.md` 与 `references/` 六份规则完整保留。若产品实际只接受单个标准 `SKILL.md` 文件，再使用独立完整版 `skills/kaoyan-english-grader-full/SKILL.md`。技能市场条目、应用内创建和本地文件导入属于不同流程；市场安装要求本项目已真实上架，应用内创建则需手动迁移并核对规则。

## 官方资料

- [QwenWork：Skills 官方文档](https://docs.qwenwork.ai/desktop/skills)
- [QwenWork：技能帮助文档](https://qwenwork.cn/docs/features/skills)
