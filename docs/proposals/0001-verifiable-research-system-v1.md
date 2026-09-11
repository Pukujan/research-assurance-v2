# Proposal 0001: Verifiable Research System v1

- **Status:** Draft
- **Version:** 1.0
- **Date:** 2026-09-11
- **Repository:** `Pukujan/research-assurance-v2`
- **Decision scope:** Product shape, development method, assurance model, and implementation sequence

## 1. Purpose

Build a local-first or self-hosted AI research system in which research can be inspected and verified from the user interface down to source artifacts, model/tool activity, claim evidence, document versions, and audit history.

The system must be useful before the complete assurance architecture exists. We will therefore develop it as a sequence of end-to-end vertical slices, with versioned contracts and explicit properties at every stage.

The repository is the durable project state. Chat context is never authoritative project memory.

## 2. Core principle

We do not try to make an LLM intrinsically trustworthy.

We make its work:

- inspectable,
- attributable,
- reproducible where possible,
- versioned,
- constrained by typed contracts,
- checked by deterministic validators where possible,
- checked by calibrated probabilistic verifiers where necessary,
- auditable by a human at the end of the chain.

The primary product question is not only **"what answer did the AI produce?"** but also **"what would a reviewer need to inspect to decide whether to rely on it?"**

## 3. Development sequence

The initial sequence is intentionally UX-first but not mockup-driven:

1. **Durable proposal and properties**
2. **Frontend visual concepts** generated from realistic research scenarios
3. **Human critique of the user flow**
4. **Proposal revision** to reflect the accepted user flow
5. **Typed frontend/backend contracts**
6. **Fixture-backed frontend** using realistic fake research records
7. **Walking vertical slice** across browser, API, database, artifacts, audit, and verification
8. **Incremental replacement of fixtures** with real components
9. **Domain assurance packs** for finance, legal, medicine, geography, and other domains
10. **Higher-assurance workflows** only where risk and observed failure justify them

No major backend subsystem is considered justified merely because it is architecturally elegant. It must support a user-visible assurance need or a property that can be tested.

## 4. Recognized patterns this proposal combines

This proposal intentionally combines established engineering practices rather than claiming a single new methodology:

- **Docs as code / architecture as code:** important design state is version controlled alongside implementation.
- **Architecture Decision Records (ADRs):** important decisions are durable and revisable.
- **Walking skeleton / tracer bullet / vertical-slice development:** establish an end-to-end executable path early, then deepen it.
- **Evolutionary architecture:** retain the ability to change components behind stable fitness functions and contracts.
- **Contract-first / API-first development:** user flow and typed boundaries are specified before implementation hardens.
- **Consumer-driven contract testing:** interfaces are validated against actual consumer needs rather than abstract schema elegance.
- **Property-driven development:** critical behavior is expressed as invariants/properties with explicit oracles.
- **Specification by example:** fixtures and gold cases make ambiguous requirements executable.
- **Test-first / feedback-sensor development for agents:** compiler, linter, type checker, tests, and custom invariants act as direct corrective feedback for coding agents.
- **Progressive assurance:** cheap checks run continuously; expensive holdouts, mutation tests, adversarial tests, and human review run at appropriate gates.

The particular combination is project-specific, but the ingredients are established practices.

## 5. Product surfaces to validate before API design

The first visual exploration should cover four surfaces.

### 5.1 Research workspace

A researcher can see:

- the research question,
- the synthesized answer,
- claim markers embedded in the answer,
- verification state for each claim,
- the underlying evidence,
- warnings for disputed or unverified claims,
- provenance/version information when requested.

A citation must be inspectable as evidence, not merely clickable as a URL.

### 5.2 Claim inspector

A claim inspector should show:

- normalized claim text,
- claim type,
- status (`VERIFIED`, `DISPUTED`, `UNVERIFIED`, optionally `INFERENCE`),
- exact evidence spans,
- artifact/source version,
- verifier results,
- deterministic checks,
- domain-policy checks,
- contradictions,
- lineage/source independence,
- history of the claim.

### 5.3 Audit timeline

A chronological view should distinguish actor classes:

- `HUMAN`,
- `MODEL`,
- `SYSTEM`,
- `TOOL`,
- `ADMIN`.

It should answer who did what, with which input/output artifacts, model/tool/version, and when.

### 5.4 Admin/reviewer dossier

A reviewer should be able to reconstruct a research run:

- authenticated user,
- research question,
- transcript,
- tool calls,
- source snapshots,
- model/provider metadata,
- claims and evidence,
- validation results,
- human edits,
- generated document versions,
- approvals,
- audit-chain integrity.

## 6. Frontend-first validation rule

Before building a production backend subsystem, we should be able to demonstrate in a fixture-backed UI why that subsystem exists.

