---
name: kaoyan-english-grader
description: Use when grading or improving Chinese postgraduate entrance exam English (考研英语一/英语二) translation, major essays, or minor practical essays. Covers six task types with exam-specific rubrics, task relevance checks, point-based translation scoring, sentence-level corrections, revised full text, and targeted study feedback.
license: MIT
compatibility: Works with Agent Skills-compatible assistants that can read local files and user-provided text or images. No MCP server, external API, or runtime dependency is required.
metadata:
  author: Swcmb
  version: "1.0.0"
---

# Kaoyan English Grader

Use this skill to grade and teach the six subjective task types in China's postgraduate entrance examination English tests:

- English I translation: five underlined sentences, 10 points.
- English I major essay: 20 points.
- English I minor essay: 10 points.
- English II translation: 15 points, with an optional five-sentence, three-points-per-sentence practice mode.
- English II major essay: 15 points, usually a chart-based essay.
- English II minor essay: 10 points.

All explanations are in Chinese. Preserve English originals, corrections, and revised essays in English. Scores are practice estimates based on the repository's stated reference rubrics; never present them as official marking schemes or guaranteed exam scores.

## Workflow

1. Identify the exam (English I or English II) and task type.
2. Read the matching reference file in the references directory before grading. Do not replace its detailed rules with this summary.
3. Check whether the prompt, writing instructions, original English, image/chart, and learner's response are sufficient for the requested evaluation.
4. For essays, extract the actual task requirements and judge task completion and relevance before language quality. For translation, parse the source sentence and its context before judging the Chinese rendering.
5. Quote concrete evidence for every material criticism and score decision.
6. Separate actual errors from optional improvements. Preserve correct wording, simple but effective sentences, and the learner's valid reasoning.
7. Produce the required corrections, a complete revised version where possible, and targeted study feedback.
8. Check score arithmetic, score band, word count, and consistency between the diagnosis and revised version.

## Task routing

| User request | Read this file |
|---|---|
| English I major essay / B section / picture-based essay | references/english1_essay_major.md |
| English I minor essay / A section / practical writing | references/english1_essay_minor.md |
| English I translation / five underlined sentences | references/english1_translation.md |
| English II major essay / chart-based essay | references/english2_essay_major.md |
| English II minor essay / practical writing | references/english2_essay_minor.md |
| English II translation / passage translation | references/english2_translation.md |

Use the user's explicit exam and task labels when supplied. When they are missing, infer only from strong task characteristics. Five underlined sentences usually indicate English I translation; a chart description plus commentary usually indicates English II major essay. If the evidence is insufficient, ask one concise question instead of guessing.

## Global grading rules

- Be strict and impartial. Do not inflate or suppress scores to sound encouraging or severe.
- The task-specific reference file controls its score bands, point allocation, typo deductions, and output order.
- Distinguish [必须修改] from [可选优化]. A correct sentence can be retained as-is.
- Do not reward rare vocabulary, long sentences, or formulaic transitions merely because they look advanced.
- Do not penalize common expressions when they are accurate, appropriate, and useful for the task.
- Every deduction must map to a specific source meaning, task requirement, or identifiable language error. Do not deduct twice for the same underlying problem.
- Essay weights such as content/task 50%, language 30%, and organization/format 20% are non-official judgment aids, not a mechanical scoring formula.
- A missing prompt, unreadable chart, or uncertain handwriting limits what can be graded. Grade what is reliably available and state what remains uncertain; never invent missing content.
- For handwritten work, transcribe first while preserving the learner's original spelling, grammar, punctuation, and paragraphing. Ask the user to confirm unreadable fragments; do not silently correct OCR/visual-recognition errors.
- Count English words using a consistent space-separated convention and state what was included or excluded when relevant. Do not invent word-count deduction formulas.
- Reference translations are secondary evidence. The English original and context govern translation judgments.
- Revised text must not add unsupported data, facts, experiences, arrangements, or causal claims.
- Before finishing, verify the chosen module, maximum score, score arithmetic, typo deductions, score band, word count, and revised-text consistency.

## Reference loading

Read only the relevant module for the current task, but read that module in full. If the user submits more than one task type, grade each task independently and never mix rubrics.

For supporting instructions, resolve paths relative to this SKILL.md:
- references/english1_essay_major.md
- references/english1_essay_minor.md
- references/english1_translation.md
- references/english2_essay_major.md
- references/english2_essay_minor.md
- references/english2_translation.md
