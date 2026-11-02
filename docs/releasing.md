<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 版本发布与 Packages

本仓库使用 GitHub Actions 将同一个 Git 标签发布为 GitHub Release 和 GitHub Container Registry（GHCR）OCI 包。

## 发布触发条件

推送符合以下格式的标签时触发：

```text
vMAJOR.MINOR.PATCH
vMAJOR.MINOR.PATCH-prerelease
```

例如：

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

工作流：[publish.yml](../.github/workflows/publish.yml)

发布前确认：

- README、Skill 主文件和六份评分规则已更新。
- `plugin.json` 等宿主清单中的版本号与本次发布版本一致。
- `LICENSE`、第三方版权声明和必要通知完整。
- 当前标签指向经过检查的提交。

## GitHub Releases

工作流会创建同名 Release，并附加以下文件：

| 文件 | 内容 |
| --- | --- |
| `kaoyan-english-grader-vX.Y.Z.zip` | 标签对应的完整仓库源码 ZIP |
| `kaoyan-english-grader-vX.Y.Z.tar.gz` | 标签对应的完整仓库源码 TAR.GZ |
| `SHA256SUMS` | 两个压缩包的 SHA-256 校验值 |

Release Notes 由 GitHub 根据标签与上一个版本自动生成。

发布入口：[GitHub Releases](https://github.com/Swcmb/kaoyan-english-grader/releases)。

## GitHub Packages（GHCR）

工作流将 Skill 打包成一个最小 OCI 镜像，推送到：

```text
ghcr.io/swcmb/kaoyan-english-grader
```

每次发布会生成两个镜像标签：

- `vX.Y.Z`
- `X.Y.Z`

镜像是用于分发文件的静态包，不是可运行的 AI 服务。Skill 目录位于：

```text
/opt/skills/kaoyan-english-grader/
```

下载并提取：

```bash
docker pull ghcr.io/swcmb/kaoyan-english-grader:v1.0.0
docker create --name kaoyan-skill-package ghcr.io/swcmb/kaoyan-english-grader:v1.0.0
docker cp kaoyan-skill-package:/opt/skills/kaoyan-english-grader ./kaoyan-english-grader
docker rm kaoyan-skill-package
```

如果只需要安装 Skill，优先使用 Release ZIP 或 [Skills CLI](../README.md#安装)。

Package 入口：[GitHub Packages](https://github.com/users/Swcmb/packages?repo_name=kaoyan-english-grader)。

### 首次发布后的可见性设置

GitHub Container Registry 中，个人账号首次创建的 Package 默认是 Private。首次成功发布后：

1. 打开上面的 Packages 页面，进入 `kaoyan-english-grader`。
2. 进入 **Package settings**。
3. 在 **Danger Zone** 中选择 **Change visibility**。
4. 选择 **Public** 并确认。

将 Package 设为 Public 后，任何人都可以匿名拉取；GitHub 不支持将已经公开的 Package 再改回 Private。请在确认公开分发意图后执行此操作。详情见 [GitHub Packages 可见性与访问控制文档](https://docs.github.com/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility)。

## 版本一致性

一次发布由同一个 Git 标签驱动：

- Release 资产从该标签对应的提交归档。
- GHCR 镜像从同一标签对应的 Dockerfile 和 Skill 文件构建。
- `vX.Y.Z` 与 `X.Y.Z` 指向同一镜像内容。

重新发布同一个标签前，先检查 Release 和 Package 是否已存在。推荐通过新版本标签发布修订，避免覆盖既有版本。
