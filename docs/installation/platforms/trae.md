<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Trae / Trae CN：安装与使用

Trae 支持以 `SKILL.md` 定义技能，并提供全局和项目两种安装范围。官方 IDE 文档包含本地导入和技能市场流程。

## 安装方式

### 使用 Skills CLI

在项目根目录执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent trae-cn
```

用户级安装增加 `-g`。

### 通过 Trae IDE 导入

1. 打开 Trae。
2. 进入 **设置 → 技能与命令**。
3. 在“技能”区域选择 **创建**。
4. 选择全局或项目范围。
5. 选择 **导入本地技能**。
6. 上传完整技能 ZIP，并确认名称、描述和指令。
7. 保存后检查技能列表。

本仓库 ZIP 应包含 `SKILL.md` 和 `references/` 六份规则。压缩时可将文件放在 ZIP 根目录，也可保留最外层技能目录；导入后检查最终目录是否保留引用文件。

### 手动安装路径

| 范围 | 路径 |
| --- | --- |
| 项目级 | `.trae/skills/kaoyan-english-grader/` |
| 用户级 macOS / Linux | `~/.trae-cn/skills/kaoyan-english-grader/` |
| 用户级 Windows | `%USERPROFILE%/.trae-cn/skills/kaoyan-english-grader/` |

将完整目录放到目标位置，不要只复制主文件。

## 验证、更新与卸载

1. 在“设置 → 技能与命令”中选择对应范围，检查技能列表。
2. 在 Agent 对话中输入 `/`，确认技能可选。
3. 测试英语一翻译和英语二大作文。
4. 检查对应评分规则文件可读。

更新时重新导入最新完整技能包，或使用 Skills CLI 更新。卸载时只删除目标范围下的 `kaoyan-english-grader/`。

## 产品版本边界

公开的 Trae IDE 技能文档包含设置、导入、项目/全局目录和技能市场流程。TraeCode、TraeWork 等产品线的菜单可能不同，以当前客户端技能管理页面为准。

## 官方资料

- [Trae：技能（Skill）](https://docs.trae.cn/ide_skills)
- [Skills CLI：Trae 与 Trae CN 路径](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
