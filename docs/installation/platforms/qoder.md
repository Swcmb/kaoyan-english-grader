<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../../../LICENSE.
-->

# Qoder：安装与使用

Qoder IDE 与 Qoder CLI 支持标准 Agent Skills，可通过 Skills CLI、IDE 上传或手动放置目录安装。

## 安装方式

### 使用 Skills CLI

在 Qoder IDE 终端或 Qoder CLI 中执行：

```bash
npx skills add https://gitee.com/ianwusb/kaoyan-english-grader.git \
  --skill kaoyan-english-grader \
  --agent qoder
```

用户级安装增加 `-g`。

### 通过 Qoder IDE 上传

1. 打开 Qoder IDE。
2. 进入 **Extensions → Skills**。
3. 选择 **Add Skills → Upload Skill**。
4. 上传本仓库完整技能 ZIP。
5. 等待导入完成，在 Installed 列表检查状态。

ZIP 应包含技能目录、`SKILL.md` 和完整的 `references/`：

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

### 手动安装路径

| 范围 | 路径 |
| --- | --- |
| 用户级 Qoder | `~/.qoder/skills/kaoyan-english-grader/` |
| 项目级 Qoder | `.qoder/skills/kaoyan-english-grader/` |
| 用户级通用兼容目录 | `~/.agents/skills/kaoyan-english-grader/` |

项目级与用户级同名技能的优先级以当前 Qoder 文档为准。

## 验证与维护

在 Extensions → Skills → Installed 中确认技能已安装。在任务输入框输入 `/`，确认技能可选。测试英语一翻译与英语二大作文，检查对应的 `references/` 文件可读。

CLI 会话与 IDE 的重载方式可能不同，按当前版本重新加载或开启新任务。更新时重新运行安装命令或上传最新 ZIP；卸载只删除本技能。

## 安全与参考资料

导入前检查来源、内容、脚本和权限。本仓库以 Markdown 规则为核心，仍应核对实际下载包。

- [Qoder IDE：Skills](https://docs.qoder.com/extensions/skills)
- [Qoder CLI：Skills](https://docs.qoder.com/cli/Skills)
- [Skills CLI：Qoder 目录映射](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
