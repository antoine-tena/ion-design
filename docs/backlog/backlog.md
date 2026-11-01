# Backlog

Everything left to do on design, in a single list ordered by priority. Started on
**2026-10-29**. How to write a ticket: [README.md](README.md); closed tickets are in
[done.md](done.md), what was turned down in [rejected.md](rejected.md). **Nothing else is open.**

North star: **Un design juste pour chaque site**.

**Next free: ion-design#T-04.**

---

## 🔴 Critical

### ion-design#T-03 · Finish the ion-repo update to v0.4.11
- **Type**: task
- **Status**: todo
- **Opened**: 2026-11-01
- **Effort**: XS · **Owner**: — · **Due**: —
- **Origin**: release notes of the ion-repo releases crossed (`ion repo update`)

What ion-repo cannot guess, to fill in right after the update (`/repo:update`):
- [ ] run `ion repo install --machine` once on each machine, so that its Claude Code catalogue moves from kiln to ion-repo. (v0.4.11)

## 🟠 Important

### T-01 · Reprendre de ion-repo l'audit visuel `/nuxt:polish`
- **Type**: task
- **Status**: blocked — waiting for ion-repo T-394 (comment un outil arrive dans un repo)
- **Opened**: 2026-10-30
- **Effort**: S · **Owner**: — · **Due**: —
- **Origin**: décision d'antoine du 2026-10-30, répartir ce que ion-repo porte hors de son métier

`plugins/nuxt/skills/polish/` de ion-repo critique une page « comme un directeur artistique » : du
design pur, seule une partie du chemin est propre à Nuxt.

- [ ] Le skill `/design:polish`, valable pour tout frontend, plus seulement Nuxt.
- [ ] Il dépend du serveur MCP Playwright du plugin `nuxt` et de `/nuxt:preview`, qui restent
  dans ion-repo (voir une page est de la technique) : décider ce que ion-design appelle quand le plugin
  `nuxt` n'est pas là.

Côté ion-repo : T-391.

## 🟡 Normal

## ⚪ Background — long-running work, debt and ideas

### T-02 · Quand passer par un canevas plutôt que par la page réelle
- **Type**: idea
- **Status**: open
- **Opened**: 2026-10-30
- **Effort**: S · **Owner**: — · **Due**: —
- **Origin**: session annski du 2026-10-30, retouche de la fenêtre de nouveautés dans `/workspace`

Retoucher un écran qui existe se fait sur la page réelle (le `/workspace` d'annski) : vrais
composants, vrai CSS, vraies données, rien à retraduire. Le canevas (Artifact « Design » de
claude.ai) est une page à part, sans les composants ni le CSS du site, à réécrire une fois
validée. Il sert dans d'autres cas :

- [ ] explorer une idée avant tout code (une page qui n'existe pas encore) ;
- [ ] comparer 3 directions visuelles côte à côte ;
- [ ] envoyer un lien au bureau (ou au client) pour qu'il commente sans lancer le site.

Écrire cette règle là où ion-design guide le travail visuel (règle ou skill), pour que chaque session
choisisse d'elle-même.
