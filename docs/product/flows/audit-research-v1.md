# Flow: Audit Research v1

## Goal
Allow an authorized reviewer/admin to reconstruct exactly what happened during a research run without making forensic detail part of the normal research experience.

## Entry points
- `Audit` action from a research run.
- Admin search by run ID, user, date, topic, document ID, or status.
- Integrity warning or review escalation.

## Audit layout
Audit mode is a specialized view with three coordinated regions:
1. searchable/filterable event list or trace;
2. selected event details;
3. links back to the affected research artifact, claim, source, message, or document version.

The normal report is not replaced as the canonical research view; Audit is a forensic projection over the same run.

## Happy path
1. Authorized user opens Audit for a run.
2. System shows run identity, owner, policy/pipeline versions, start/end times, and integrity summary.
3. Auditor filters by actor, action, object, time, or severity.
4. Auditor selects an event.
5. Detail panel shows actor, action, timestamp, relevant input/output object IDs/hashes, and structured metadata.
6. Auditor follows links to exact transcript message, source snapshot, claim, document version, or review decision.
7. Auditor can verify the event chain and artifact integrity summary.
8. Any export/download of the dossier is itself recorded when policy requires.

## Actor classes
- `HUMAN`
- `MODEL`
- `SYSTEM`
- `TOOL`
- `ADMIN`

Actor identity must be supplied by trusted application context, not by model-generated metadata.

## Minimum event families
- authentication/session events relevant to the run;
- run creation and state transitions;
- search/tool calls and results;
- source retrieval/snapshot/version events;
- parsing/extraction events;
- claim proposal and verification events;
- synthesis and reverse-audit events;
- human edits;
- review/approval/rejection events;
- document export/share events;
- admin dossier views/exports when sensitive.

## Default presentation
The event list should emphasize readable summaries:
`09:14:11 MODEL proposed claim C12`

Raw JSON, hashes, token counts, and provider response metadata appear only in the detail panel or advanced view.

## Integrity summary
At minimum show:
- audit-chain status;
- referenced artifact availability;
- artifact hash verification;
- missing/broken references;
- document lineage status;
- policy/pipeline version identity.

## Properties implied
- Every audit event is attributable to a trusted actor identity/type.
- Events are append-oriented and historically reconstructable.
- Audit detail can resolve to the exact referenced object/version.
- Admin access to sensitive dossiers can itself be audited.
- The audit UI cannot silently substitute current source content for the historical snapshot used by the run.

## UX questions to validate visually
- Timeline versus table versus trace as default.
- Whether event families should be color-coded or rely mostly on icons/labels.
- How to surface integrity warnings without creating an alarm-heavy interface.
- Whether model/tool events should collapse into higher-level stages by default.
