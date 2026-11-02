# Claude Code

This repository is packaged as a Claude Code plugin and as a standalone Agent Skill.

## Install as a plugin

Open Claude Code and run:

~~~text
/plugin marketplace add Swcmb/kaoyan-english-grader
/plugin install kaoyan-english-grader@kaoyan-english-grader
~~~

Start a new Claude Code session after installation.

## Install as a standalone skill

Use the Agent Skills CLI:

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent claude-code
~~~

This installs the skill into the current project's Claude skills directory. Add -g to install globally.

## Verify

Ask Claude Code to grade a specific English I/II translation or essay and confirm that it loads kaoyan-english-grader and the matching file under references/.
