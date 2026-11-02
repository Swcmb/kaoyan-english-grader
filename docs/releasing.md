<!--
Copyright (C) 2026 kaoyan-english-grader contributors
SPDX-License-Identifier: GPL-3.0-or-later
This file is licensed under GPL-3.0-or-later. See LICENSE.
-->

# 版本发布与 GitHub Packages

本仓库通过 GitHub Actions 将同一个 Git 标签发布为 GitHub Release 和 GitHub Container Registry（GHCR）OCI 包。**GitHub Packages 是项目发布流程的一部分，保留并持续发布。**

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

发布前确认 README、Skill 主文件和六份评分规则已更新；插件清单的版本号与本次发布一致；许可证和第三方通知完整；标签指向已经检查的提交。

## GitHub Releases

工作流创建同名 Release，并附加：

| 文件 | 内容 |
| --- | --- |
| `kaoyan-english-grader-vX.Y.Z.zip` | 标签对应的完整仓库 ZIP |
| `kaoyan-english-grader-vX.Y.Z.tar.gz` | 标签对应的完整仓库 TAR.GZ |
| `SHA256SUMS` | 两个归档文件的 SHA-256 校验值 |

Release Notes 由 GitHub 根据标签和上一个版本自动生成。

发布入口：[GitHub Releases](https://github.com/Swcmb/kaoyan-english-grader/releases)。

## GitHub Packages（GHCR）

工作流构建一个用于分发 Skill 文件的最小 OCI 镜像，不提供可运行的 AI 服务。

镜像名称：

```text
ghcr.io/swcmb/kaoyan-english-grader
```

每次发布会生成 `vX.Y.Z` 和 `X.Y.Z` 两个标签。完整 Skill 目录位于：

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

Package 页面：[GitHub Packages](https://github.com/users/Swcmb/packages?repo_name=kaoyan-english-grader)。

### 首次发布后的可见性

个人账号下首次发布的 GHCR Package 默认是 Private。首次成功发布后，若要公开分发：

1. 打开上面的 Packages 页面，进入 `kaoyan-english-grader`。
2. 进入 **Package settings**。
3. 在 **Danger Zone** 中选择 **Change visibility**。
4. 选择 **Public** 并确认。

GitHub 文档说明，Package 一旦设为 Public，后续不能再改回 Private。公开前确认分发意图和包内容。参考 [GitHub Packages 可见性与访问控制](https://docs.github.com/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility)。

## 版本一致性与故障排查

Release 归档和 GHCR 镜像都从同一个标签对应的提交构建。重新发布同一标签前，先检查 Release 和 Package 是否已存在；修订优先使用新版本标签。

若 Release 成功而 GHCR 失败，检查 Actions 的 Package job、`packages: write` 权限、GHCR 登录和包的仓库关联。若 GHCR 成功而 Release 失败，检查 Release job 的 `contents: write` 权限、标签和资产上传日志。

不要通过删除 Package 来修复发布失败。先定位失败步骤，保留已有版本资产，再使用修复后的新标签重新发布。
