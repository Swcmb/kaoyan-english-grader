# Gemini CLI and Qwen Code

The repository contains a Gemini CLI extension manifest and a GEMINI.md context file that loads the portable skill.

## Gemini CLI

Install from GitHub:

~~~bash
gemini extensions install https://github.com/Swcmb/kaoyan-english-grader
~~~

Restart Gemini CLI after installation. To refresh the extension later:

~~~bash
gemini extensions update
~~~

Check installed extensions with /extensions list.

## Qwen Code

Qwen Code supports Gemini CLI extensions and converts their manifest and context files during installation:

~~~bash
qwen extensions install Swcmb/kaoyan-english-grader
~~~

Restart Qwen Code after installation. To see the available extension commands, run qwen extensions --help.

## Standalone Agent Skill

Both tools are also supported by the Agent Skills CLI:

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent gemini-cli
~~~

Use -a qwen-code only when that agent identifier appears in the installed skills CLI's current supported-agent list.
