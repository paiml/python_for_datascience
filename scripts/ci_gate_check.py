#!/usr/bin/env python3
"""Structural checks for the `gate` status context.

This repository is a Jupyter Book / Jekyll course: notebooks, YAML config, a
table of contents and two helper scripts. There is no test suite to aggregate,
so the gate measures the things this repo actually IS.

Every check prints its DENOMINATOR ("checked N ...") and FAILS when N is zero.
A check that silently inspected nothing must never read as a pass.

`selftest` proves each checker can actually fail: it builds deliberately broken
fixtures in a temp directory and asserts every checker rejects them. A guard
that has never been shown to fail is not evidence of anything.

Usage:
    ci_gate_check.py notebooks | yaml | json | python | toc | lessons | selftest
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - surfaced as a hard failure, never a skip
    print("FAIL: PyYAML is not importable; the YAML checks cannot run.", file=sys.stderr)
    print("An absent verifier is a NO-GO, not a pass.", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent


def discover(root: Path, suffixes: tuple[str, ...]) -> list[Path]:
    """Tracked files under `root` matching `suffixes`.

    Uses `git ls-files` inside a checkout so untracked scratch files can never
    inflate or deflate a denominator; falls back to a walk for selftest
    fixtures, which are not git repositories.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        names = [n for n in out.split("\0") if n]
    except (subprocess.CalledProcessError, FileNotFoundError):
        names = [
            str(p.relative_to(root))
            for p in root.rglob("*")
            if p.is_file()
        ]
    return sorted(root / n for n in names if n.endswith(suffixes))


def report(kind: str, n: int, errors: list[str]) -> int:
    for e in errors:
        print(f"  ERROR: {e}")
    print(f"checked {n} {kind}")
    if n == 0:
        print(f"FAIL: found 0 {kind} to check - the check inspected nothing.")
        return 1
    if errors:
        print(f"FAIL: {len(errors)} of {n} {kind} are broken.")
        return 1
    print(f"OK: {n} {kind} pass.")
    return 0


# --------------------------------------------------------------------------
# checkers: each returns (denominator, errors)
# --------------------------------------------------------------------------

def _cell_defects(cells: list, rel) -> list[str]:
    return [
        f"{rel}: cell {i} lacks 'cell_type'/'source'"
        for i, cell in enumerate(cells)
        if not isinstance(cell, dict)
        or "cell_type" not in cell
        or "source" not in cell
    ]


def _notebook_defects(nb, rel) -> list[str]:
    if not isinstance(nb, dict):
        return [f"{rel}: top level is {type(nb).__name__}, expected object"]
    errors: list[str] = []
    if not isinstance(nb.get("nbformat"), int):
        errors.append(f"{rel}: missing or non-integer 'nbformat'")
    cells = nb.get("cells")
    if not isinstance(cells, list):
        errors.append(f"{rel}: missing or non-list 'cells'")
        return errors
    return errors + _cell_defects(cells, rel)


def check_notebooks(root: Path) -> tuple[int, list[str]]:
    files = discover(root, (".ipynb",))
    errors: list[str] = []
    for f in files:
        rel = f.relative_to(root)
        try:
            nb = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"{rel}: not valid JSON: {exc}")
            continue
        errors.extend(_notebook_defects(nb, rel))
    return len(files), errors


def check_yaml(root: Path) -> tuple[int, list[str]]:
    files = discover(root, (".yml", ".yaml"))
    errors: list[str] = []
    for f in files:
        try:
            yaml.safe_load(f.read_text(encoding="utf-8"))
        except (yaml.YAMLError, UnicodeDecodeError) as exc:
            errors.append(f"{f.relative_to(root)}: invalid YAML: {exc}")
    return len(files), errors


def check_json(root: Path) -> tuple[int, list[str]]:
    files = discover(root, (".json",))
    errors: list[str] = []
    for f in files:
        try:
            json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"{f.relative_to(root)}: invalid JSON: {exc}")
    return len(files), errors


def check_python(root: Path) -> tuple[int, list[str]]:
    files = discover(root, (".py",))
    errors: list[str] = []
    for f in files:
        try:
            compile(f.read_text(encoding="utf-8"), str(f), "exec")
        except (SyntaxError, ValueError, UnicodeDecodeError) as exc:
            errors.append(f"{f.relative_to(root)}: does not compile: {exc}")
    return len(files), errors


def _toc_urls(node, out: list[str]) -> None:
    """Collect internal (non-external) urls from a jupyter-book toc tree."""
    if isinstance(node, list):
        for item in node:
            _toc_urls(item, out)
    elif isinstance(node, dict):
        url = node.get("url")
        if isinstance(url, str) and not node.get("external") and url.startswith("/"):
            out.append(url)
        _toc_urls(node.get("sections"), out)


