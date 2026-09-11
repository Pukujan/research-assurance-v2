# Research Assurance v2

A local-first, auditable AI-assisted research system designed so that every meaningful step can be inspected, versioned, tested, and reproduced.

## Current phase

**Specification / fixture-backed product development.** The structural UX is accepted for v1; contracts and implementations remain intentionally revisable as vertical slices expose problems.

The repository, rather than any chat session, is the durable project state.

## Start here

- Current proposal: [`docs/proposals/0001-verifiable-research-system-v1.1.md`](docs/proposals/0001-verifiable-research-system-v1.1.md)
- Property-driven development: [`docs/development/property-driven-development-v1.md`](docs/development/property-driven-development-v1.md)
- Core assurance properties: [`assurance/properties/core-v1.yaml`](assurance/properties/core-v1.yaml)
- Epistemic IR / living ontology: [`docs/product/epistemic-ir-and-living-ontology-v1.md`](docs/product/epistemic-ir-and-living-ontology-v1.md)
- Conceptual domain model: [`docs/architecture/domain-model-v1.md`](docs/architecture/domain-model-v1.md)
- Draft API contracts: [`docs/contracts/api-contracts-v0.md`](docs/contracts/api-contracts-v0.md)
- Fixture-backed prototype: [`prototype/README.md`](prototype/README.md)

## Current local-agent work packet

The standalone phone-review artifact is a small Property-Driven Development slice.

Read in this order:

1. [`assurance/properties/mobile-prototype-v1.yaml`](assurance/properties/mobile-prototype-v1.yaml)
2. [`docs/product/mobile-prototype-slice-v1.md`](docs/product/mobile-prototype-slice-v1.md)
3. [`.agent/tasks/mobile-prototype-v1.md`](.agent/tasks/mobile-prototype-v1.md)
4. [`prototype/verify_mobile.py`](prototype/verify_mobile.py)

Target artifact:

```text
prototype/research-assurance-mobile.html
```

Minimum verification:

```bash
python prototype/verify_mobile.py
python prototype/verify_mobile.py --browser  # when Playwright is available
```

An agent must not report this slice complete merely because the HTML looks correct; the relevant property oracles must pass or be explicitly recorded as not run.

## Development sequence

1. Durable intent, users, roles, stories, and flows.
2. Accepted structural UX.
3. Property registries and counterexamples.
4. Conceptual domain model and draft contracts.
5. Realistic fixtures and fixture-backed frontend.
6. Walking vertical slices that cross UI, contracts, persistence, provenance, and verification.
7. Replace fixture components incrementally while preserving properties.
8. Add domain assurance packs, living ontology workflows, and deeper formal verification only when slices require them.
