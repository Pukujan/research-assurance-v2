# Property-Driven Development v1

- Status: Active development convention
- Date: 2026-09-11
- Applies to: Research Assurance v2

## Purpose

Research Assurance is developed from externally observable properties and trust invariants rather than from implementation tasks alone.

The durable sequence is:

```text
user story / slice
    -> properties and counterexamples
    -> deterministic oracle where possible
    -> fixture / acceptance scenario
    -> implementation
    -> browser / integration verification
    -> human acceptance
```

A feature is not complete because an agent says it looks correct. It is complete when its relevant properties have passing oracles and the user-visible slice behaves correctly.

## Source-of-truth precedence

When an implementation agent starts work, use this precedence:

1. code and executable tests/oracles;
2. property registry under `assurance/properties/`;
3. slice specification under `docs/`;
4. GitHub issue describing the work unit;
5. agent checkpoint/handoff notes;
6. chat transcripts.

Chat is never the durable engineering specification.

## Property shape

Properties should include, where useful:

```yaml
id: P-XXX
statement: externally observable invariant
severity: critical | high | medium | low
scope: affected subsystem
oracle: how it is checked
strategy: examples, generated cases, mutation, browser scenario, etc.
acceptance: explicit pass condition
counterexample: a concrete failing state
```

Not every property requires all fields immediately, but every critical property must have a meaningful oracle before the corresponding slice is considered production-ready.

## Oracle hierarchy

Prefer the least subjective oracle that can decide the property:

1. deterministic structural or mathematical check;
2. schema / referential-integrity check;
3. property-based or metamorphic check;
4. integration or browser assertion;
5. calibrated model-assisted review;
6. sampled human review.

LLM judgment must not replace a deterministic oracle when a deterministic oracle is available.

## Slice rule

Each implementation slice should cross the stack:

```text
story
-> properties
-> fixture
-> UI / contract
-> persistence or artifact
-> audit/provenance behavior
-> verification
```

Avoid horizontal phases such as "build all database tables" or "build the ontology system" before a user-visible slice needs them.

## Agent workflow

An implementation agent should:

1. read the slice spec and relevant property files;
2. run existing oracles before editing;
3. implement the smallest change satisfying the properties;
4. run deterministic checks;
5. run browser/integration checks when the slice is user-visible;
6. record any property that cannot be verified and why;
7. never weaken or delete a property merely to make an implementation pass without explicit review.

A reviewing agent should inspect failing counterexamples, not merely summarize the diff.

## Verification records

For important slices, verification output should be reproducible from repo commands. A short result may be attached to a PR or checkpoint, but the commands and acceptance criteria belong in the repo.

## Current property registries

- `assurance/properties/core-v1.yaml` — core research/evidence/versioning/security/UX invariants.
- `assurance/properties/mobile-prototype-v1.yaml` — standalone mobile prototype properties.

## Future refinement

As the implementation grows, property IDs should remain stable. Statements can be superseded through explicit versioning rather than silently changing historical acceptance criteria.
