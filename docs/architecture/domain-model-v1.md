# Conceptual Domain Model v1

- Status: Draft for contract derivation
- Date: 2026-09-11
- Scope: Product/domain concepts before SQL or API freezing

## 1. Identity and collaboration

### Organization
Owns users, teams, policies, quotas, and protected research.

### Team
Groups users for collaboration and visibility.

### User
Authenticated human identity.

### Membership
Relates User to Organization/Team with a role.

## 2. Research

### ResearchRun
A versioned epistemic investigation.

Key concepts:
- stable ID;
- organization/team/owner;
- originating question;
- visibility;
- state;
- created/updated/completed times;
- component/policy/prompt versions;
- ontology version when applicable;
- assurance summary projection.

### Message
A user/model/system conversational or task message associated with a run.

### Topic
Human- or system-assigned classification metadata used for discovery. Topics are not evidence.

### ResearchTopic
Many-to-many relationship between ResearchRun and Topic with provenance for who/what assigned it.

## 3. Sources and artifacts

### Source
Logical source identity: URL, publication, filing, statute, local document, dataset, etc.

### SourceVersion
Exact observed version used by research.

Key concepts:
- source identity;
- retrieval/ingestion time;
- artifact identity/hash;
- canonical extraction identity/hash;
- parser version;
- valid/known temporal metadata when available;
- lineage to related source versions.

### Artifact
Content-addressed immutable bytes stored outside or alongside the relational database.

### EvidenceSpan
Exact inspectable region of a SourceVersion used to evaluate a claim.

## 4. Claims and verification

### Claim
Atomic epistemic proposition expressed in human-readable text.

Key concepts:
- normalized text;
- claim type;
- epistemic state;
- created/superseded history;
- originating run.

### ClaimIR
Structured intermediate representation of a Claim.

Potential fields:
- subject;
- predicate;
- object/value;
- qualifiers;
- valid time;
- jurisdiction;
- units;
- comparison basis.

Unknown values are permitted.

### ClaimEvidence
Typed relationship between Claim and EvidenceSpan.

Initial relation vocabulary:
- SUPPORTS;
- PARTIALLY_SUPPORTS;
- CONTRADICTS;
- NEUTRAL.

### VerificationResult
Output from a deterministic, symbolic, semantic, policy, or human verification activity.

Key concepts:
- verifier kind;
- verifier/component version;
- result/status;
- explanation;
- structured findings;
- input identities;
- timestamp.

### ClaimRelation
Claim-to-claim relationships such as DERIVED_FROM, DEPENDS_ON, SUPERSEDES.

## 5. Synthesis and documents

### Synthesis
Generated human-readable composition from an allowed claim set.

### Document
Logical deliverable identity associated with a ResearchRun.

### DocumentVersion
Immutable version of a generated or edited deliverable.

Key concepts:
- parent version;
- content/artifact identity;
- contributing claim set;
- creator actor;
- creation/edit activity;
- review state.

## 6. Review

### Review
Human review activity bound to an exact DocumentVersion and/or explicitly scoped claim set.

Possible decisions:
- APPROVED;
- REJECTED;
- CHANGES_REQUESTED;
- APPROVED_WITH_CAVEATS.

### ReviewFinding
Structured reviewer finding referencing a claim, evidence item, source version, or document location.

## 7. Audit and provenance

### AuditEvent
Append-oriented process event describing actor, activity, inputs, outputs, versions, and time.

Actor classes:
- HUMAN;
- MODEL;
- SYSTEM;
- TOOL;
- ADMIN.

### ComponentManifest
Versions/configuration required to interpret a run.

Potential members:
- system version;
- schema versions;
- retriever;
- extractor;
- verifier;
- synthesizer;
- reverse auditor;
- policy;
- prompt pack;
- ontology version;
- frontend/API contract version.

## 8. Sharing and authorization

### Visibility
Initial vocabulary:
- PRIVATE;
- TEAM;
- ORGANIZATION;
- EXPLICITLY_SHARED.

### ShareGrant
Explicit authorization allowing a user/group or share mechanism to access a protected object.

Stable external/internal references must not bypass normal authorization.

## 9. Ontology evolution (future-capable)

### Ontology
Logical ontology identity.

### OntologyVersion
Immutable semantic version used by research or policy.

### OntologyAssertion
Versioned concept/relation/constraint statement with provenance.

### OntologyProposal
Candidate change proposed from research or human work.

Possible proposal actions:
- ADD_CONCEPT;
- ADD_RELATION;
- RENAME_CONCEPT;
- SPLIT_CONCEPT;
- MERGE_CONCEPTS;
- DEPRECATE_CONCEPT;
- CHANGE_PARENT;
- ADD_CONSTRAINT;
- CHANGE_DEFINITION;
- ADD_ALIAS.

Living-ontology objects are not required by Slices 1-6 except that a run must be able to record an ontology version if one participates.

## 10. Conceptual relationship map

```text
Organization
  -> Team
  -> User
  -> ResearchRun
       -> Message
       -> Topic
       -> Source -> SourceVersion -> Artifact
                              -> EvidenceSpan
       -> Claim -> ClaimIR
                -> ClaimEvidence -> EvidenceSpan
                -> VerificationResult
                -> ClaimRelation -> Claim
       -> Synthesis
       -> Document -> DocumentVersion -> Review -> ReviewFinding
       -> AuditEvent
       -> ComponentManifest
       -> optional OntologyVersion

Ontology -> OntologyVersion -> OntologyAssertion
                         -> OntologyProposal
```

## 11. Non-goals for initial contract/schema

Do not add yet unless a slice proves the need:
- canonical cross-run claim merging;
- universal entity registry;
- graph database-specific IDs;
- vector embeddings as first-class domain objects;
- theorem-prover-specific objects;
- distributed job primitives;
- ontology editor state;
- global knowledge-graph layout state.

## 12. Contract derivation rule

API contracts should expose projections required by accepted user flows, while preserving stable IDs that allow drill-down to the canonical domain objects.

The UI is allowed to have lightweight list-item projections such as ResearchRunListItem or ReviewQueueItem; those are views, not new domain entities.