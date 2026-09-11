# Flow: Share Research v1

## Goal
Allow a user to reference research outside the application without losing the identity, version, provenance, or access controls of what was shared.

## Entry points
- `Share` action from a research run.
- `Share` from a specific approved document version.
- `Copy link` from a claim/evidence item for internal discussion.

## V1 sharing modes
1. **Internal run link** — points to the research run and respects normal authorization.
2. **Internal version link** — points to an exact document/report version.
3. **Export** — PDF/Markdown/evidence bundle generated from a specific version.

Guest/public links are future work unless required by deployment policy.

## Happy path: internal share
1. User selects `Share`.
2. System shows the exact object being shared: run or approved document version.
3. User copies a stable URL.
4. Recipient authenticates.
5. Authorization is checked at access time.
6. Recipient opens the same run/version and can inspect evidence according to permissions.

## Happy path: export
1. User selects a document/report version.
2. System generates an export artifact.
3. Export includes stable run ID and document version ID.
4. Export optionally includes a verification/provenance summary.
5. Artifact is hashed and recorded in the run.
6. `document.exported` audit event is recorded.

## External citation pattern
Exports or copied references should make it possible to cite the research itself, for example:

`Research Assurance RUN-... / Document v3 / Claim C17`

The reference is not a substitute for the underlying source citation; it identifies the research process and exact artifact being discussed.

## Access principles
- Sharing never silently broadens organization visibility.
- A stable URL does not imply public access.
- Revoking access does not erase the historical fact that sharing/export occurred.
- Shared links to mutable `current` views should visibly identify the current version and allow inspection of earlier referenced versions.

## Properties implied
- Shared version links resolve to the exact intended version.
- Exported artifacts have content identity/hash and lineage back to the run.
- Authorization is checked when protected links are opened.
- Exports record who/what created them and from which source document version.
- Sharing/export activity is auditable according to policy.

## UX questions to validate visually
- Should `Share` default to run link or approved document version?
- How prominently should recipients see run/version identity?
- What assurance summary belongs in an export without making it look like a compliance certificate?
- Should claim-level deep links be part of v1 or follow shortly after?
