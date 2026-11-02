# Install with the Agent Skills CLI

The repository packages one portable Agent Skill under skills/kaoyan-english-grader. The community skills CLI can install it into the native skill directory for many coding agents, avoiding platform-specific file copying.

## Install interactively

Requires Node.js 22.20 or later.

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader
~~~

Choose one or more detected agents and choose project or global scope.

## Install into selected agents

~~~bash
npx skills add Swcmb/kaoyan-english-grader \
  --skill kaoyan-english-grader \
  --agent claude-code \
  --agent codex \
  --agent cursor \
  --agent opencode \
  --agent gemini-cli \
  --agent antigravity \
  --agent kimi-code-cli \
  --agent qwen-code \
  --agent github-copilot \
  --agent trae \
  --agent windsurf \
  --agent cline
~~~

Use -g for global installation across projects:

~~~bash
npx skills add Swcmb/kaoyan-english-grader \
  --skill kaoyan-english-grader \
  --agent codex \
  --agent opencode \
  --global
~~~

The CLI also supports other agents. Run npx skills add --help for the current supported-agent list and options.

## Update and remove

~~~bash
npx skills check
npx skills update kaoyan-english-grader
npx skills remove kaoyan-english-grader
~~~

## Source and compatibility

The installer reads the skill from the repository's skills/ directory and creates links or copies in each target agent's supported location. Agent-specific capabilities vary; this skill uses only portable Markdown instructions and relative reference files, so it does not require hooks, MCP servers, shell scripts, or host-specific tools.

For native plugin installation methods, see the platform-specific guides linked from the main README.
