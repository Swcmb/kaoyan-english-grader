# Google Antigravity

The repository includes an Antigravity plugin manifest at .antigravity-plugin/plugin.json and a standard Agent Skill under skills/.

## Install as a plugin

~~~bash
agy plugin install https://github.com/Swcmb/kaoyan-english-grader
~~~

Verify the installation:

~~~bash
agy plugin list
~~~

To validate a local checkout before installing:

~~~bash
agy plugin validate --strict ./kaoyan-english-grader
agy plugin install ./kaoyan-english-grader
~~~

## Install as a standalone skill

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent antigravity
~~~

Use -g for global installation.
