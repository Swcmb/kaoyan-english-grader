# OpenAI Codex

The repository includes a portable root plugin.json, a Codex compatibility manifest, and a repository marketplace entry.

## Install as a plugin

Add the GitHub repository as a plugin marketplace:

~~~bash
codex plugin marketplace add Swcmb/kaoyan-english-grader
~~~

Then open Codex and run /plugins. Find the kaoyan-english-grader marketplace, select the plugin, and install it. Start a new session after installation.

Update the marketplace metadata with:

~~~bash
codex plugin marketplace upgrade kaoyan-english-grader
~~~

## Install as a standalone skill

Codex discovers skills from the project .agents/skills directory or the user-level ~/.agents/skills directory. The Agent Skills CLI installs the skill into the appropriate location:

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent codex
~~~

Add -g for global installation.

## Verify

Ask Codex to list or invoke kaoyan-english-grader, then submit an English I or English II task. The expected module is loaded from the skill's references directory.
