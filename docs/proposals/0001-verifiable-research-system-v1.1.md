# Proposal 0001: Verifiable Research System v1.1

- **Status:** Draft
- **Version:** 1.1
- **Date:** 2026-09-11
- **Supersedes for current design work:** `0001-verifiable-research-system-v1.md`
- **Decision scope:** Product shape, development sequence, UX model, assurance model, and implementation boundaries

## 1. Why v1.1 exists

Visual exploration and user-flow discussion changed the product shape in useful ways before API contracts or production code were frozen.

The initial proposal correctly identified research, claim inspection, audit, and review as core needs, but the visual concepts showed that presenting all assurance information simultaneously creates an overloaded "research cockpit." The accepted direction is calmer and more document-centered.

The product principle for the next phase is:

> **Research first. Assurance on demand. Audit when needed.**

The assurance system remains deep; it is no longer expected to be visually present at all times.

## 2. Product objective

Build a local-first or self-hosted AI research application in which teams can create, reuse, inspect, review, share, and audit research while preserving exact source versions, claims, evidence, model/tool activity, human edits, and document history.

The system should feel like a focused research workspace during normal use and expose forensic depth only when the user asks for it or policy requires it.

The repository is the durable project state. Chat history is not authoritative project memory.

## 3. Development method

The revised sequence is:

1. Durable product proposal.
2. Users, roles, and user stories.
3. End-to-end user flows/storyboards.
4. Visual UX exploration against those flows.
5. Human acceptance/revision of the flows and screen model.
6. Property registry: what must remain true.
7. Domain/data concepts sufficient for the accepted flows.
8. Typed API contracts derived from actual UI needs.
9. Fixture-backed interactive frontend.
10. Walking vertical slice across browser, API, persistence, audit, and one real research path.
11. Incremental replacement of fixtures and narrow implementations with production components.
12. Domain assurance packs and higher-assurance workflows when observed risk justifies them.

The system is developed as complete user actions, not horizontal subsystems.

A vertical slice must cross the relevant layers:

`story -> property -> UI -> contract -> persistence -> implementation -> audit -> verification`

## 4. Recognized engineering patterns

This project combines established practices rather than relying on one methodology:

- docs as code;
- Architecture Decision Records;
- walking skeleton / tracer bullet development;
- vertical slices;
- evolutionary architecture;
- contract-first and consumer-driven contract testing;
- property-driven development;
- specification by example;
- property-based testing;
- deterministic feedback sensors for coding agents: formatter, linter, type checker, tests;
- progressive assurance using mutation tests, gold cases, hidden holdouts, adversarial checks, and sampled human review.

Property-Driven Development is the project convention that critical product and assurance requirements are expressed as durable properties with explicit oracles, not only prose requirements.

## 5. Accepted product surfaces

### 5.1 Research

The Research workspace is the primary product surface.

The report/document is visually dominant. A user should normally be able to read research without looking at provenance infrastructure.

Expected content:
- research question/title;
- simple run progress while active;
- synthesized answer/report;
- inline citations or claim markers;
- compact assurance summary;
- follow-up/fork/share actions.

Possible lightweight modes/tabs:
- Answer;
- Claims;
- Sources.

### 5.2 Contextual evidence inspector

Claim inspection is no longer a separate top-level application screen. It is a reusable contextual inspector opened from a citation, claim, source, or review item.

Default content:
- normalized claim;
- verification state;
- exact evidence;
- source identity and location;
- source preview when useful;
- concise explanation of support/contradiction.

Advanced detail is progressively disclosed:
- source/artifact version;
- hashes;
- parser/verifier versions;
- temporal metadata;
- lineage;
- raw structured validation results.

Where feasible, high-assurance review should expose both:
- the human-verifiable original source fragment, such as a PDF page/table/image region;
- the machine-verifiable canonical extracted representation.

Both must resolve to the same source version.

### 5.3 Library

The Library is a calm work list for prior research, not a KPI dashboard.

Primary functions:
- search prior runs;
- reopen active/recent work;
- find runs needing review;
- discover authorized teammate research;
- filter by owner/team/topic/status/date;
- eventually surface related or overlapping research.

Topic/category auto-allocation is future-friendly metadata. Users must be able to inspect and correct it.

### 5.4 Reviews

Reviews provide a focused human-review queue.

The reviewer should start with the highest-risk items rather than rereading every report linearly.

Potential review triggers include:
- disputed claims;
- unsupported or partially supported claims;
- temporal ambiguity;
- questionable source lineage;
- human edits that strengthen certainty;
- domain-policy warnings.

Review decisions refer to an exact document/report version and are separate from AI verification state.

### 5.5 Audit

Audit is an explicit forensic mode, not normal research chrome.

