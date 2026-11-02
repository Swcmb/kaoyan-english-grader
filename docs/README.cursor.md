# Cursor

The repository includes both the portable Agent Plugin manifest (plugin.json) and Cursor-specific manifest (.cursor-plugin/plugin.json).

## Install locally for evaluation

Clone the repository:

~~~bash
git clone https://github.com/Swcmb/kaoyan-english-grader.git
~~~

Copy the complete repository into Cursor's local plugin directory:

- macOS/Linux: ~/.cursor/plugins/local/kaoyan-english-grader
- Windows: %USERPROFILE%\.cursor\plugins\local\kaoyan-english-grader

Keep plugin.json, .cursor-plugin/plugin.json, skills/, and the other repository files together. Restart Cursor or run Developer: Reload Window, then verify the plugin in Customize.

## Install as a standalone skill

~~~bash
npx skills add Swcmb/kaoyan-english-grader --skill kaoyan-english-grader --agent cursor
~~~

Add -g for global installation.

## Marketplace distribution

Cursor installs Agent Plugins and Cursor Plugins from a marketplace. To distribute this plugin through the public Cursor Marketplace, submit the repository for review at cursor.com/marketplace/publish. Team marketplaces can distribute the plugin within an organization.
