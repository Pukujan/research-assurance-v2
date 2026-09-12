# UX Visual Archive

This directory preserves the generated UX visual references used during Research Assurance v2 product discovery.

## Authority

The images are **design references, not normative specifications**.

The authoritative v1 structural UX decisions live in:

- `docs/product/ux-acceptance-v1.md`
- `docs/product/screen-requirements-v1.md`

If an image conflicts with those documents, the written acceptance decisions win.

## Accepted v1 direction

`accepted-v1-direction.webp` is the latest visual direction that received positive human acceptance ("looks pretty good") before the project moved from broad UX exploration into specification.

It represents the intended overall feel:

- dark, low-glare, spacious UI;
- Research / Library / Reviews / Audit as the main surfaces;
- Research is document-first;
- Library, Reviews, and Audit use tables when appropriate;
- sorting/filtering are first-class table behavior;
- evidence/details are progressively disclosed rather than permanently occupying the screen;
- no KPI-heavy or mission-control dashboard as the normal workspace.

Do not treat every visual detail in this image as frozen. Typography, exact spacing, component implementation, mobile behavior, and detailed column choices remain implementation-level decisions.

## Historical generated images

The original generated images from the product-design conversation were recovered and hashed. Their metadata is in `manifest.json`.

The historical set includes early dashboard concepts, audit-focused concepts, mission-control/cosmic experiments, the UX concept board, and later simplified dark-mode composites. Several of those earlier concepts were explicitly rejected as too busy and are retained only as design history.

The repo intentionally does not make rejected visual concepts authoritative merely because they are archived.

## Provenance

The accepted image is a compressed WebP derivative of the generated image originally named:

`a_wide_dark_mode_ui_ux_dashboard_mockup_collage_i.png`

Original SHA-256:

`d006954d1890db5efea9a8ff2146ffdf8229dd29f03c15c25cd8d4278bce4c83`

The original was 1536x1024. Compression is only for repository convenience; the original hash remains recorded in `manifest.json`.

## Future rule

When a generated visual materially changes an accepted product decision:

1. archive the visual or a repository-sized derivative;
2. record its source hash/provenance;
3. update the written UX acceptance decision;
4. treat the written acceptance decision as authoritative;
5. keep superseded visuals as historical references rather than silently replacing them.