It should answer:
- who did what;
- when;
- with which model/tool/component version;
- using which source/artifact version;
- what changed;
- which document version was approved/exported.

Default presentation should be readable event summaries with filters and a selected-event detail panel. Raw JSON/hashes remain available but secondary.

### 5.6 Admin

Admin is for organization management:
- users;
- teams;
- roles/access;
- audit search;
- policies;
- quotas/usage;
- operational visibility.

Infrastructure/system operation and permission to read research content should remain conceptually distinct.

## 6. Panel and complexity rule

The working UI rule is:

- **1 primary information region** for reading/list screens;
- **+1 contextual inspector** when the user requests detail;
- **3 simultaneous regions maximum** for explicit forensic/audit workflows.

This is a design hypothesis to test in fixtures/E2E UX, not an eternal constraint.

Avoid permanently visible dashboards of every metric, verifier, source, timeline, and graph.

## 7. Visual direction

The accepted aesthetic direction is dark-first, low-glare, spacious, and mildly futuristic.

Desired feeling:

> **A research pilot building serious systems with AI.**

Use:
- dark calm surfaces;
- restrained luminous accents;
- generous whitespace;
- strong document typography;
- occasional space/mission-control metaphors for progress/exploration;
- monospaced type only for technical metadata.

Avoid:
- dense sci-fi HUDs;
- constant neon borders;
- large authentication/status cards;
- dashboard mosaics where a simple list/document is better.

A future knowledge-sphere/galaxy explorer may become an optional projection over the same data model. It is explicitly **not** an MVP architectural requirement and does not justify a graph database.

## 8. Users and collaboration

Initial hierarchy:

`Organization -> Teams -> Users -> Research Runs`

Core product roles:
- Researcher;
- Reviewer;
- Organization Admin;
- System Operator;
- Guest/Unauthenticated user.

Initial research visibility vocabulary:
- private;
- team;
- organization;
- explicitly shared.

Team discovery should promote reuse while preserving independent research histories.

Overlapping research runs are not automatically merged. Shared sources may be deduplicated by content identity while each run remains independently attributable and auditable.

## 9. Sharing and external discussion

Important research objects receive stable identities, including runs, claims, source versions, and document versions where needed.

Users should be able to discuss research outside the application using stable internal links or versioned exports.

An exported artifact must retain lineage back to the originating run/document version. A reference to Research Assurance identifies the research process; it does not replace citation of the underlying source evidence.

## 10. Versionable meta-system

A research run is produced by independently versioned components rather than one opaque application version.

Illustrative manifest:

```json
{
  "system_version": "0.1.0",
  "components": {
    "artifact_schema": "1",
    "claim_schema": "1",
    "provenance_schema": "1",
    "retriever": "bm25.v1",
    "extractor": "claim-extractor.v1",
    "verifier": "entailment.v1",
    "synthesizer": "synthesis.v1",
    "reverse_auditor": "reverse-audit.v1",
    "policy": "generic.v1",
    "prompt_pack": "v1",
    "frontend_contract": "research-api.v1"
  }
}
```

Meaningful transformations record input identity, output identity, component/configuration version, actor, and time.

## 11. Properties and verification

Initial properties from v1.0 remain in force as candidates:
- artifact integrity;
- claim grounding;
- tenant isolation;
- source-order robustness;
- untrusted-content isolation;
- document lineage;
- historical reproducibility.

The accepted user flows add likely properties around:
- stable run identity before asynchronous work;
- exact citation -> claim -> evidence -> source-version resolution;
- approval being bound to an exact document version;
- post-approval edits invalidating/superseding review state as policy dictates;
- sharing protected resources without silently broadening authorization;
- preserving independent histories for overlapping research.

These should next be formalized in `assurance/properties/` with explicit oracles.

## 12. Assurance levels

The progressive assurance ladder remains:

### Level 0 — Exploratory
- retrieval;
- source snapshots;
- citations;
- basic claim linkage.

### Level 1 — Verified
- claim extraction;
- claim/evidence verification;
- deterministic numeric/structural checks where applicable;
- reverse synthesis audit.

### Level 2 — High assurance
Level 1 plus:
- contradiction search;
- source-lineage analysis;
- temporal/version checks;
- independent verifier pass.

### Level 3 — Human reviewed
Level 2 plus:
- explicit reviewer;
- recorded findings/caveats;
- approval tied to an exact version.

## 13. Testing hierarchy

### Fast inner loop
- formatter;
- linter;
- type checker;
- unit tests.

### Commit/PR loop
- property tests;
- integration tests;
- contract tests;
- browser/E2E tests;
- targeted security tests.

### Assurance loop
- mutation testing on trust-critical deterministic code;
- gold cases;
- hidden holdouts;
- metamorphic tests;
- prompt-injection tests;
- synthesis reverse audits;
- sampled human review.

