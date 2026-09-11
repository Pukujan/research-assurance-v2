# UX Acceptance v1

- Status: Accepted for v1 structural design
- Date: 2026-09-11
- Scope: Navigation, information hierarchy, interaction model, and visual direction

## Accepted structure

Primary product surfaces:

- Research
- Library
- Reviews
- Audit

Admin remains a secondary organization-management surface.

## Interaction rule

Default layout:

`one main region + optional contextual detail`

Three simultaneous regions are reserved for explicitly forensic workflows.

The normal research experience must not expose every assurance signal at once.

## Research

Research is document-first. The synthesized answer/report is visually dominant.

Default content:
- title/question;
- lightweight run state;
- readable report;
- inline citations/claim markers;
- compact assurance summary;
- follow-up/fork/share actions.

Evidence, provenance, hashes, parser versions, and detailed verifier output are opened on demand rather than shown continuously.

## Library

Library is a calm searchable work list, not a KPI dashboard.

Substantial lists use the same table interaction pattern:
- search;
- useful filters;
- ascending/descending sorting by column where meaningful;
- clear default sort;
- easy filter reset;
- stable row identity.

Expected Library filters may include owner, team, topic, status, date, review state, and visibility.

## Reviews

Reviews are risk-focused rather than report-first.

The queue should surface disputed, unsupported, temporally ambiguous, lineage-sensitive, or materially edited findings before low-risk material.

The reviewer can open the exact claim/evidence/document context from a row.

## Audit

Audit is a forensic mode.

Default presentation is a chronological/filterable event table or timeline with one selected-event detail view. Raw JSON, hashes, model/tool metadata, and low-level provenance remain available but secondary.

## Visual direction

Accepted direction:
- dark-first;
- low glare;
- spacious;
- strong document typography;
- restrained blue/purple/teal accents;
- mildly futuristic / mission-control feeling;
- technical monospace only where it helps.

Avoid:
- dense sci-fi HUD layouts;
- metric mosaics;
- permanent side inspectors;
- neon borders around every component;
- dashboard cards when a table or document is clearer.

Working product phrase:

> Research first. Assurance on demand. Audit when needed.

Desired emotional direction:

> A research pilot building serious systems with AI.

## What is fixed vs flexible

Fixed for v1 unless implementation evidence disproves it:
- primary navigation model;
- document-first Research;
- table-first Library/Reviews/Audit where appropriate;
- contextual evidence inspection;
- progressive disclosure of assurance detail;
- one-main-region default.

Still flexible:
- exact typography;
- spacing;
- component library;
- exact columns;
- exact filter controls;
- color tuning;
- animation;
- mobile adaptations;
- minor tab placement.

No further broad visual exploration is required before contracts. New mockups should be generated only to resolve a specific interaction ambiguity.