# Research Assurance v2

A local-first, auditable AI-assisted research system designed so that every meaningful step can be inspected, versioned, tested, and reproduced.

## Current phase

**Proposal / UX discovery.** No production architecture is considered final yet.

The current design proposal is:

- [`docs/proposals/0001-verifiable-research-system-v1.md`](docs/proposals/0001-verifiable-research-system-v1.md)

## Development sequence

1. Write durable intent and assurance properties.
2. Generate and critique frontend concepts against realistic research fixtures.
3. Revise the proposal to match the validated user flow.
4. Define typed API/data contracts from that flow.
5. Build a walking vertical slice against fixtures.
6. Replace fixture components incrementally with real implementations while preserving contracts and properties.
7. Add domain assurance packs and deeper benchmarks only where evidence shows they are needed.

The repository, rather than any chat session, is the durable project state.
