# Agent Task: Standalone Mobile Prototype v1

## Read first

1. `docs/development/property-driven-development-v1.md`
2. `assurance/properties/mobile-prototype-v1.yaml`
3. `docs/product/mobile-prototype-slice-v1.md`
4. `prototype/verify_mobile.py`

## Goal

Implement:

```text
prototype/research-assurance-mobile.html
```

Do not depend on this chat for requirements. The files above are authoritative for this task.

## Required work loop

```text
read properties
-> run verifier (expected to fail before artifact exists)
-> implement smallest compliant artifact
-> run static verifier
-> run browser verifier when Playwright is available
-> manually inspect at a phone-sized viewport
-> report exact verification status
```

Commands:

```bash
python prototype/verify_mobile.py
python prototype/verify_mobile.py --browser  # when Playwright is installed
```

## Completion gate

Do not report this task complete unless:

- static verifier passes;
- the artifact exists as one self-contained HTML file;
- Research is visible by default;
- the four surfaces work with JavaScript disabled;
- fixture/demo labeling is visible;
- evidence is inspectable through native HTML disclosure;
- browser verification is either PASS or explicitly recorded as NOT RUN with reason.

## Handoff format

```text
Artifact: prototype/research-assurance-mobile.html
Static verifier: PASS/FAIL
Browser file:// smoke: PASS/FAIL/NOT RUN
JavaScript-disabled navigation: PASS/FAIL/NOT RUN
390x844 overflow: PASS/FAIL/NOT RUN
Known limitations: ...
Changed property files: none | list + rationale
```

If a property appears wrong or impossible, do not silently weaken it. Flag it for review.