Examples:

- If we cannot explain how source version history helps a reviewer, do not build a sophisticated source-version subsystem yet.
- If the claim inspector cannot communicate bitemporal state clearly, refine the interaction before finalizing the database representation.
- If a reviewer cannot distinguish AI-generated text from human-modified text, the document-version model is incomplete regardless of backend correctness.

Generated UI images are exploratory artifacts, not specifications. The durable specification remains text plus executable fixtures/contracts.

## 7. Versionable meta-system

A research run is produced by an assembly of independently versioned components rather than by a single opaque application version.

Example component manifest:

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

Every meaningful transformation records:

- implementation/component version,
- configuration version,
- model/provider version where applicable,
- input identities/hashes,
- output identities/hashes,
- timestamp,
- actor.

## 8. Property-driven development

Important requirements become durable properties, not prose-only aspirations.

A property contains:

- ID,
- statement,
- rationale,
- severity,
- oracle,
- scope,
- counterexample or adversarial case,
- linked tests/benchmarks,
- version history.

Initial candidate properties:

### P-001 Artifact integrity

Any byte mutation to an immutable stored source artifact must cause artifact-integrity verification to fail.

**Oracle:** deterministic hash verification.

### P-002 Claim grounding

No factual statement may enter a completed report unless it maps to one or more registered claims or is explicitly marked as analysis/opinion/inference under policy.

**Oracle:** reverse claim extraction plus claim-graph comparison, with deterministic structural checks where possible.

### P-003 Tenant isolation

An authenticated user in organization A must not retrieve research artifacts belonging to organization B unless an explicit cross-organization authorization exists.

**Oracle:** deterministic authorization tests and mutation tests.

### P-004 Source-order robustness

Permuting source order must not materially alter deterministic/numeric conclusions whose evidence set is unchanged.

**Oracle:** metamorphic test.

### P-005 Untrusted-content isolation

Retrieved documents must not directly invoke privileged tools, mutate trusted state, or override system policy.

**Oracle:** adversarial integration tests; unauthorized side-effect count must be zero.

### P-006 Document lineage

Every final-document version must identify its parent version, originating research run, contributing claim set, creator/actor, and content hash.

**Oracle:** deterministic graph/integrity validation.

### P-007 Historical reproducibility

Old source, claim, transcript, and generated-document versions must remain independently addressable and auditable after later revisions.

**Oracle:** bitemporal/version-history tests.

The property registry will live under `assurance/properties/` once implementation begins.

## 9. Verification ladder

The system must distinguish assurance levels rather than implying every report has identical assurance.

### Level 0 — Exploratory

- retrieval,
- source snapshots,
- citations,
- basic claim linkage.

### Level 1 — Verified

- claim extraction,
- claim/evidence verification,
- deterministic numeric/structural checks where applicable,
- reverse synthesis audit.

### Level 2 — High assurance

Level 1 plus:

- contradiction search,
- source-lineage analysis,
- temporal/version checks,
- independent verifier pass.

### Level 3 — Human reviewed

Level 2 plus:

- explicit human reviewer,
- reviewed findings,
- approved document/version,
- signed/recorded approval event.

High-stakes workflows may require Level 3 by policy.

## 10. Deterministic versus probabilistic checks

The system must prefer deterministic validators whenever the task admits one.

Examples suitable for deterministic validation:

- hashes,
- schema conformance,
- tenant/RBAC boundaries,
- event-chain integrity,
- arithmetic,
- units/currency scaling,
- dates and temporal intervals,
- document version lineage,
- geometry validity/CRS constraints,
- file existence and content identity.

LLM/verifier components should focus on semantic tasks such as:

- entailment,
- qualifier preservation,
- claim decomposition,
- contradiction interpretation,
- source-role classification,
- synthesis fidelity.

Probabilistic verifiers must be calibrated on labeled examples before their `PASS` state is treated as meaningful assurance.

## 11. Testing and feedback sensors

### Fast inner loop

- formatter,
- linter,
- type checker,
- unit tests.

### Commit / PR loop

- property tests,
- integration tests,
- contract tests,
- browser/E2E tests,
- targeted security tests.

### Assurance loop

- mutation testing on trust-critical deterministic code,
- gold-case benchmarks,
- hidden holdouts,
- metamorphic tests,
- prompt-injection tests,
- synthesis round-trip/reverse audits,
- sampled human review.

Agents must not mark an implementation task complete while required lint, type, test, property, or contract gates are red.

## 12. Fixture-first API design

Before production API implementation:

1. Create realistic fixture research runs.
2. Build the frontend against those fixtures.
3. Revise the UX until the assurance information is understandable.
4. Derive typed API contracts from the accepted user flow.
5. Generate shared frontend/backend types from a single contract source where possible.
6. Make the real backend satisfy the already-working contract.

