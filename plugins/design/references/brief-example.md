# A design brief, for example

An invented hair salon in an invented town: no real business, no real person. The facts (name,
address, hours, keywords) stay in its file; the brief only names their fields.

```markdown
# Brief de design : Atelier Fil d'Or

## Sources

`dossier/dossier.toml`, `photos/` (34 fichiers), `textes/histoire.md`, `references/` (2
captures) ; réponses de la gérante au téléphone le 2026-11-04.

## Audience

1. Les habituées du quartier, 35-60 ans, sur leur téléphone, souvent dans la rue : elles viennent
   prendre rendez-vous ou vérifier si le salon est ouvert. En dix secondes : le bouton de
   réservation et les horaires du jour.
2. Les nouveaux venus à Valbourg, sur ordinateur le soir : ils comparent les salons. En dix
   secondes : le style des coupes, les prix, l'avis des autres clients.
3. Les mariées et leurs proches, quelques fois par an (réponse du 2026-11-04) : l'offre mariage
   et un moyen d'écrire.

## Main action

Réserver en ligne (le lien de réservation de `shop.links`) ; sinon appeler (`shop.phone`).

## Character

- Lumineux, pas clinique.
- Précis, pas froid : le geste de la coupe compte plus que le décor.
- Accueillant, pas familier (`texts.tone` : vouvoiement, complice).

## Fixed and open

Fixe : le logo fourni (`brand.logo`), un fil doré sur fond blanc. Ouvert : la palette
(`brand.palette` : « choisie à la direction »), les polices (`brand.fonts` : « choisies par
nous »).

## Photos

34 photos, dont 20 utilisables en grand : le salon vide au matin (6), les mains au travail (9),
des coupes terminées de dos (5). Aucun visage de client : les consentements manquent
(`photos.consents`). Assez pour une page portée par la photo ; les portraits attendent la séance
du 2026-11-20 (`photos.shoot_date`).

## References

- **Liked** : `brand.liked_sites`. Au téléphone, la gérante ajoute qu'elle aime aussi leurs
  pages presque vides (réponse du 2026-11-04).
- **Sector** : la bibliothèque de l'organisation, secteur beauté.
- **Neighbours** : trois salons de Valbourg ; tous ouvrent sur un diaporama de coupes, un fond
  noir et doré, une liste de prix en tableau. Le défaut à quitter. `brand.avoid` : « le rose ».

## Motion level

2, moderne : `brand.animation_level` vaut « moderne », dans le niveau vendu (`contract.level`
= 2). Question : l'audience 1 lit sur un téléphone pressé, le niveau 1 suffirait-il ?

## To remember

Le geste : des mains qui coupent, en grand, avant tout décor.

## Open questions

- Afficher les prix sur le site, ou « à partir de » ? (`contract.approver`)
- L'offre mariage a-t-elle sa page, parmi les huit de `texts.pages` ? (`contract.approver`)
```
