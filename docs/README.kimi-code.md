# Kimi Code

This repository provides a native Kimi plugin manifest at kimi.plugin.json. It packages the portable skill directory and supporting references.

## Install from GitHub

In Kimi Code, run:

~~~text
/plugins install https://github.com/Swcmb/kaoyan-english-grader
/reload
~~~

You can also start a new session after installation. The plugin is installed at user scope and the skill is listed under the plugin namespace.

## Use as a standalone Agent Skill

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent kimi-code-cli
~~~

Add -g for global installation when using the Agent Skills CLI.

## Verify

Use the skill selector or ask Kimi Code to grade a specific English I/II translation or essay. The loaded skill should read the corresponding module from the adjacent references directory.
