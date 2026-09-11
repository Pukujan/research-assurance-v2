# Flow: Inspect Evidence v1

## Goal
A user can move from a statement in the research report to the exact supporting evidence and source version without losing reading context.

## Entry points
- Citation marker in report text.
- Claim status chip.
- Claims tab/list.
- Reviewer risk queue.

## Happy path
1. User reads a factual statement in the report.
2. User selects the citation or claim marker.
3. A contextual inspector opens without replacing the report.
4. Inspector shows the normalized claim and current verification state.
5. Inspector shows exact evidence span(s) and source metadata.
6. User can open a source preview at the relevant page/section/bounding box where available.
7. User can expand `Verification` to see deterministic and semantic checks.
8. User can expand `Provenance` to see source version, retrieval time, parser/version, and artifact identity.
9. User can optionally open full Audit mode for forensic details.

## Default inspector content
- claim text;
- status: `VERIFIED`, `DISPUTED`, `UNVERIFIED`, `INFERENCE`, or `SUPERSEDED`;
- evidence quote or table fragment;
- source title/publisher/type;
- page/section/location;
- snapshot/retrieval time;
- brief explanation of why evidence supports or contradicts the claim.

## Progressive disclosure
Hidden until expanded:
- artifact hash;
- parser version;
- verifier model/version;
- raw structured verifier output;
- lineage graph;
- bitemporal metadata;
- audit-event IDs.

## Source preview
For PDFs/scans/images, the human-review view should prefer the original visual fragment with a highlight when technically available. Machine verification can still operate on a canonical extracted representation.

Human and machine views must resolve to the same source version.

## Multiple evidence items
When a claim has multiple evidence spans:
- show the strongest/direct evidence first;
- label support vs contradiction;
- expose source independence/lineage when available;
- do not imply duplicate syndicated sources are independent confirmation.

## Failure / ambiguity states
- Evidence span missing: claim cannot display as fully verified.
- Source snapshot unavailable: show explicit integrity/access warning.
- Source has a newer version: preserve the cited historical version and optionally indicate a newer version exists.
- Evidence only partially supports claim: status must not be rendered as direct verification.

## Properties implied
- Every visible citation resolves to a registered claim/evidence relation.
- Every evidence span resolves to an immutable source version.
- Source preview and machine evidence representation reference the same source identity/version.
- Missing evidence cannot silently degrade into a normal citation.
- Historical source versions remain addressable after newer versions arrive.

## UX questions to validate visually
- Right drawer, bottom sheet, or split pane on desktop?
- How much source metadata belongs above the fold?
- Should source preview be inline or one click deeper?
- How do support and contradiction coexist without visual overload?
