# Standalone Mobile Prototype Slice v1

- Status: Ready for implementation
- Date: 2026-09-11
- Intended implementer: local worker agent (for example Luna)
- Durable properties: `assurance/properties/mobile-prototype-v1.yaml`
- Target artifact: `prototype/research-assurance-mobile.html`

## User story

As a user opening a Research Assurance prototype from a phone attachment/download, I can inspect the accepted v1 product surfaces without running a local server and without depending on JavaScript or network access.

## Why this slice exists

The first fixture frontend under `prototype/` depends on JavaScript and fixture fetches. Some mobile attachment/file viewers suppress scripts or block local resource loading, which can produce a blank page.

This slice produces a deliberately portable review artifact. It is not the production frontend architecture.

## Product constraints

Preserve the accepted structural UX:

- Research
- Library
- Reviews
- Audit
- one dominant content area;
- dark, low-glare, spacious visual direction;
- Research is document-first;
- evidence/provenance is progressively disclosed;
- Library/Reviews/Audit use tables where appropriate;
- no KPI dashboard;
- no persistent multi-panel forensic UI;
- collaboration is contextual to research objects, not a chat product.

## Hard implementation requirements

Create exactly one primary artifact:

```text
prototype/research-assurance-mobile.html
```

The artifact must:

- be self-contained HTML + CSS;
- contain fixture content inline;
- have no runtime fetch/XHR;
- have no external stylesheet, script, font, image, module, or CDN dependency;
- open directly through `file://`;
- expose useful content with JavaScript disabled;
- show Research by default;
- use a no-JavaScript navigation mechanism (for example radio controls + labels/anchors + CSS);
- use native HTML disclosure (`details`/`summary`) where useful for evidence and forensic detail;
- label all research data as illustrative fixture/demo content;
- remain readable on desktop while being mobile-first around 390x844.

JavaScript is not required for this slice. If any JavaScript is added, it must be progressive enhancement only: disabling it cannot remove primary navigation, report content, claims, evidence inspection, Library, Reviews, or Audit.

## Research fixture

Use the existing long-duration storage fixture as a UI scenario only. The artifact must make clear that the content is illustrative rather than current research advice.

Research should contain:

- question/title;
- topic chips;
- compact assurance state summary;
- readable report sections;
- inline claim/citation markers;
- VERIFIED, DISPUTED, UNVERIFIED, and INFERENCE claims;
- at least one inspectable claim -> evidence -> source-version path;
- at least one contradiction/qualifier warning;
- Claims disclosure;
- Sources disclosure;
- a small research-scoped Discussion section.

Do not display a fabricated universal confidence percentage.

## Library

Provide a small table/list fixture showing multiple research runs with:

- title;
- owner;
- status;
- review state;
- claim summary;
- updated date.

For this standalone no-JavaScript review artifact, filters do not need to execute dynamically. The visual treatment should demonstrate how search/filter/sort controls will fit, but mobile table behavior is the primary acceptance concern.

The table must be contained in a horizontally scrollable region rather than widening the entire document viewport.

## Reviews

Show a small risk-focused queue containing at least:

- an open HIGH-risk qualifier-preservation finding bound to an exact `DocumentVersion`;
- an approved review for comparison.

Use native disclosure for finding detail if useful.

## Audit

Show a chronological table with HUMAN, MODEL, TOOL, and SYSTEM actors.

At least one event must expose additional detail using native disclosure, including representative component/version and hash/payload metadata.

Keep table rows concise.

## Verification contract

An implementation agent must run:

```bash
python prototype/verify_mobile.py
```

The script is the minimum static oracle and must pass before completion is reported.

### Browser verification

When browser tooling such as Playwright is available, additionally verify the artifact directly from a file URL at a 390x844 viewport.

Required assertions:

1. `Research` is visible immediately on first open.
2. Research report text is visible.
3. Library, Reviews, and Audit can each be selected with JavaScript disabled.
4. At least one native evidence disclosure can be opened with JavaScript disabled.
5. `document.documentElement.scrollWidth` does not materially exceed the viewport width; wide tables scroll within their own containers.
6. No network requests are required for content, fonts, scripts, styles, or images.
7. Capture a screenshot for human review when tooling permits.

If browser tooling is not available, report `browser verification: not run` rather than claiming success.

## Completion record

The implementation agent should include in its PR/checkpoint:

```text
Static verifier: PASS/FAIL
Browser file:// smoke test: PASS/FAIL/NOT RUN
JavaScript-disabled smoke test: PASS/FAIL/NOT RUN
390x844 overflow test: PASS/FAIL/NOT RUN
Known limitations: ...
```

Do not paste large transient reasoning logs into the repository.

## Non-goals

This slice does not:

- replace the fixture-backed prototype architecture;
- define production responsive components;
- add real persistence;
- add authentication;
- add Slack/Teams integration;
- implement living ontology workflows;
- implement theorem proving;
- create a general messaging system.

## Follow-on

After human acceptance of the standalone artifact, return to the main implementation path:

```text
accepted UX + properties
-> revised API contract
-> typed Pydantic/OpenAPI contracts
-> generated TypeScript types/client
-> walking Slice 1: identity -> create run -> SQLite -> Library -> AuditEvent
```
