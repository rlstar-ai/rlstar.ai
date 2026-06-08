#!/usr/bin/env python3
"""
build.py — Generate algorithms.js from algorithms/**/*.md

Usage:
    python build.py

Each .md file must begin with a YAML frontmatter block (between --- delimiters).
Required fields:  id, name, full, category, year, affiliation, paper, connects
Optional fields:  code, venue, stars, formula

The script reads all .md files, sorts by year then id, and writes algorithms.js.
"""

import os
import re
import json
import glob

ALGO_DIR = os.path.join(os.path.dirname(__file__), "algorithms")
OUT_FILE = os.path.join(os.path.dirname(__file__), "algorithms.js")

REQUIRED = {"id", "name", "full", "category", "year", "affiliation", "paper", "connects"}
# Auto-discover valid categories from subdirectory names — no manual list needed.
VALID_CATEGORIES = {
    d for d in os.listdir(ALGO_DIR)
    if os.path.isdir(os.path.join(ALGO_DIR, d))
}


def extract_desc(text):
    """Extract first sentence from ## Core Idea section as desc fallback."""
    m = re.search(r"##\s+Core Idea\s*\n+(.+?)(?:\n\n|\n##|$)", text, re.DOTALL)
    if not m:
        return ""
    # Collapse whitespace, take first sentence (up to . or end)
    body = re.sub(r"\s+", " ", m.group(1).strip())
    # Strip markdown formatting
    body = re.sub(r"\*\*(.+?)\*\*", r"\1", body)
    body = re.sub(r"\$.*?\$", "", body).strip()
    # First sentence only (≤ 200 chars)
    sentence = re.split(r"(?<=[.!?])\s", body)[0]
    return sentence[:200]


def parse_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()

    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        raise ValueError(f"{path}: missing or malformed YAML frontmatter")

    raw = m.group(1)
    data = {}

    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        if ":" not in stripped:
            i += 1
            continue
        key, _, val = stripped.partition(":")
        key = key.strip()
        val = val.strip()

        # Multi-line mapping block: "improves:" with no inline value,
        # followed by indented "  target_id: description" lines.
        if key == "improves" and val == "":
            mapping = {}
            i += 1
            while i < len(lines):
                sub = lines[i]
                # Stop if line is not indented (back to top-level)
                if sub and not sub.startswith(" ") and not sub.startswith("\t"):
                    break
                sub_stripped = sub.strip()
                if sub_stripped and ":" in sub_stripped:
                    sub_key, _, sub_val = sub_stripped.partition(":")
                    v = sub_val.strip()
                    # Strip surrounding quotes added by YAML-style "value"
                    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
                        v = v[1:-1]
                    mapping[sub_key.strip()] = v
                i += 1
            data[key] = mapping
            continue

        # Parse connects list:  [a, b, c]  or  []
        if key == "connects":
            val = val.strip("[]")
            data[key] = [v.strip() for v in val.split(",") if v.strip()] if val else []
        # Parse year / stars as int when possible
        elif key in ("year", "stars"):
            try:
                data[key] = int(val)
            except ValueError:
                data[key] = val  # keep as string if e.g. "~"
        else:
            data[key] = val

        i += 1

    return data


def js_value(v):
    if isinstance(v, list):
        return "[" + ", ".join(json.dumps(x) for x in v) + "]"
    if isinstance(v, dict):
        pairs = ", ".join(
            json.dumps(k, ensure_ascii=False) + ": " + js_value(val)
            for k, val in v.items()
        )
        return "{" + pairs + "}"
    if isinstance(v, int):
        return str(v)
    return json.dumps(v, ensure_ascii=False)


def build():
    md_files = sorted(glob.glob(os.path.join(ALGO_DIR, "**", "*.md"), recursive=True))
    if not md_files:
        print(f"No .md files found under {ALGO_DIR}")
        return

    algos = []
    errors = []

    for path in md_files:
        try:
            data = parse_frontmatter(path)
        except ValueError as e:
            errors.append(str(e))
            continue

        missing = REQUIRED - set(data.keys())
        if missing:
            errors.append(f"{path}: missing required fields: {', '.join(sorted(missing))}")
            continue

        if data["category"] not in VALID_CATEGORIES:
            errors.append(f"{path}: unknown category '{data['category']}' — must be one of {VALID_CATEGORIES}")
            continue

        # Auto-extract desc from Core Idea if not explicitly set
        if not data.get("desc"):
            with open(path, encoding="utf-8") as f:
                full_text = f.read()
            data["desc"] = extract_desc(full_text)

        algos.append((path, data))

    if errors:
        print("Errors found — fix before generating:")
        for e in errors:
            print(f"  ✗ {e}")
        return

    # Sort by year, then id
    algos.sort(key=lambda x: (x[1].get("year", 9999), x[1]["id"]))

    # Field order for readability in the output JS
    FIELD_ORDER = ["id", "name", "full", "category", "year", "affiliation",
                   "desc", "formula", "paper", "code", "venue", "stars", "connects", "improves"]

    lines = []
    lines.append("// algorithms.js — AUTO-GENERATED by build.py")
    lines.append("// Do NOT edit by hand. Edit the .md files in algorithms/ instead.")
    lines.append("// Run:  python build.py")
    lines.append("")
    lines.append("const ALGORITHMS = [")
    lines.append("")

    category_comments = {
        "foundation": "// ── Foundation ───────────────────────────────────────────────────",
        "reasoning":  "// ── Reasoning-RL ─────────────────────────────────────────────────",
        "report":     "// ── Tech Report ──────────────────────────────────────────────────",
        "agentic":    "// ── Agentic-RL ───────────────────────────────────────────────────",
        "alignment":  "// ── Alignment ────────────────────────────────────────────────────",
    }
    seen_categories = set()

    for path, data in algos:
        cat = data["category"]
        if cat not in seen_categories:
            seen_categories.add(cat)
            lines.append(f"  {category_comments.get(cat, '')}")

        # Build object fields in order, skipping absent optional ones
        fields = []
        for key in FIELD_ORDER:
            if key not in data:
                continue
            val = data[key]
            # Skip empty optional fields
            if val in ("", None, "~", []):
                continue
            fields.append(f"    {key}: {js_value(val)}")

        obj = "  {\n" + ",\n".join(fields) + "\n  }"
        lines.append(obj + ",")

    lines.append("")
    lines.append("];")
    lines.append("")

    out = "\n".join(lines)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(out)

    print(f"✓ Written {len(algos)} algorithms to {OUT_FILE}")
    for _, d in algos:
        print(f"  {d['category']:12s}  {d['id']}")


if __name__ == "__main__":
    build()