Agents cannot mark work complete while required gates are red.

## 14. Data and backend direction

The first implementation should remain deliberately boring unless a user flow proves otherwise.

Working hypotheses:
- Python/FastAPI backend;
- SQLite as the initial system of record;
- SQLite FTS5/BM25 for initial lexical retrieval;
- content-addressed artifact storage outside SQLite;
- Pydantic/JSON Schema/OpenAPI contracts;
- TypeScript frontend;
- Playwright E2E;
- Ruff + Pyright/Mypy;
- ESLint + TypeScript compiler;
- Pytest + Hypothesis;
- provider-neutral LLM adapter.

SQLite remains canonical even if later UIs render provenance or knowledge relationships as graphs. Graphs, timelines, source previews, and future knowledge-sphere views are projections over the versioned core data.

## 15. Temporal and provenance direction

The future durable data model should preserve:
- valid time: when information applies in the represented world;
- knowledge/system time: when this system learned or recorded that version.

Unknown temporal values remain unknown; models should not invent them to satisfy a schema.

Provenance records at minimum:

`input -> activity -> output`, plus actor and version.

Internal data should remain simple and map/export to standards such as W3C PROV when useful rather than requiring standards-heavy infrastructure in v1.

## 16. Agent development and handoff

Agents work from reconstructed durable state, not accumulated chat history.

State precedence:
1. code and executable test state;
2. Git commit;
3. machine-readable checkpoint;
4. issue description/comments;
5. project-board metadata.

Checkpoints contain current externally relevant state only: task, commit, properties, completed work, failing checks, decisions, open questions, and next action.

## 17. Explicit non-goals for MVP

Do not begin with:
- graph database;
- vector database solely for novelty;
- distributed job infrastructure;
- Kubernetes;
- blockchain;
- custom transparency network;
- universal ontology;
- universal credibility score;
- AI-vs-human authorship detector;
- complex multi-agent debate framework;
- 3D knowledge-universe backend requirements.

A future knowledge explorer must reuse the same durable research model rather than force an early architectural rewrite.

## 18. Milestone 0 — Product and assurance skeleton

Current durable inputs now include:
- Proposal v1.0 and this v1.1 revision;
- users and roles v1;
- user stories v1;
- flows for start research, inspect evidence, library/prior research, review, audit, and sharing;
- screen requirements v1;
- several visual explorations establishing the preferred calm mission-control direction.

Remaining Milestone 0 work before real backend implementation:
1. generate a focused visual pass from the durable flows;
2. accept/revise the final screen/user-flow model;
3. formalize the first property registry;
4. define domain/data concepts required by the accepted flows;
5. derive typed API contracts;
6. create realistic fixtures;
7. build a fixture-backed interactive frontend;
8. establish lint/type/test commands and CI;
9. establish ADR and agent checkpoint conventions.

## 19. Milestone 1 — First walking vertical slice

The first real implementation path should be smaller than the complete research engine.

Recommended sequence:

### Slice 1 — Research identity
`authenticated user -> create run -> persist run -> library -> audit event`

### Slice 2 — Source identity
`run -> ingest one source -> snapshot/hash -> source view -> audit event`

### Slice 3 — Evidence/claim
`source -> evidence span -> one claim -> verification state -> inspector`

### Slice 4 — Research answer
`question -> collection -> sources -> claims -> verification -> synthesis -> citations`

### Slice 5 — Audit/review
`completed run -> audit reconstruction -> review decision -> versioned approval`

Each slice must be human-verifiable end to end before increasing scope.

## 20. Immediate next step

Generate a new visual pass directly from the durable flows and screen requirements, focusing on four views:
- Research Workspace with evidence inspector;
- Library;
- Reviews;
- Audit.

The visual pass should obey the panel-count rule and preferred dark/low-glare mission-control aesthetic.

After the user confirms or revises those flows, formalize properties and only then freeze initial API contracts.

## Changelog

### v1.1 — 2026-09-11

Revised after visual/product-flow exploration. Establishes the "Research first. Assurance on demand. Audit when needed." UX principle; changes Claim Inspector from a standalone product surface to a contextual primitive; adds Library and Reviews as primary surfaces; separates Audit as forensic mode; records role/collaboration/sharing direction; establishes a 1–2 panel default; records the calm mission-control visual direction; and explicitly treats any future knowledge-sphere explorer as an optional projection rather than an MVP backend requirement.

### v1.0 — 2026-09-11

Initial proposal. Established UX-first vertical-slice development, property-driven assurance, fixture-first contracts, versionable components, durable agent handoffs, progressive assurance, and the requirement to revise architecture after visual/user-flow validation and before implementation hardens.
