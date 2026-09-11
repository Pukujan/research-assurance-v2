# Flow: Library and Prior Research v1

## Goal
Help users find, reopen, compare, and reuse prior research without turning the library into a metrics dashboard.

## Entry points
- `Library` in primary navigation.
- Search command from the app shell.
- Related-research suggestions from an active run.

## Default view
The library should feel like a calm work list, not an analytics dashboard.

Suggested groups:
- Active
- Needs review
- Recent
- Shared with me

Each row shows only:
- title/question;
- owner;
- updated time;
- current status;
- topic/category chips;
- compact assurance indicator when relevant.

## Search and filters
Initial filters:
- text query;
- owner;
- team;
- topic/category;
- status;
- date range;
- visibility.

Future filters may include domain policy, assurance level, source type, and overlap score.

## Happy path
1. User opens Library.
2. User searches or filters.
3. Results update without losing the user's filter state.
4. User opens a run.
5. Research workspace opens at the preserved run version/current state.
6. User can optionally see related research.

## Team discovery
If authorized, users may discover teammate research.

The UI should make ownership obvious and should never imply the current user created the run.

Suggested views:
- My research
- My team
- Organization
- Shared with me

## Overlap and related research
V1 should not merge overlapping runs.

Future relationships may include:
- shared source overlap;
- shared topic overlap;
- explicit parent/fork relation;
- semantic similarity;
- shared canonical claims.

Any overlap score should be explainable, for example:
`12 shared sources` or `Topics: Tax, Depreciation` rather than an opaque similarity number alone.

## Topic/category auto-allocation
Automatic topic/category allocation may suggest metadata after run creation.

Users must be able to:
- see assigned topics;
- remove incorrect topics;
- add missing topics;
- distinguish suggested/automatic metadata from authoritative user-curated metadata when needed.

Topic assignment should not rewrite the research itself.

## Empty and first-use state
When no research exists, show a strong `New Research` action and a small explanation of what will be preserved: sources, claims, evidence, and audit trail.

## Properties implied
- Library visibility respects authorization scope.
- Opening an older run does not silently regenerate it.
- Ownership and origin remain attributable.
- Related/overlapping research suggestions never destructively merge histories.
- Topic corrections are versioned metadata changes where audit policy requires.

## UX questions to validate visually
- List-first versus card-first layout.
- Whether topic chips should be visible on every row or only on hover/selection.
- Whether Active/Needs Review/Recent are sections or saved filters.
- How much assurance status belongs in the library without becoming visual noise.
