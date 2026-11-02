# Backlog

Everything left to do on design, in a single list ordered by priority. Started on
**2026-10-29**. How to write a ticket: [README.md](README.md); closed tickets are in
[done.md](done.md), what was turned down in [rejected.md](rejected.md). **Nothing else is open.**

North star: **Un design juste pour chaque site**.

**Next free: ion-design#T-06.**

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

### ion-design#T-05 · L'étape build de la méthode de design
- **Type**: task
- **Status**: todo
- **Opened**: 2026-11-02
- **Effort**: M · **Owner**: — · **Due**: —
- **Origin**: generateur.md d'Ember Studio, « Notre méthode, en quatre étapes », point 3

Les pages s'assemblent à partir d'une bibliothèque de sections qui suivent les tokens. Cette
bibliothèque n'existe pas encore et la part propre à une structure reste privée chez elle :
attendre l'essai qui la fait naître. Cet essai est la répétition sur un salon fictif, dans
ion-repo-sandbox, pas un vrai client : dossier rempli, `ion deal check` puis `ion deal new`,
`/design:brief`, `/design:direction`, puis le build.

- [ ] Ce que l'outil porte (comment une section lit les tokens, comment choisir et ordonner les
  sections d'une page) et ce que la bibliothèque d'une structure garde.
- [ ] Le skill `/design:build`, entre `/design:direction` et `/design:polish`.

## 🟡 Normal

## ⚪ Background — long-running work, debt and ideas

### ion-design#T-02 · Quand passer par un canevas plutôt que par la page réelle
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