A backend implementation should be replaceable without changing the frontend if the contract is preserved.

## 13. Initial technical direction (non-binding until UX confirmation)

Current working assumptions:

- Python backend, likely FastAPI.
- SQLite locally, including FTS5/BM25 for initial lexical retrieval.
- Content-addressed artifact directory outside SQLite.
- Pydantic/JSON Schema/OpenAPI for typed contracts.
- TypeScript frontend.
- Playwright for browser/E2E checks.
- Ruff plus Pyright or Mypy for Python quality gates.
- ESLint plus TypeScript compiler for frontend quality gates.
- Pytest plus Hypothesis for deterministic/property testing.
- Provider-neutral LLM adapter supporting cloud and local/OpenAI-compatible endpoints.

These are hypotheses, not commitments. UX/contracts may invalidate them.

## 14. Agent development and handoff

Agents must work from reconstructed durable state, not accumulated conversation history.

Canonical durable state hierarchy:

1. code and executable test state,
2. Git commit,
3. machine-readable checkpoint,
4. issue description/comments,
5. project-board metadata.

A checkpoint should contain only current externally relevant state:

- issue/work item,
- current commit,
- applicable properties,
- completed work,
- failing checks,
- important decisions,
- open questions,
- next action,
- files/components touched.

It should not serialize a full conversation or hidden reasoning trace.

Local/cheap agents should handle durable repetitive work; stronger cloud reasoning agents should be escalated for architecture, ambiguity, security boundaries, high-risk changes, unexplained regressions, and adversarial review.

## 15. Bitemporal and provenance direction

The system should eventually distinguish:

- **valid time:** when a fact/source state applies in the represented world,
- **knowledge/system time:** when this system learned or recorded that version.

This distinction should be preserved from the first durable data model, but the UI representation must be validated before final schema/API decisions.

Provenance should record at minimum:

`input -> activity -> output`, plus actor and version.

The internal representation should remain simple and later be exportable/mappable to standards such as W3C PROV where useful; standards compliance is not a v1 prerequisite.

## 16. Explicit non-goals for the first build

Do not begin with:

- graph database,
- vector database solely for novelty,
- distributed job infrastructure,
- Kubernetes,
- blockchain,
- custom public transparency log,
- universal ontology,
- universal credibility score,
- AI-vs-human authorship detector,
- complex multi-agent debate framework,
- implementation of entire external standards stacks.

Those require an observed need and a property/use case that justifies them.

## 17. Milestone 0 — verifiable skeleton

Before serious research-agent implementation, establish:

- this proposal and durable docs,
- initial property registry,
- ADR convention,
- lint/type/test commands,
- component/version manifest format,
- visual concepts for the four core product surfaces,
- accepted user flow,
- fixture research records,
- fixture-backed frontend,
- typed API contracts,
- agent checkpoint format,
- GitHub issue/PR workflow.

Milestone 0 should contain very little AI-specific implementation.

## 18. Milestone 1 — first real vertical slice

Implement one complete path:

`authenticated user -> research run -> source snapshot -> evidence -> claim -> verification -> synthesis -> reverse audit -> dossier`

The slice may initially support only a narrow input class such as HTML, text PDFs, local text/Markdown, and selected SEC sources.

Every step must be visible through the same user-facing assurance surfaces designed in Milestone 0.

## 19. Revision policy

This proposal is deliberately expected to change.

Changes should occur as versioned revisions, with a short changelog explaining:

- what user-flow evidence changed our view,
- which assumptions were invalidated,
- which properties were added/changed/removed,
- which contracts became stable,
- which decisions moved into ADRs.

Major conceptual changes increment the proposal major version. Clarifications and non-breaking refinements increment the minor version.

Once a decision becomes implementation-specific and relatively stable, move it into an ADR rather than endlessly expanding this proposal.

## 20. Immediate next step

Generate visual concepts for the four primary product surfaces using a realistic end-to-end research scenario.

The images should help answer:

- What does a researcher need to see while working?
- What makes evidence inspection intuitive rather than forensic?
- What information belongs behind progressive disclosure?
- What does an admin/reviewer need that a researcher does not?
- How do disputed, unverified, superseded, and human-edited content appear?
- How does a user move from answer -> claim -> evidence -> source version -> audit history without losing context?

After visual review, revise this proposal before freezing API contracts.

## Changelog

### v1.0 — 2026-09-11

Initial proposal. Establishes UX-first vertical-slice development, property-driven assurance, fixture-first contracts, versionable components, durable agent handoffs, progressive assurance, and the requirement to revise architecture after visual/user-flow validation and before implementation hardens.
