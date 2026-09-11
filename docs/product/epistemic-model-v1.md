# Epistemic Model v1

- **Status:** Draft
- **Version:** 1.0
- **Date:** 2026-09-11
- **Scope:** Conceptual model for research, claims, evidence, provenance, synthesis, review, and audit

## 1. Purpose

Research Assurance does not treat a research run as one opaque answer with one confidence score. A research run is a versioned epistemic investigation composed of claims, evidence, provenance, synthesis, review state, and process history.

The central distinction is:

- **ResearchRun = epistemic investigation/case**
- **Claim = epistemic atom/proposition**
- **EvidenceSpan = exact observable support or contradiction**
- **EvidenceEdge = typed justification relationship**

The system should make it possible to answer both:

1. **Process question:** What happened, who/what did it, and when?
2. **Epistemic question:** Why should a particular conclusion be believed, disputed, qualified, or rejected?

These are related but not interchangeable.

## 2. Core conceptual graph

```text
ResearchRun
│
├── Question
│
├── Source
│    └── SourceVersion
│          └── EvidenceSpan
│
├── Claim
│    ├── supported_by ───────> EvidenceSpan
│    ├── contradicted_by ────> EvidenceSpan
│    ├── partially_supported_by -> EvidenceSpan
│    ├── derived_from ───────> Claim
│    ├── supersedes ─────────> Claim
│    └── depends_on ─────────> Claim
│
├── Synthesis
│    └── references ─────────> Claim
│
├── DocumentVersion
│    └── produced_from ──────> Claim set + Synthesis
│
├── Review
│    └── binds_to ───────────> DocumentVersion
│
└── AuditEvent
     └── records ────────────> actor + activity + inputs + outputs
```

This is a semantic graph even if the initial implementation uses SQLite tables and ordinary foreign keys.

## 3. ResearchRun

A `ResearchRun` is an independent epistemic case.

It identifies at minimum:

- stable run ID;
- originating question or task;
- authenticated user and organization/team context;
- creation time;
- visibility/access scope;
- run state;
- pipeline/component versions;
- applicable policy profile;
- links to sources, claims, documents, reviews, and audit events.

A run remains independently attributable and auditable even when it overlaps heavily with another run.

### 3.1 No single truth/confidence score

The application must not collapse a run into a universal number such as `92% confidence`.

A more meaningful run summary is compositional, for example:

```text
24 VERIFIED claims
3 INFERENCE claims
2 DISPUTED claims
11 independent evidence roots
1 unresolved contradiction
Human review: pending
```

The run-level state is therefore an aggregation/projection over lower-level epistemic objects, not a primitive truth score.

## 4. Claim

A `Claim` is the primary epistemic unit.

A claim should be atomic enough that evidence can support, partially support, contradict, or fail to address it without relying on unrelated propositions bundled into the same sentence.

Illustrative claim types:

- reported fact;
- calculated fact;
- historical fact;
- causal claim;
- interpretation;
- forecast;
- legal conclusion;
- clinical result;
- geospatial observation;
- inference.

Initial claim states:

- `VERIFIED`
- `DISPUTED`
- `UNVERIFIED`
- `INFERENCE`

These states summarize verification results under a particular policy/version. They are not timeless declarations of truth.

### 4.1 Claim identity and history

Claims may be versioned or superseded rather than silently overwritten.

Later versions may:

- narrow or broaden wording;
- add/remove qualifiers;
- correct numeric values;
- reflect new source versions;
- respond to contradiction/retraction;
- preserve lineage to the earlier claim.

For v1, independent runs may contain semantically duplicate claims. Automatic canonical claim merging is explicitly not required.

Incorrectly merging two claims is more dangerous than temporarily retaining duplicates.

## 5. Source and SourceVersion

A source identity and an observed source version are different concepts.

`Source` describes the logical origin, such as a URL, filing, publication, statute, internal document, or dataset.

`SourceVersion` describes the exact observed artifact used in a run.

A source version should be able to identify:

