<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See ../LICENSE.
-->

# GitHub Releases 发布

仓库通过 GitHub Actions 将经过检查的 Git 标签发布为 GitHub Release。源码归档包含项目文件和唯一的自包含 Skill；发布附件同时提供 SHA-256 校验文件。

## 触发条件

推送符合以下格式的标签时触发：

~~~text
vMAJOR.MINOR.PATCH
vMAJOR.MINOR.PATCH-prerelease
~~~

例如：

~~~bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
~~~

工作流见 [publish.yml](../.github/workflows/publish.yml)。

## Release 资产

| 文件 | 内容 |
| --- | --- |
| `kaoyan-english-grader-vX.Y.Z.zip` | 标签对应的完整仓库 ZIP |
| `kaoyan-english-grader-vX.Y.Z.tar.gz` | 标签对应的完整仓库 TAR.GZ |
| `SHA256SUMS` | 两个源码归档的 SHA-256 校验值 |

Release Notes 由 GitHub 根据标签和上一个版本生成。发布入口：[GitHub Releases](https://github.com/Swcmb/kaoyan-english-grader/releases)。

## 从源码包安装 Skill

解压源码包后，安装唯一的 Skill 目录：

~~~text
skills/
└── kaoyan-english-grader/
    └── SKILL.md
~~~

支持标准 Agent Skills 的平台安装整个 `skills/kaoyan-english-grader/` 目录。明确提供单文件导入入口的平台可以直接导入该目录中的 `SKILL.md`。全部六类题型评分规则已经内嵌，不需要额外复制或下载引用文件。

## 发布前检查

- [ ] README、安装文档和版本说明描述当前实际能力。
- [ ] 唯一 Skill 的六类题型评分规则、满分和输入输出要求完整。
- [ ] 插件清单版本号与发布版本一致。
- [ ] 根目录 `LICENSE`、文件级版权和第三方通知完整。
- [ ] 标签指向经过审查的提交。
- [ ] 文档链接、安装步骤和示例与该版本一致。
- [ ] GitHub 页面渲染正常，归档可下载。

## 版本管理与故障排查

修订已发布内容时使用新版本标签，不覆盖已发布版本。创建失败时检查 Actions Release job、`contents: write` 权限、标签格式和资产上传日志。

发布后下载 ZIP 与 TAR.GZ，检查 Skill 主文件和六类评分规则，再校验 `SHA256SUMS`。归档校验通过不代表 Skill 已在任何平台完成安装测试。
