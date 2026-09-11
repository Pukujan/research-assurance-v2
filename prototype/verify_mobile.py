#!/usr/bin/env python3
"""Deterministic verifier for the standalone mobile review artifact.

Usage:
    python prototype/verify_mobile.py
    python prototype/verify_mobile.py --browser

The default mode uses only the Python standard library. Browser mode additionally
uses Playwright when installed and verifies the artifact through file:// with
JavaScript disabled at a 390x844 viewport.
"""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

TARGET = Path(__file__).with_name("research-assurance-mobile.html")


class Inspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.default_research_checked = False
        self.details_count = 0
        self.summary_count = 0
        self._hidden_depth = 0
        self.visible_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {k.lower(): (v or "") for k, v in attrs}
        if values.get("id"):
            self.ids.add(values["id"])
        if tag.lower() == "input" and values.get("id") == "tab-research":
            attr_names = {k.lower() for k, _ in attrs}
            self.default_research_checked = "checked" in attr_names
        if tag.lower() == "details":
            self.details_count += 1
        if tag.lower() == "summary":
            self.summary_count += 1
        if tag.lower() in {"style", "script", "head"}:
            self._hidden_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"style", "script", "head"} and self._hidden_depth:
            self._hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._hidden_depth == 0:
            text = " ".join(data.split())
            if text:
                self.visible_text.append(text)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def static_verify(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing artifact: {path}"]

    source = path.read_text(encoding="utf-8")
    lower = source.lower()

    if "<!doctype html" not in lower:
        fail(errors, "missing <!doctype html>")
    if "<meta name=\"viewport\"" not in lower and "<meta name='viewport'" not in lower:
        fail(errors, "missing mobile viewport meta tag")

    forbidden = {
        "fetch(": "runtime fetch() dependency",
        "xmlhttprequest": "XMLHttpRequest dependency",
        "<script src=": "external script dependency",
        "<script src =": "external script dependency",
        "rel=\"stylesheet\"": "external stylesheet dependency",
        "rel='stylesheet'": "external stylesheet dependency",
        "@import url": "CSS import dependency",
        "url(http://": "external CSS URL dependency",
        "url(https://": "external CSS URL dependency",
        "src=\"http://": "external source dependency",
        "src=\"https://": "external source dependency",
        "src='http://": "external source dependency",
        "src='https://": "external source dependency",
    }
    for needle, label in forbidden.items():
        if needle in lower:
            fail(errors, label)

    parser = Inspector()
    try:
        parser.feed(source)
        parser.close()
    except Exception as exc:  # HTMLParser is permissive; this still catches gross input failures.
        fail(errors, f"HTML parser failure: {exc}")
        return errors

    required_ids = {"tab-research", "research", "library", "reviews", "audit"}
    missing_ids = sorted(required_ids - parser.ids)
    if missing_ids:
        fail(errors, f"missing required section/navigation ids: {', '.join(missing_ids)}")

    if not parser.default_research_checked:
        fail(errors, "Research is not the default checked surface")

    text = " ".join(parser.visible_text)
    normalized = text.lower()
    if len(text) < 1200:
        fail(errors, f"insufficient visible fixture content ({len(text)} characters; expected >= 1200)")

    required_phrases = [
        "research assurance",
        "research",
        "library",
        "reviews",
        "audit",
        "verified",
        "disputed",
        "unverified",
        "inference",
        "illustrative",
        "fixture",
    ]
    for phrase in required_phrases:
        if phrase not in normalized:
            fail(errors, f"missing required visible phrase/state: {phrase}")

    if parser.details_count < 2 or parser.summary_count < 2:
        fail(errors, "expected at least two native details/summary disclosures")

    if re.search(r"\bloading(?:\.{3}|…)?\b", normalized) and "fixture" not in normalized:
        fail(errors, "artifact appears to expose a loading shell instead of embedded content")

    return errors


def browser_verify(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return ["browser verification requested but Playwright is not installed"]

    file_url = path.resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 390, "height": 844},
            java_script_enabled=False,
        )
        page = context.new_page()
        external_requests: list[str] = []

        def on_request(req) -> None:  # type: ignore[no-untyped-def]
            if not req.url.startswith("file:"):
                external_requests.append(req.url)

        page.on("request", on_request)
        page.goto(file_url, wait_until="load")

        if not page.locator("#research").is_visible():
            fail(errors, "Research surface is not visible on first open")
        if page.locator("#research").inner_text().strip().__len__() < 300:
            fail(errors, "Research surface contains too little visible report content")

        for control_id, section_id in [
            ("tab-library", "library"),
            ("tab-reviews", "reviews"),
            ("tab-audit", "audit"),
            ("tab-research", "research"),
        ]:
            page.locator(f'label[for="{control_id}"]').click()
            if not page.locator(f"#{section_id}").is_visible():
                fail(errors, f"{section_id} is not reachable with JavaScript disabled")

        details = page.locator("#research details")
        if details.count() < 1:
            fail(errors, "Research has no native evidence disclosure")
        else:
            details.first.locator("summary").click()
            if not details.first.get_attribute("open"):
                fail(errors, "native evidence disclosure did not open")

        overflow = page.evaluate(
            "document.documentElement.scrollWidth - document.documentElement.clientWidth"
        )
        if overflow > 4:
            fail(errors, f"page-level horizontal overflow at 390px viewport: {overflow}px")

        if external_requests:
            fail(errors, "unexpected non-file network requests: " + ", ".join(external_requests))

        context.close()
        browser.close()

    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--browser", action="store_true", help="also run Playwright file:// smoke checks")
    ap.add_argument("path", nargs="?", type=Path, default=TARGET)
    args = ap.parse_args()

    print(f"Verifying {args.path}")
    errors = static_verify(args.path)
    if errors:
        print("STATIC: FAIL")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("STATIC: PASS")

    if args.browser:
        browser_errors = browser_verify(args.path)
        if browser_errors:
            print("BROWSER (JS disabled, 390x844, file://): FAIL")
            for error in browser_errors:
                print(f"  - {error}")
            return 1
        print("BROWSER (JS disabled, 390x844, file://): PASS")
    else:
        print("BROWSER: NOT RUN (use --browser when Playwright is available)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
