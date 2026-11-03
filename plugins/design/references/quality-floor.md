# The quality floor

What every page meets without being asked, and what a session forgets when it looks only at the
design. Checked by the build, again by `/design:polish`. Drawn from the UX rules of
ui-ux-pro-max (MIT), kept to those a showcase site needs.

- **Contrast**, computed on the tokens, not judged on screen: body text 4.5:1 on its background,
  large text (24 px, or 19 px bold) 3:1, focus outline and control borders 3:1. A pale accent
  (brass, sand, pastel) is often under 3:1 on a light background: never the focus colour there,
  and never the only sign of a link.
- **Keyboard**: focus visible on every background of the site, in an order that follows the page.
- **Touch targets** 44 × 44 px at least, links included (a phone number, an underlined link, the
  header button): `min-h-11` and `inline-flex items-center` rather than a bigger font.
- **Images**: width and height known (Astro's `<Image />`, or the attributes), so the page does
  not jump as it loads; the first image `loading="eager"` and `fetchpriority="high"`, the others
  lazy; `sizes` that match the layout; an `alt` that says what the photo shows, empty when it
  only decorates.
- **Motion** behind `prefers-reduced-motion`: the page reads complete without it.
- **Widths**: 375 px with no horizontal scroll, then 768, 1 024 and 1 440 px; text lines under 80
  characters.
- **Icons**: SVG from one family and one stroke, never emoji; an icon alone in a button has an
  `aria-label`.
- **Forms**: a visible `<label>` per field (a placeholder is not one), the error next to its
  field, saying how to fix it.
