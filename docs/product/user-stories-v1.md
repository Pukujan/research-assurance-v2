# User Stories v1

- **Status:** Draft
- **Version:** 1.0
- **Date:** 2026-09-11
- **Scope:** Core jobs to be validated before API contracts are frozen

## Purpose

These stories define what the product must let people accomplish. They are intentionally phrased in user terms rather than implementation terms.

## Researcher stories

### US-R01 Start research
As a researcher, I can enter a question and create a durable research run so that the work has a stable identity from the first action.

**Success:** the run appears in my library immediately and its creation is auditable.

### US-R02 Observe progress
As a researcher, I can see whether a run is queued, collecting sources, extracting claims, verifying, synthesizing, complete, or failed without reading raw logs.

**Success:** progress communicates state and actionable failures without exposing implementation noise.

### US-R03 Read the result
As a researcher, I can read the synthesized research as the dominant object on the page.

**Success:** assurance detail remains available without overwhelming the report.

### US-R04 Inspect a citation
As a researcher, I can select a cited statement and see the supporting claim, exact evidence, source identity, and source snapshot/version.

**Success:** I can understand why the citation supports the sentence without navigating away from the report.

### US-R05 Understand uncertainty
As a researcher, I can distinguish verified, disputed, unverified, inference, superseded, and review-needed content.

**Success:** the interface does not imply uniform confidence or certainty.

### US-R06 Reopen prior work
As a researcher, I can search and filter prior research by text, owner, topic, category, date, and status.

**Success:** prior work is reusable rather than hidden in chat history.

### US-R07 Discover teammate work
As a researcher, I can discover authorized teammate research relevant to my question.

**Success:** the system encourages reuse but never silently merges separate runs.

### US-R08 Continue or fork research
As a researcher, I can ask a follow-up or create a new child/forked run while preserving the prior result and its audit trail.

**Success:** historical state remains inspectable.

### US-R09 Share research
As a researcher, I can share a stable internal link or export a versioned report that references the originating research run.

**Success:** recipients can identify which exact run/document version is being discussed.

### US-R10 See related research
As a researcher, I can see suggested related runs based on shared topics, sources, or future overlap detection.

**Success:** suggestions are advisory and explain the relationship where possible.

## Reviewer stories

### US-V01 Review queue
As a reviewer, I can see runs that need my attention and why they need review.

### US-V02 Focus on risk
As a reviewer, I can start with disputed, unsupported, temporally ambiguous, or manually escalated claims rather than rereading everything linearly.

### US-V03 Inspect evidence chain
As a reviewer, I can move from report sentence -> claim -> evidence -> source version -> provenance without losing context.

### US-V04 Compare source positions
As a reviewer, I can see supporting and contradicting evidence side by side when both exist.

### US-V05 Review human edits
As a reviewer, I can identify changes made by humans after AI generation, including semantic strengthening or qualifier removal.

### US-V06 Approve with attribution
As a reviewer, I can approve, reject, request changes, or approve with caveats, and that action is recorded separately from generation.

## Admin stories

### US-A01 Locate a run
As an admin, I can find a research run by run ID, user, team, topic, status, date, or document reference.

### US-A02 Reconstruct activity
As an admin, I can reconstruct who asked what, what models/tools ran, what sources were seen, what claims were produced, and what final document was approved.

### US-A03 Verify integrity
As an admin, I can verify stored artifact hashes, document versions, audit-chain continuity, and missing references.

### US-A04 Audit access
As an admin, I can see who viewed or exported sensitive research dossiers.

### US-A05 Manage access
As an admin, I can manage organization membership, team membership, roles, and visibility policy.

### US-A06 Inspect usage
As an admin, I can see queued work, quotas, model/token usage, failures, and expensive runs without exposing secrets in logs.

## Guest / unauthenticated stories

### US-G01 Sign in boundary
As an unauthenticated visitor, I cannot browse private organization research and I am clearly directed to authenticate when necessary.

### US-G02 Verify shared artifact (future)
As a guest with an authorized share link, I can view exactly the version that was shared and, where policy permits, inspect its provenance summary.

## Cross-cutting stories

### US-X01 Stable identity
Every research run, claim, source version, and document version that may be referenced outside the immediate screen has a stable identifier.

### US-X02 Bitemporal awareness
Where time matters, the interface can distinguish when information was valid from when the system learned or recorded it.

### US-X03 Topic/category management
Research may be automatically assigned topics/categories, but users can inspect and correct them. Automatic classification is metadata, not hidden truth.

### US-X04 Overlap without destructive merging
When two runs share sources/topics or later appear semantically overlapping, the system can surface the relationship while preserving both histories.

### US-X05 Progressive disclosure
Normal users see the report first; assurance and forensic detail appears contextually or in explicit audit/review modes.

## Initial priority

The first walking product should satisfy, in order:

1. US-R01 Start research
2. US-R06 Reopen prior work
3. US-R04 Inspect a citation
4. US-R03 Read the result
5. US-A02 Reconstruct activity
6. US-V03 Inspect evidence chain
7. US-R09 Share research

The remaining stories should influence the data model only where failing to anticipate them would force destructive redesign later.
