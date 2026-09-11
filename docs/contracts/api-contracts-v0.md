# API Contracts v0

- Status: Draft for fixture frontend
- Date: 2026-09-11
- Source of truth: accepted UX + conceptual domain model + core properties

This document defines the minimum resource projections required to build the fixture-backed frontend. It is not yet a frozen OpenAPI schema.

## 1. Contract principles

- Contracts model durable domain concepts, not individual visual cards.
- List/table projections may be lightweight views of canonical objects.
- Every object exposed to the UI has a stable ID.
- Sorting/filtering never changes object identity.
- Authorization applies to every endpoint and drill-down target.
- Historical/versioned objects are never silently replaced by current state.
- Evidence drill-down must preserve citation -> claim -> evidence -> source-version resolution.

## 2. Initial resource shapes

### ResearchRun

```text
id
organization_id
team_id?
owner
question
title
status
visibility
created_at
updated_at
completed_at?
topics[]
assurance_summary
component_manifest_ref
current_document_version_id?
review_state
```

### ResearchRunListItem

Optimized for Library tables:

```text
id
title
question_excerpt
owner
team?
status
review_state
visibility
topics[]
claim_counts
source_count
updated_at
completed_at?
```

### Claim

```text
id
run_id
text
normalized_text
claim_type
state
ir?
created_at
supersedes_claim_id?
verification_summary
```

### ClaimIR

```text
subject?
predicate?
object_or_value?
qualifiers[]
valid_time?
jurisdiction?
unit?
comparison_basis?
```

Unknown values remain null/absent.

### EvidenceSpan

```text
id
source_version_id
kind
locator
human_excerpt_or_preview_ref
canonical_excerpt
content_hash?
```

### ClaimEvidence

```text
claim_id
evidence_span_id
relation
verification_result_id?
```

Relations:
- SUPPORTS
- PARTIALLY_SUPPORTS
- CONTRADICTS
- NEUTRAL

### SourceVersion

```text
id
source_id
title
source_type
publisher?
url?
retrieved_at
published_at?
valid_from?
valid_to?
artifact_hash
canonical_extraction_hash?
parser_version?
lineage_summary?
```

### DocumentVersion

```text
id
document_id
run_id
version_number
parent_version_id?
content_ref
content_hash
creator
created_at
review_state
```

### ReviewQueueItem

```text
id
run_id
document_version_id
risk_reason
severity
primary_claim_id?
owner
review_state
created_at
updated_at
```

### Review

```text
id
document_version_id
reviewer
status
findings[]
created_at
completed_at?
```

### AuditEvent

```text
id
run_id
sequence
actor_type
actor_display
event_type
summary
created_at
input_refs[]
output_refs[]
component_version?
status
```

### AuditEventDetail

Adds:

```text
payload
input_hashes[]
output_hashes[]
previous_event_hash?
event_hash?
model_metadata?
tool_metadata?
```

## 3. Read operations for fixture frontend

### Identity

```text
GET /api/me
```

### Research / Library

```text
GET  /api/runs
GET  /api/runs/{run_id}
POST /api/runs
```

Suggested list parameters:

```text
q
owner
team
topic
status
review_state
visibility
created_from
created_to
updated_from
updated_to
sort
order=asc|desc
cursor|page
limit
```

Initial sortable Library fields:
- updated_at
- created_at
- completed_at
- title
- owner
- status
- review_state

### Claims and evidence

```text
GET /api/runs/{run_id}/claims
GET /api/claims/{claim_id}
GET /api/claims/{claim_id}/evidence
GET /api/evidence/{evidence_id}
```

### Sources

```text
GET /api/runs/{run_id}/sources
GET /api/source-versions/{source_version_id}
```

### Documents

```text
GET /api/runs/{run_id}/documents
GET /api/document-versions/{document_version_id}
```

### Reviews

```text
GET  /api/reviews
GET  /api/reviews/{review_id}
POST /api/document-versions/{document_version_id}/reviews
```

Suggested queue parameters:

```text
severity
status
owner
team
risk_reason
sort
order
```

### Audit

```text
GET /api/runs/{run_id}/audit
GET /api/audit-events/{event_id}
```

Suggested parameters:

```text
actor_type
event_type
status
from
to
sort=sequence|created_at
order=asc|desc
```

## 4. Minimal write operations for first real slices

### Slice 1

```text
POST /api/runs
```

Creates:
- ResearchRun
- initial AuditEvent

### Slice 2

```text
POST /api/runs/{run_id}/sources
```

Creates:
- Source/SourceVersion as needed
- Artifact reference
- AuditEvent

### Slice 3

Initially internal/system-driven rather than arbitrary client writes:

```text
POST /api/runs/{run_id}/claims:extract
POST /api/claims/{claim_id}/verify
```

These commands may later become job/action resources rather than REST verbs. The fixture frontend does not depend on their final form.

### Slice 4

```text
POST /api/runs/{run_id}/synthesis
```

Produces a new DocumentVersion rather than mutating an existing document.

### Slice 5

```text
POST /api/document-versions/{document_version_id}/reviews
```

Review decisions always bind to the specified immutable document version.

## 5. Evidence inspector composition

The UI should be able to open a citation/claim without several unrelated round trips. Two acceptable implementations:

1. client composes Claim + ClaimEvidence + EvidenceSpan + SourceVersion from separate resources; or
2. backend provides a convenience projection:

```text
GET /api/claims/{claim_id}/inspector
```

Possible InspectorProjection:

```text
claim
evidence[]
source_versions[]
verification_results[]
advanced_provenance_summary
```

This is a projection, not a new canonical entity.

## 6. Ontology contracts

Not required for Slices 1-6.

The only early requirement is that ResearchRun/component metadata can record an ontology version identifier when applicable.

Future contracts may include:

```text
GET  /api/ontology/versions
GET  /api/ontology/versions/{id}
GET  /api/ontology/proposals
POST /api/ontology/proposals
POST /api/ontology/proposals/{id}/reviews
```

Do not implement these until the Living Ontology slice.

## 7. Error and authorization behavior

The API must not leak object existence across tenant/authorization boundaries.

List endpoints return only authorized objects.

Direct object retrieval must apply the same authorization rules as list retrieval.

Stable IDs are references, not capabilities.

## 8. Next contract step

Before freezing OpenAPI/Pydantic models:

1. create realistic fixture datasets using these projections;
2. build the Research, Library, Reviews, and Audit screens against them;
3. identify over-fetching/under-fetching or awkward round trips;
4. revise this document;
5. then convert accepted shapes to Pydantic/OpenAPI and generated TypeScript types.
