# Epistemic IR and Living Ontology v1

- Status: Design decision + bounded future direction
- Date: 2026-09-11
- Scope: Structured claim representation, ontology versioning, ontology evolution, and formal verification boundaries

## 1. Core decision

Research Assurance uses a structured epistemic intermediate representation (IR) between natural-language claims and specialized verification.

Natural-language text remains canonical for human meaning; the IR provides machine-checkable structure.

A minimal claim representation may contain:

```text
ClaimIR
- claim_id
- claim_type
- subject
- predicate
- object_or_value
- qualifiers
- valid_time
- jurisdiction
- unit
- comparison_basis
- source_scope
```

Fields may be unknown. Unknown values must remain unknown rather than being invented to satisfy the schema.

## 2. Purpose of the IR

The IR enables dispatch to the cheapest appropriate verifier.

Examples:
- numeric fact -> arithmetic/unit validator;
- temporal claim -> date/interval validator;
- policy eligibility -> rule/constraint validator;
- semantic support -> entailment verifier;
- causal claim -> stricter evidence policy;
- forecast -> inference/prediction handling.

The verifier architecture is therefore plural rather than one universal model:

```text
Claim
  -> ClaimIR
  -> proof obligation
  -> deterministic validator | symbolic/rule validator | semantic verifier | domain policy | human review
```

## 3. Ontology boundary

The project may use a small core ontology and domain extensions, but does not require a universal ontology for v1.

Core concepts may include:
- ResearchRun;
- Claim;
- Evidence;
- Source;
- Entity;
- Event;
- Actor;
- Time;
- Document.

Domain extensions may add concepts such as:
- finance: Company, Metric, Currency, FiscalPeriod, Filing;
- law: Jurisdiction, Statute, Court, Decision, EffectiveDate;
- medicine: Population, Intervention, Comparator, Outcome, Study.

Ontology is a semantic aid and policy input, not the canonical storage technology. SQLite may remain the system of record.

## 4. Living ontology direction

A living ontology is an accepted future subsystem, but not a prerequisite for the first research slices.

Research may produce ontology-change proposals:

```text
Research observations
  -> OntologyProposal
  -> evidence + review
  -> accept/reject/refine/merge
  -> OntologyVersion
```

Potential change types:
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

## 5. Historical stability

If an ontology participates in interpretation or verification, each ResearchRun records the ontology version used.

Later ontology changes must not silently reinterpret historical runs.

A historical run may be explicitly re-evaluated against a later ontology, but that produces a new evaluation/version rather than mutating the earlier result.

## 6. Ontology provenance

Ontology assertions and changes should eventually carry provenance similar to research claims:
- assertion/change identity;
- ontology version introduced;
- proposer actor;
- evidence/research references;
- reviewer/approver;
- timestamps;
- supersession/deprecation history.

The ontology itself is therefore auditable rather than being treated as unexplained background truth.

## 7. Anti-circularity rule

Ontology evolution must not become self-confirming.

A canonical ontology assertion cannot be accepted solely because a prior ontology version already implied it.

The system should distinguish:
- observations grounded directly in source evidence;
- inferences that depend on the current ontology.

This distinction becomes a formal assurance property.

## 8. Formal verification boundary

Durable principle:

> Use deterministic or formal verification whenever the claim admits it.

Potential tools include arithmetic validators, unit systems, temporal logic, rule engines, constraint solvers, SMT solvers, or theorem provers.

No specific theorem prover is an architectural dependency in v1.

Full theorem proving is not the general truth engine because many research claims depend on uncertain empirical evidence, interpretation, methodology, or incomplete facts.

## 9. Status classification

Durable decisions:
- Epistemic IR exists conceptually and should appear when Claim/Evidence verification is implemented.
- Unknown structured values remain unknown.
- Ontology use is versioned per run where applicable.
- Ontology evolution, if implemented, is proposed/reviewed/versioned/audited.
- Formal methods are used opportunistically behind proof obligations.

Future hypotheses, not commitments:
- automatic ontology induction;
- global cross-domain ontology;
- automatic ontology merge;
- knowledge-sphere ontology visualization;
- generalized theorem proving for research;
- fully automatic canonical concept/entity resolution.

## 10. Slice impact

The ontology does not move in front of the product.

Expected introduction order:

```text
Slice 1: Research identity              -> no ontology dependency
Slice 2: Source identity                -> no ontology dependency
Slice 3: Claim + Evidence               -> introduce minimal ClaimIR
Slice 4: Research answer                -> IR-driven verification dispatch
Slice 5: Review                         -> no new ontology requirement
Slice 6: Team collaboration             -> no new ontology requirement
Slice 7: Domain policy                  -> small domain vocabularies/ontology may emerge
Slice 8: Living ontology                -> proposals + review + OntologyVersion
Slice 9+: Exploration                   -> related research / graph / sphere projections
```

This keeps the living ontology as an evolutionary capability rather than an MVP blocker.