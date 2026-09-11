# Flow: Start Research v1

## Goal
A signed-in researcher creates a durable research run from a question and can immediately see that it exists, who owns it, and what state it is in.

## Entry points
- Primary `New Research` action.
- Empty-state prompt on Home/Research.
- Optional future action from a prior run: `Research this further`.

## Happy path
1. Researcher opens `New Research`.
2. Researcher enters a question and optionally attaches local documents.
3. System shows lightweight options only when needed: visibility, team, assurance level.
4. Researcher submits.
5. Server authenticates user and authorizes organization/team context.
6. System creates `ResearchRun` with stable run ID before expensive work begins.
7. System records `run.created` audit event.
8. Run appears in Library immediately with state `Created` or `Queued`.
9. Research workspace opens and shows progress in plain-language stages.
10. Worker begins collection/research according to run policy.

## Progress states
User-facing states should be simpler than internal worker states:
- Created
- Queued
- Researching
- Verifying
- Preparing report
- Complete
- Needs attention
- Failed

## Failure behavior
- Validation failure before run creation: explain inline; no run created.
- Worker failure after run creation: preserve the run and all completed artifacts/events; mark `Needs attention` or `Failed`.
- Quota/concurrency limit: keep the run durable and queued when policy allows.

## What must be visible
- question;
- owner;
- run ID (quietly, copyable);
- created time;
- visibility;
- current state;
- cancellation/retry only when meaningful.

## What must not dominate the screen
- raw tool traces;
- token counts;
- hashes;
- provider internals.

Those belong in Audit/Details.

## Audit events
At minimum:
- `run.created`
- `run.queued` when applicable
- `run.started`
- state transitions
- cancellation/retry actions

## Properties implied
- A run receives a stable identity before asynchronous research work.
- Run creation is attributable to an authenticated actor.
- Failed work does not erase previously created artifacts/events.
- Unauthorized users cannot create runs in another organization/team scope.

## UX questions to validate visually
- Is the initial form one large question box or a modal?
- Where do attachments live without making the start screen busy?
- Should assurance level be explicit or defaulted by policy?
- How much progress detail is useful before it becomes observability noise?
