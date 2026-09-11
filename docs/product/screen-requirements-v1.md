# Screen Requirements v1

- **Status:** Draft
- **Version:** 1.0
- **Date:** 2026-09-11
- **Purpose:** Define the minimum product surfaces to validate visually before API contracts are frozen.

## Design principle

**Research first. Assurance on demand. Audit when needed.**

Normal use should feel like a focused research application, not an observability console. Forensic and provenance detail should be progressively disclosed.

## Global shell

Primary navigation for a researcher:
- Research
- Library
- Reviews (only when relevant)

Additional admin navigation appears only for authorized users.

Global shell also includes:
- search/command entry;
- quiet authenticated identity control;
- organization/team context where needed;
- unobtrusive run/status notifications.

Avoid dashboard KPI cards unless they support a concrete user decision.

## Screen 1: Research Workspace

### Primary purpose
Read and work with one research run.

### Layout
Prefer 2 persistent regions maximum on desktop:
1. main report/workspace;
2. optional contextual inspector drawer.

A third persistent panel should be avoided unless testing shows a clear need.

### Main content
- research question/title;
- run status while active;
- synthesized report/document;
- inline citation/claim markers;
- compact assurance summary;
- follow-up / fork / share actions.

### Tabs or modes
Possible lightweight tabs:
- Answer
- Claims
- Sources

Audit should be a separate mode rather than another always-visible panel.

### Inspector drawer
Opens contextually for citation/claim/source selection and contains:
- claim text/status;
- exact evidence;
- source identity;
- source preview where useful;
- concise verification summary;
- expandable provenance/technical detail.

## Screen 2: Library

### Primary purpose
Find and reopen prior research.

### Layout
1 primary list region plus optional filter bar/side filter. No dashboard mosaic.

### Content
- New Research action;
- search;
- saved/basic filters;
- Active, Needs Review, Recent, Shared with Me groupings or equivalent filters;
- compact rows with title/question, owner, status, updated time, topics.

### Future-friendly metadata
- automatically suggested topics/categories;
- related/overlapping research indicator;
- parent/fork relationships.

These should remain secondary to finding the run.

## Screen 3: Reviews

### Primary purpose
Triage and decide on research requiring human attention.

### Layout
2 regions:
1. queue/list;
2. selected review detail or direct navigation into Research Workspace in Review mode.

### Content
- why review is needed;
- disputed/unverified counts;
- high-risk claim list;
- reviewer actions: approve, approve with caveats, request changes, reject;
- review notes/history.

The review experience should reuse the same claim/evidence inspector as Research rather than inventing a second evidence UI.

## Screen 4: Audit

### Primary purpose
Forensic reconstruction of a run.

### Layout
2 regions preferred, 3 maximum:
1. event table/timeline/trace;
2. selected event details;
3. optional linked artifact preview when needed.

### Content
- run identity and integrity summary;
- filters by actor/action/time/object;
- readable event list;
- actor class and identity;
- input/output references;
- links to transcript messages, claims, source versions, documents, reviews;
- advanced raw metadata behind expansion.

## Screen 5: Admin

### Primary purpose
Organization management rather than research reading.

Subsections may include:
- Users
- Teams
- Roles/Access
- Audit search
- Policies
- Usage / quotas

Admin does not need to be visually elaborate in v1.

## Authentication states

### Authenticated
Normal application shell. Identity is quiet and available from account control.

### Unauthenticated
No private library/research content. Show sign-in or an explicitly authorized shared artifact.

Do not dedicate large dashboard real estate to an `Authenticated` card.

## Visual direction

Current preferred direction:
- dark, low-glare background;
- restrained space/mission-control aesthetic;
- generous spacing;
- subtle luminous accents, not neon everywhere;
- document-first typography;
- occasional orbital/mission metaphors for progress and exploration;
- no dense sci-fi HUD treatment;
- technical metadata uses monospaced typography only when appropriate.

The desired emotional tone is: **research pilot building serious systems with AI**, while remaining calm enough for long reading sessions.

## Reusable UI primitives

Prefer composing screens from a small set of primitives:
1. List
2. Document/report surface
3. Inspector drawer
4. Timeline/trace
5. Command/search bar
6. Status/assurance chip
7. Source preview

Do not create bespoke dashboard widgets when these primitives suffice.

## Panel-count rule

Default:
- 1 primary panel for normal reading/list screens;
- +1 contextual inspector when the user requests detail;
- 3 simultaneous information regions only for explicit forensic/audit workflows.

This rule should be tested during visual generation and fixture prototyping rather than treated as permanent law.

## Questions for the next visual pass

- Can the Research screen remain visually calm while citations are clearly interactive?
- Does the inspector feel like evidence inspection rather than an analytics sidebar?
- Can Library communicate teamwork and topic organization without card overload?
- Does Review make risk obvious without turning every item red/yellow?
- Does Audit feel powerful but intentionally separate from everyday research?
- Can the mission-control aesthetic survive in light mode or should v1 be intentionally dark-first?
