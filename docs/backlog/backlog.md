# Backlog

Everything left to do on design, in a single list ordered by priority. Started on
**2026-10-29**. How to write a ticket: [README.md](README.md); closed tickets are in
[done.md](done.md), what was turned down in [rejected.md](rejected.md). **Nothing else is open.**

North star: **Un design juste pour chaque site**.

**Next free: ion-design#T-11.**

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

### ion-design#T-06 · Décider si un agent peut lancer `/design:brief` et `/design:direction`
- **Type**: task
- **Status**: todo
- **Opened**: 2026-11-02
- **Effort**: XS · **Owner**: — · **Due**: —
- **Origin**: répétition du salon fictif « Les Ciseaux de Lorvane », `ion-repo-sandbox/neufs/salon/`, 2026-11-02

Les deux skills portent `disable-model-invocation: true` : un agent qui déroule la chaîne (dossier,
brief, direction) ne peut pas les lancer, il lit `SKILL.md` à la main, ce qu'a fait la répétition.
Décider : retirer l'option, ou la garder et le dire dans le README du plugin. L'activation du
plugin dans le site d'un client : ion-repo#T-420.

### ion-design#T-07 · `/design:direction` ne dit pas où vivent les mini-pages ni ce qu'on en garde
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-11-02
- **Effort**: S · **Owner**: — · **Due**: —
- **Origin**: répétition du salon fictif « Les Ciseaux de Lorvane », `ion-repo-sandbox/neufs/salon/`, 2026-11-02

L'étape 3 demande de vraies mini-pages, l'étape 5 un seul fichier de tokens. Sur un site Astro
d'ion-repo, la règle [STYLE-3] veut tous les tokens dans `global.css` : la répétition a mis les
deux pistes en tokens préfixés (`--color-a-*`, `--color-b-*`), les pages dans
`frontend/src/pages/directions/`, puis a tout retiré après le choix et gardé les captures dans
`design/directions/` et le récit dans `design/direction.md`, un fichier que le skill ne nomme
pas. Rien de cela n'est écrit : chaque session inventera autre chose, et l'étape build
(ion-design#T-05) a besoin de savoir ce qu'elle reçoit.

- [ ] Où construire les mini-pages, comment leurs tokens cohabitent avec le fichier unique.
- [ ] Ce qui reste après le choix : `design/direction.md` (pistes, choix, raisons du client, date),
  les captures, et le sort des mini-pages (supprimées, ou gardées comme première section du build).
- [ ] Une branche pour brief et direction, ou une chacun (la répétition en a pris une seule,
  `design/brief`).

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

### ion-design#T-08 · Captures : Playwright non épinglé, barre d'outils d'Astro, PNG trop lourds
- **Type**: bug
- **Status**: todo
- **Opened**: 2026-11-02
- **Effort**: S · **Owner**: — · **Due**: —
- **Origin**: répétition du salon fictif « Les Ciseaux de Lorvane », `ion-repo-sandbox/neufs/salon/`, 2026-11-02

Trois accrocs en capturant les pistes (méthode de `/design:polish`, reprise par
`/design:direction`) :

- `npx playwright screenshot` prend la dernière version, dont le navigateur n'est pas dans
  `~/.cache/ms-playwright` : « Executable doesn't exist … chromium_headless_shell-1200 ». Il a
  fallu chercher la version qui va avec le cache (`playwright@1.64`).
- Sur `astro dev`, la barre d'outils d'Astro apparaît au milieu de chaque capture : capturer
  `astro build` puis `astro preview`, ou couper `devToolbar`.
- Une capture pleine page d'ordinateur en PNG dépasse 1 Mo et le hook `check-added-large-files`
  refuse le commit : les garder en JPEG, ou hors de git.

Reproduire : `astro dev --background` dans le site, `npx -y playwright screenshot
--viewport-size=1440,900 --full-page http://localhost:4321/ x.png`.

### ion-design#T-09 · Où mettre l'espacement et le niveau de mouvement dans les tokens
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-11-02
- **Effort**: XS · **Owner**: — · **Due**: —
- **Origin**: répétition du salon fictif « Les Ciseaux de Lorvane », `ion-repo-sandbox/neufs/salon/`, 2026-11-02

L'étape 5 range « couleurs, polices, échelle d'espacement et niveau de mouvement » dans le fichier
de tokens. Avec Tailwind 4 (`@theme`), couleurs et polices ont leur espace de noms ;
l'espacement garde `--spacing`, et le niveau de mouvement n'en a aucun : la répétition a inventé
`--motion-level: 2`, que rien ne lit. Dire la convention (nom, et qui le lit au build).

### ion-design#T-10 · Le brief sans sites aimés ni voisins réels
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-11-02
- **Effort**: XS · **Owner**: — · **Due**: —
- **Origin**: répétition du salon fictif « Les Ciseaux de Lorvane », `ion-repo-sandbox/neufs/salon/`, 2026-11-02

Le salon n'avait ni site aimé (`brand.liked_sites` : sans objet), ni bibliothèque par secteur, ni
voisins à regarder : la rubrique References du modèle n'a rien dit, et `/design:direction` n'a
rien eu à capturer à son étape 1. Cas courant chez un petit commerçant. Dire quoi faire alors :
chercher soi-même deux ou trois voisins de la même ville (et lesquels), ou partir des seuls mots
du client, en le notant comme hypothèse.

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