- source identity;
- retrieval/ingestion time;
- original artifact hash;
- canonical extraction hash;
- parser/extractor version;
- publication/effective/observation time when known;
- response headers or version identifiers where useful;
- lineage to earlier/later source versions where known.

The system should be able to say not merely "we used this URL," but "we used this exact observed representation."

## 6. EvidenceSpan

An `EvidenceSpan` is an exact region of a source version used to evaluate a claim.

A human-facing representation may be:

- highlighted PDF text;
- a page/table crop;
- a web-page passage;
- a spreadsheet cell/range;
- a filing section;
- a map feature/geometry;
- another inspectable fragment.

A machine-facing representation should resolve to the same source version and may contain:

- canonical text offsets;
- page/block coordinates;
- table/row/cell identifiers;
- byte/content hashes;
- structured field paths;
- parser version.

High-assurance review should expose both the human-verifiable original representation and machine-verifiable canonical representation where feasible.

## 7. EvidenceEdge

Evidence relationships must be typed. Citation existence alone does not imply support.

Initial semantic relations:

- `SUPPORTS`
- `PARTIALLY_SUPPORTS`
- `CONTRADICTS`
- `NEUTRAL`

Additional graph relations may include:

- `DERIVED_FROM`
- `DEPENDS_ON`
- `SUPERSEDES`
- `QUOTES`
- `COPIED_FROM`
- `CITES`
- `SAME_ENTITY_AS`

An evidence edge may carry verifier output such as:

- relation;
- missing qualifiers;
- entity/date/unit mismatch;
- semantic escalation warning;
- verifier/policy version;
- explanation suitable for reviewer inspection.

## 8. Proof obligations and policy

Different claim types require different proof obligations.

The core system should not pretend that one generic entailment check is enough for every domain.

Examples:

### 8.1 Reported numeric fact

Possible obligations:

- correct entity;
- correct reporting period;
- correct currency/unit/scale;
- matching value;
- appropriate source role.

### 8.2 Calculated fact

Possible obligations:

- verified input claims;
- recorded formula;
- reproducible deterministic calculation;
- unit compatibility.

### 8.3 Legal claim

Possible obligations:

- correct jurisdiction;
- correct authority type;
- correct effective version/date;
- holding/text relevance;
- amendment/supersession awareness.

### 8.4 Medical claim

Possible obligations:

- population;
- intervention;
- comparator;
- outcome;
- study design;
- effect measure;
- sample size;
- uncertainty/confidence interval;
- correction/retraction state.

Domain policy therefore changes verification requirements while preserving the same core epistemic model.

## 9. Source independence and lineage

Multiple citations do not necessarily mean multiple independent evidence roots.

Example:

```text
Company press release
        ↓
      Wire story
      ↙      ↘
 News A      News B
```

Three downstream articles may represent one underlying information origin.

The system should preserve lineage where known so later assurance logic can reason about independent roots rather than raw citation count.

Source independence is therefore a graph property, not a count of URLs.

## 10. Synthesis

Synthesis is downstream of registered claims.

Preferred conceptual flow:

```text
sources
  ↓
evidence
  ↓
claims
  ↓
verification
  ↓
allowed claim set
  ↓
synthesis
```

The synthesizer should primarily compose from registered claims instead of treating the entire raw corpus as unconstrained prose context.

The final report may contain:

- verified factual claims;
- clearly identified disputed points;
- explicitly marked inference/analysis;
- uncertainty and qualifiers preserved from the claim set.

## 11. Reverse audit

After synthesis, the system should extract/check externally verifiable assertions from the generated report and compare them with the allowed claim set.

Conceptually:

```text
C_output = claims asserted by final report
C_allowed = registered claims permitted by policy

unauthorized = C_output - C_allowed
```

The reverse audit should flag semantic escalation such as:

- association -> causation;
- possibility -> certainty;
- subgroup result -> universal result;
- estimate -> exact fact;
- historical result -> current result;
- removing material qualifiers.

## 12. DocumentVersion

A final report/export is a versioned artifact, not mutable anonymous text.

Each document version should identify:

