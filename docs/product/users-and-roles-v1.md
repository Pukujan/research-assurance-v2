# Users and Roles v1

- **Status:** Draft
- **Version:** 1.0
- **Date:** 2026-09-11
- **Scope:** Product roles, visibility, collaboration, and audit expectations

## Purpose

Define who uses Research Assurance, what they are trying to accomplish, and which capabilities each role needs. This document describes product behavior, not the final authorization schema.

## Product model

The initial collaboration hierarchy is:

`Organization -> Teams -> Users -> Research Runs`

A research run has an owner and a visibility policy. Team membership affects discovery and review, but does not change the immutable history of the run.

## Roles

### Researcher

Primary job: create, inspect, refine, reuse, and share research.

Needs to:
- start a research run from a question;
- see research progress without reading implementation logs;
- read the resulting report;
- inspect claims, citations, source snapshots, and evidence;
- reopen prior research;
- find related work by teammates when authorized;
- add follow-up questions without destroying the prior run;
- share a stable internal reference or export;
- see what is unverified, disputed, superseded, or awaiting review.

A researcher should not need to understand hashes, model traces, or raw audit JSON during normal work.

### Reviewer

Primary job: decide whether a research result is sufficiently supported for a given use.

Needs everything a researcher can see, plus:
- a queue of runs requiring review;
- the weakest or disputed claims surfaced first;
- direct claim-to-evidence inspection;
- source version and temporal context;
- contradiction and lineage information when available;
- visibility into AI-generated versus human-edited content;
- approve, reject, request changes, or record a caveat;
- leave review notes that become part of the audit trail.

Reviewer approval is a separate event from report generation.

### Organization Admin

Primary job: manage access and reconstruct what happened.

Needs to:
- manage users, teams, roles, and organization policy;
- locate research by user, team, topic, status, date, or run ID;
- inspect complete research dossiers;
- inspect authenticated actor history;
- inspect transcript, tool activity, source snapshots, generated documents, edits, reviews, and approvals;
- verify audit-chain and artifact integrity;
- inspect usage limits and operational failures;
- audit administrative access itself.

Admin capabilities should not clutter the normal researcher interface.

### System Operator

Primary job: operate the deployment without automatically receiving broad research-content privileges.

Needs to:
- observe service health, jobs, storage, migrations, and failures;
- manage deployment configuration and infrastructure;
- inspect operational metadata necessary for support;
- avoid unrestricted content access unless separately authorized.

Infrastructure administration and research-content administration should remain conceptually distinct.

### Guest / Unauthenticated User

The default unauthenticated state should expose no organization research.

Possible future capabilities:
- view an explicitly shared public/guest research artifact;
- verify a signed/exported evidence bundle;
- view a deliberately published report.

Unauthenticated users cannot create organization research, browse the library, inspect private source artifacts, or access audit history.

## Visibility states

Initial research visibility vocabulary:

- `private`: owner plus explicitly authorized reviewers/admins;
- `team`: visible to members of the owning team;
- `organization`: discoverable by organization members;
- `shared`: accessible to explicitly granted users or guest link according to policy.

Cross-organization sharing is out of scope for the first build.

## Collaboration principles

1. Research runs remain independently auditable even when they overlap.
2. Sharing a run does not transfer ownership of its historical actions.
3. Follow-up research creates new attributable events and, where useful, child runs rather than rewriting history.
4. Team discovery should favor reuse over duplication without automatically merging distinct research questions.
5. Comments, reviews, and approvals are attributed actions with timestamps and actor identities.
6. Administrative reads of sensitive dossiers are themselves auditable events.

## UX implications

Researcher navigation should be minimal:

`Research | Library | Reviews (when applicable)`

Reviewer navigation adds review-focused actions and assurance detail.

Admin navigation adds:

`Admin -> Users | Teams | Audit | Policies | Usage`

The signed-in identity should be present but visually quiet. Authentication is a prerequisite, not a dashboard feature.

## Open questions

- Whether reviewer is a persistent role or an assignment on a specific run.
- Whether team-visible research is discoverable by default or opt-in.
- Whether shared guest links can expose evidence/source snapshots or report only.
- Whether comments belong on the whole run, individual claims, or both.
- Whether users can fork a teammate's run into a new independently versioned run.
