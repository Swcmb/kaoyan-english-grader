# OpenCode

OpenCode supports the Agent Skills format natively. It discovers project skills from .agents/skills/ and .opencode/skills/, and global skills from ~/.agents/skills/ and ~/.config/opencode/skills/.

## Recommended installation

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent opencode
~~~

Use -g for global installation.

## Manual installation

Copy the complete skill directory, including its references folder, to one of these locations:

- Project: .agents/skills/kaoyan-english-grader/
- Project-native: .opencode/skills/kaoyan-english-grader/
- Global: ~/.config/opencode/skills/kaoyan-english-grader/
- Global Agent Skills: ~/.agents/skills/kaoyan-english-grader/

Do not copy only SKILL.md: the six grading modules are supporting files in the adjacent references directory.

## Use and update

Use OpenCode's native skill tool to list and load kaoyan-english-grader. Update an installation made by the skills CLI with npx skills update kaoyan-english-grader.
