# Fixture Pack v0

This fixture pack drives the first interactive frontend before a production backend exists.

## Primary scenario

Use a neutral cross-domain research question:

> Compare long-duration battery storage and green hydrogen for grid balancing, focusing on efficiency, duration, infrastructure needs, and uncertainty.

The scenario should include:

- one completed ResearchRun;
- one in-progress ResearchRun;
- one teammate ResearchRun visible in Library;
- one overlapping ResearchRun sharing at least one SourceVersion;
- at least six Claims across VERIFIED, DISPUTED, UNVERIFIED, and INFERENCE states;
- exact EvidenceSpans for every visible citation;
- at least one CONTRADICTS edge;
- at least one calculated ClaimIR with units;
- at least one unknown IR field preserved as unknown;
- at least three SourceVersions, including two independent roots and one downstream/derived source;
- one DocumentVersion awaiting review;
- one ReviewQueueItem with a HIGH risk reason;
- at least five AuditEvents across HUMAN, MODEL, SYSTEM, and TOOL actors.

## Library table coverage

Fixture runs must support testing:

- text search;
- owner filter;
- team filter;
- topic filter;
- status filter;
- review-state filter;
- ascending/descending sorting by updated date, title, owner, status, and review state;
- stable row identity while sorting/filtering.

## Research screen coverage

The selected run must provide:

- title/question;
- topics;
- readable report sections;
- inline claim/citation markers;
- compact assurance summary;
- claim list;
- evidence inspector projection;
- source-version details behind progressive disclosure.

## Reviews coverage

Include at least:

- one disputed claim;
- one qualifier-preservation warning;
- one already approved review for comparison;
- one open review bound to an exact DocumentVersion.

## Audit coverage

Events must support filtering by:

- actor type;
- event type;
- status;
- time;
- run.

The selected event may expose raw payload/hashes in a detail drawer, but table rows stay concise.

## Ontology scope

The fixture may include a placeholder ontology version identifier in the run manifest, but must not require ontology editing or living-ontology workflows yet.

## Next implementation step

Create fixture JSON matching `docs/contracts/api-contracts-v0.md`, then build Research, Library, Reviews, and Audit screens against the fixtures before introducing real persistence.