- originating run;
- parent document version if any;
- contributing claim set;
- creator/actor;
- generation/edit activity;
- content hash;
- timestamps;
- review/approval state.

AI generation and human edits must remain attributable.

## 13. Review

Human review is distinct from AI/model verification.

A review binds to an exact document version and may include:

- reviewer identity;
- findings;
- required changes;
- caveats;
- approval/rejection decision;
- timestamp;
- policy/assurance level.

If the approved document is subsequently edited, the earlier approval must not silently apply to the new version.

## 14. AuditEvent

Audit events answer the process question: what happened?

Actor classes may include:

- `HUMAN`
- `MODEL`
- `SYSTEM`
- `TOOL`
- `ADMIN`

An audit event may record:

- actor;
- action/activity;
- input identities/hashes;
- output identities/hashes;
- model/tool/component versions;
- run/document/source/claim references;
- timestamp;
- previous event/hash-chain data where implemented.

Process audit and epistemic audit are complementary:

```text
Process assurance: can we reconstruct the activity?
Epistemic assurance: did the evidence justify the claim/conclusion?
```

A run may be perfectly process-auditable while epistemically weak, or epistemically well supported while process provenance is incomplete. The system should surface the difference.

## 15. Bitemporal direction

Important source and claim state should eventually distinguish:

- **valid time:** when the represented fact/state applies in the world;
- **knowledge/system time:** when this system learned or recorded it.

Unknown times remain unknown. Models must not invent missing dates solely to satisfy schema requirements.

## 16. Overlapping research

Two research runs may overlap in question, sources, topics, or claims while remaining independent investigations.

```text
R1 != R2
Sources(R1) ∩ Sources(R2) may be non-empty
Claims(R1) ∩ Claims(R2) may be semantically similar
```

Rules:

- do not automatically merge runs;
- content-addressed source artifacts may be physically deduplicated;
- each run retains its own question, policy/model versions, claim decisions, synthesis, reviewer state, and audit trail;
- later UI may surface shared sources, topics, or probable claim overlap as discovery aids.

## 17. UI projections

The same epistemic model supports multiple projections without changing the canonical backend.

Normal research projection:

```text
Answer -> citation -> claim -> evidence
```

Audit projection:

```text
run -> event -> input/output -> source/document version
```

Future exploration projection:

```text
domain -> topic -> research -> claim -> evidence -> source
```

A future graph/knowledge-sphere visualization is therefore a projection over this model, not a requirement to replace SQLite with a graph database.

## 18. Design consequences for upcoming contracts

The eventual typed contracts should preserve at least these durable concepts:

- `ResearchRun`
- `Claim`
- `Source`
- `SourceVersion`
- `EvidenceSpan`
- `EvidenceEdge` / claim-evidence relationship
- `Synthesis` or report representation
- `DocumentVersion`
- `Review`
- `AuditEvent`

The UI may request lighter projections, but those projections should not erase the relationships needed for inspection and audit.

## 19. Initial properties implied by this model

Candidate properties to formalize next include:

1. Every visible citation resolves to a registered claim/evidence relationship.
2. Every evidence span resolves to an immutable source version.
3. Evidence relation is explicit; a citation alone cannot imply `SUPPORTS`.
4. Final externally verifiable assertions must map to allowed registered claims or be explicitly labeled inference/analysis.
5. Human approval binds to exactly one document version.
6. Editing an approved document creates/supersedes review state rather than inheriting approval silently.
7. Independent overlapping research runs retain independent provenance and audit histories.
8. Source lineage must not count downstream copies as independent evidence roots where common ancestry is known.
9. Unknown temporal metadata must remain unknown rather than model-invented.
10. Tenant/authorization boundaries apply to all projections of the epistemic graph.

## 20. Working product statement

The simplest product-level description is:

> **A ResearchRun is a versioned epistemic investigation. Claims are its epistemic atoms. Evidence relationships justify, weaken, or contradict those claims. Synthesis turns the allowed claim set into readable output. Review and audit make the result inspectable and attributable.**
