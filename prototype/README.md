# Fixture-backed prototype

This is a no-build static prototype for validating Research Assurance v0 contracts and interaction flow before a production backend exists.

## Run locally

From the repository root:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/prototype/
```

Do not open `index.html` directly with `file://`; the prototype fetches JSON from `fixtures/v0/`.

## Implemented interactions

- **Research**: readable report, assurance summary, inline claim citations, claim/evidence/source inspector, claim and source projections, object-linked discussion.
- **Library**: text search, owner/status/review filters, ascending/descending updated-time sort, stable run IDs, row drill-down.
- **Reviews**: severity/state filtering, exact `DocumentVersion` binding, finding detail, claim drill-down for the main fixture.
- **Audit**: actor/status filtering, chronological event table, raw event payload/hashes behind a detail drawer.

## Deliberate limitations

- Fixture-only; no persistence or authentication.
- New comments exist only in browser memory.
- Only `run_grid_001` has a complete dossier; other Library rows demonstrate discovery/filter/sort behavior.
- No general team chat. Collaboration is scoped to research objects.
- Ontology editing and living-ontology workflows are not part of this slice.

## What this prototype should tell us

Use it to identify awkward resource boundaries, missing fields, over-fetching, and UI interactions before freezing `docs/contracts/api-contracts-v0.md` into OpenAPI/Pydantic models.
