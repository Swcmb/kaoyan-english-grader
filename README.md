# kaoyan-english-grader 考研英语批改技能

一个用于 TRAE 等 AI 编程助手的 Skill，让 AI 化身考研英语阅卷老师，对你的考研英语作文和翻译进行**严格客观的模拟评分与逐句批改**。

## 功能特性

- **全题型覆盖**：英语一/英语二的大作文、小作文、翻译共 6 个模块
- **真实评分标准**：内置民间整理的分档评分参考，按内容、语言、结构综合定档
- **逐句批改**：区分【必须修改】与【可选优化】，标注原句、问题、修改句与中文解释
- **修改后全文**：保留你的原意与正确句式，加粗主要修改，注明修改后词数
- **复盘积累**：提炼实用表达与可复现句式，给出具体练习建议
- **手写识别友好**：先转录手写内容，无法辨认处请求确认，不把识别错误当你的错误

## 模块清单

| 模块 | 题型 | 满分 | 参考文档 |
|------|------|------|----------|
| 英语一大作文 | B 节议论文 | 20 分 | `references/english1_essay_major.md` |
| 英语一小作文 | A 节应用文 | 10 分 | `references/english1_essay_minor.md` |
| 英语一翻译 | 5 个划线句，每句 2 分 | 10 分 | `references/english1_translation.md` |
| 英语二大作文 | 图表作文 | 15 分 | `references/english2_essay_major.md` |
| 英语二小作文 | 应用文 | 10 分 | `references/english2_essay_minor.md` |
| 英语二翻译 | 整段英译汉 | 15 分 | `references/english2_translation.md` |

## 安装方法

### 方式一：克隆仓库

```bash
git clone https://github.com/Swcmb/kaoyan-english-grader.git
```

### 方式二：复制到技能目录

将本仓库内容复制到 TRAE 的技能目录：

```bash
# TRAE 技能目录（项目级）
mkdir -p .trae/skills
cp -r kaoyan-english-grader .trae/skills/
```

安装后，在对话中直接提出批改请求即可自动触发，无需手动粘贴指令。

## 使用示例

在 TRAE 对话中输入：

> 帮我批改这篇考研英语二大作文，满分 15 分。题目是……（粘贴题目与图表信息）我的作文是……（粘贴作文或上传手写照片）

或更简单地：

> 批改我的考研英语一翻译，共 5 个划线句。英文原文：……我的译文：……

技能会自动识别科目与题型，加载对应批改指令，输出：

1. 整体评分（词数、得分、档位及依据）
2. 逐句批改（原句 → 问题 → 修改句 → 中文解释）
3. 修改后全文（加粗主要修改）
4. 复盘积累（3 个改进问题 + 3—5 个实用表达）

## 批改守则

- 用中文讲解，英文呈现原句、修改句及修改后作文
- 严格客观，不刻意抬分或压分
- 先综合定档再给分，不机械按错误数量扣分
- 正确但简单的表达可以保留，不以生僻词为高分必要条件
- 缺少题目时先批改语言，暂不给确定总分

## 目录结构

```
kaoyan-english-grader/
├── SKILL.md              # 技能主入口（路由与通用守则）
├── README.md             # 使用说明
├── LICENSE               # MIT 许可证
└── references/           # 6 个批改指令模块
    ├── english1_essay_major.md
    ├── english1_essay_minor.md
    ├── english1_translation.md
    ├── english2_essay_major.md
    ├── english2_essay_minor.md
    └── english2_translation.md
```

## 免责声明

本技能的评分参考为民间整理，非官方阅卷标准，评分结果仅供练习参考，不代表实际考研成绩。

## 许可证

[MIT License](LICENSE)
