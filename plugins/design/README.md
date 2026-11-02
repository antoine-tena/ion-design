# Le plugin Claude Code `design`

Ce que Claude Code sait faire avec la commande `ion-design` : `/design:…`.

- `.claude-plugin/plugin.json` : son nom et sa description, sans `version` exprès (Claude Code
  suit alors les commits) ; le catalogue qui le publie est `.claude-plugin/marketplace.json`, à
  la racine du dépôt.
- `skills/` : un dossier par skill, nommé d'un verbe (`skills/<verbe>/SKILL.md`, son `name` est
  le nom du dossier). La méthode de design d'un site, en quatre étapes (brief, direction, build,
  polish) : `/design:direction` (squelette) trouve la direction visuelle et en tire les tokens,
  `/design:polish` audite une page sur captures et la corrige, pour tout frontend ; `run` lance
  la commande `ion-design`.
- `references/` : le savoir-faire partagé par les skills (les signes d'un site générique, le
  mouvement selon le niveau).
- Des hooks s'ajoutent dans `hooks/hooks.json`, des serveurs MCP dans `.mcp.json`.

Les sessions ouvertes dans ce dépôt l'activent (`.claude/settings.json`, à l'état de `main`).
Ailleurs : `claude plugin marketplace add antoine-tena/ion-design`, puis
`claude plugin install design@ion-design`.
