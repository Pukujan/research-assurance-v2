# Flow: Review Research v1

## Goal
A reviewer can assess a completed or escalated research run, focus on the highest-risk claims, record a decision, and leave an attributable review history.

## Entry points
- `Reviews` queue.
- `Request review` action on a research run.
- Admin/reviewer deep link to a run.

## Review queue
Each item should show only what helps triage:
- research title/question;
- owner;
- requested reviewer/team;
- reason review is required;
- count of disputed/unverified claims;
- age / requested time;
- assurance level.

## Happy path
1. Reviewer opens a queued run.
2. Research report remains the primary reading surface.
3. Review mode highlights claims needing attention first.
4. Reviewer opens a claim inspector and examines evidence.
5. Reviewer may compare support and contradiction side by side.
6. Reviewer may inspect source version, temporal context, lineage, or human edits.
7. Reviewer records one of:
   - approve;
   - approve with caveats;
   - request changes;
   - reject for current intended use.
8. Reviewer may add structured or freeform notes.
9. System records reviewer identity, decision, target report/document version, and time.
10. Research status updates without rewriting prior generated content.

## Review principles
- Review is a decision about a specific version, not a timeless endorsement of the research topic.
- Review approval is separate from AI verification status.
- A reviewer can approve a report containing disclosed uncertainty if policy permits.
- Human edits after approval invalidate or supersede that approval according to policy.

## High-risk focus
Review UI should be able to prioritize:
- disputed claims;
- unsupported or partially supported claims;
- temporal ambiguity;
- source lineage concerns;
- marketing/secondary source dependence;
- large semantic changes introduced during synthesis;
- human edits that strengthen certainty;
- domain-policy warnings.

## Properties implied
- Approval references an exact report/document version.
- Approval identity and timestamp are immutable audit facts.
- Post-approval edits cannot remain silently covered by prior approval.
- Reviewer notes are attributable and versioned/append-only under audit policy.
- The reviewer can always inspect the underlying evidence for claims they are asked to approve.

## UX questions to validate visually
- Does review happen inside the same Research screen or a separate Review workspace?
- Should risky claims be a right-side queue or inline highlights?
- How do caveats appear to later readers?
- Should reviewers be able to mark individual claims reviewed independently of the full report?