def check_toc(root: Path) -> tuple[int, list[str]]:
    """Every internal toc entry must resolve to a real file under content/.

    This is what catches a renamed or deleted lesson: the book still builds a
    sidebar entry, but the page behind it is gone.
    """
    tocs = [p for p in discover(root, (".yml",)) if p.name == "toc.yml"]
    errors: list[str] = []
    checked = 0
    for toc in tocs:
        book_root = toc.parent.parent  # <book>/_data/toc.yml
        content = book_root / "content"
        if not content.is_dir():
            errors.append(f"{toc.relative_to(root)}: no content/ dir beside it")
            continue
        urls: list[str] = []
        _toc_urls(yaml.safe_load(toc.read_text(encoding="utf-8")), urls)
        for url in urls:
            checked += 1
            stem = content / url.lstrip("/")
            if not any(
                stem.with_suffix(ext).is_file() for ext in (".md", ".ipynb", ".markdown")
            ):
                errors.append(
                    f"{toc.relative_to(root)}: url {url} resolves to no "
                    f"{stem.relative_to(book_root)}.{{md,ipynb}}"
                )
    return checked, errors


def check_lessons(root: Path) -> tuple[int, list[str]]:
    """`make book` copies the top-level Colab notebooks into content/lessons/.

    If a lesson exists at the top level but not under content/lessons/, the
    published book is silently missing it until someone re-runs `make book`.
    """
    lessons_dir = root / "content" / "lessons"
    top = [p for p in discover(root, (".ipynb",)) if p.parent == root]
    errors: list[str] = []
    if not lessons_dir.is_dir():
        errors.append("content/lessons/ does not exist")
        return len(top), errors
    for nb in top:
        if not (lessons_dir / nb.name).is_file():
            errors.append(
                f"{nb.name} is not published to content/lessons/ (run `make book`)"
            )
    return len(top), errors


CHECKS = {
    "notebooks": ("notebook(s)", check_notebooks),
    "yaml": ("YAML file(s)", check_yaml),
    "json": ("JSON file(s)", check_json),
    "python": ("Python file(s)", check_python),
    "toc": ("table-of-contents entr(ies)", check_toc),
    "lessons": ("top-level lesson notebook(s)", check_lessons),
}


# --------------------------------------------------------------------------
# selftest: prove every checker can fail
# --------------------------------------------------------------------------

GOOD_NB = json.dumps(
    {"nbformat": 4, "nbformat_minor": 0, "metadata": {}, "cells": [
        {"cell_type": "markdown", "source": ["# hi"], "metadata": {}}]}
)


def _fixture(tmp: Path, name: str, files: dict[str, str]) -> Path:
    root = tmp / name
    for rel, body in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
    return root


def _selftest_cases() -> list:
    """(label, checker, broken fixture, empty fixture-or-None)."""
    good_toc = (
        "- title: Home\n  url: /intro\n"
        "- title: Ext\n  url: https://example.com\n  external: true\n"
    )
    no_source = {"README.md": "x"}
    return [
        ("notebooks", check_notebooks, {"a.ipynb": "{not json"}, no_source),
        ("notebooks-shape", check_notebooks,
         {"a.ipynb": json.dumps({"nbformat": 4, "cells": [{"source": []}]})}, None),
        ("yaml", check_yaml, {"a.yml": "a:\n  - b\n c: bad indent\n"}, no_source),
        ("json", check_json, {"a.json": "{,}"}, no_source),
        ("python", check_python, {"a.py": "def broken(:\n"}, no_source),
        ("toc", check_toc,
         {"_data/toc.yml": good_toc, "content/other.md": "x"},
         {"_data/toc.yml": "- title: Ext\n  url: https://e.com\n  external: true\n",
          "content/intro.md": "x"}),
        ("lessons", check_lessons,
         {"L1.ipynb": GOOD_NB, "content/lessons/keep.md": "x"}, no_source),
    ]


def _assert_rejects(label: str, fn, root: Path) -> int:
    """A checker must report at least one error on a deliberately broken tree."""
    n, errors = fn(root)
    if not errors:
        print(f"  SELFTEST FAIL: {label} accepted a broken fixture")
        return 1
    print(f"  selftest ok: {label} rejects broken input (n={n})")
    return 0


def _assert_zero_denominator(label: str, fn, root: Path) -> int:
    """A checker must report denominator 0 when there is nothing to inspect."""
    n, _ = fn(root)
    if n != 0:
        print(f"  SELFTEST FAIL: {label} counted {n} on an empty fixture")
        return 1
    print(f"  selftest ok: {label} reports denominator 0 on empty input")
    return 0


def selftest() -> int:
    cases = _selftest_cases()
    failures = 0
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        for i, (label, fn, broken, empty) in enumerate(cases):
            failures += _assert_rejects(label, fn, _fixture(tmp, f"broken{i}", broken))
            if empty is not None:
                failures += _assert_zero_denominator(
                    label, fn, _fixture(tmp, f"empty{i}", empty)
                )
    print(f"checked {len(cases)} checker(s) for falsifiability")
    if failures:
        print(f"FAIL: {failures} selftest assertion(s) failed.")
        return 1
    print("OK: every checker demonstrably fails on broken input.")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    name = argv[1]
    if name == "selftest":
        return selftest()
    if name not in CHECKS:
        print(f"unknown check: {name}", file=sys.stderr)
        return 2
    kind, fn = CHECKS[name]
    n, errors = fn(REPO)
    return report(kind, n, errors)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
