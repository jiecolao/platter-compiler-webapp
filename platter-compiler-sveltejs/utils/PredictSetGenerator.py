"""
Predict Set Generator

Reads a CSV where:
- Column A: non-terminals (dict keys), e.g. <program>
- Column B: predict set text, e.g. { piece, sip, flag, chars }

Generates a predict_set.py in the same folder as the CSV.

Parsing rules implemented:
- Outer { } defines the set.
- Inner '{' or '}' inside the set are treated as literal elements.
- Comma ',' is normally a separator, BUT if it appears where an element is expected
  (e.g., "{ , ,, ) }"), then ',' is treated as an element.
- When merging: same non-terminal keys merged, no duplicates, preserve insertion order (unsorted).
- When NOT merging: repeated non-terminals get suffix _1, _2, ...
- Output dict is ordered with <program> first if present, then in discovery order.
"""

from __future__ import annotations

import csv
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# =========================
# CONFIG (edit these)
# =========================

SEARCH_ROOT = r"."              # Folder to traverse for the CSV (recursive)
CSV_NAME = "predict_set.csv"    # CSV filename to find
MERGE_NONTERMINALS = False       # True => merge duplicates, False => suffix _1, _2, ...
OUTPUT_PY_NAME = "predict_set_nonmerged.py"

HAS_HEADER = False              # Set True if your CSV has a header row
ENCODING = "utf-8-sig"          # utf-8-sig handles Excel BOM nicely

# =========================


MULTI_CHAR_TOKENS = {
    "==", "!=", "<=", ">=", "+=", "-=", "*=", "/=", "%=",
    "&&", "||", "::",
}

SINGLE_CHAR_TOKENS = set("{}()[];:+-*/%<>=!:")


@dataclass
class RowItem:
    key: str
    raw_set: str


def find_csv(root: Path, filename: str) -> Path:
    """Traverse root recursively and return the first matching CSV path."""
    for p in root.rglob(filename):
        if p.is_file():
            return p
    raise FileNotFoundError(f"Could not find '{filename}' under '{root.resolve()}'.")


def read_csv_rows(csv_path: Path, has_header: bool) -> List[RowItem]:
    rows: List[RowItem] = []
    with csv_path.open("r", encoding=ENCODING, newline="") as f:
        reader = csv.reader(f)
        if has_header:
            next(reader, None)

        for i, cols in enumerate(reader, start=1):
            if not cols:
                continue
            # Ensure at least two columns
            if len(cols) < 2:
                continue

            key = (cols[0] or "").strip()
            raw_set = (cols[1] or "").strip()

            if not key:
                continue
            if not raw_set:
                # allow empty set cell -> treat as empty predict set
                raw_set = "{}"

            rows.append(RowItem(key=key, raw_set=raw_set))

    return rows


def extract_outer_set_text(s: str) -> str:
    """
    Return substring inside the OUTERMOST '{' '}'.
    If not found, returns the original string (best-effort).
    """
    first = s.find("{")
    last = s.rfind("}")
    if first != -1 and last != -1 and last > first:
        return s[first + 1:last]
    return s.strip()


def parse_set_elements(raw_set: str) -> List[str]:
    """
    Parse the predict set cell into a list of elements per rules.

    Key behaviors:
    - Outer braces define the set; we parse inside them.
    - Inner '{' and '}' become literal elements.
    - Comma ',' is a separator UNLESS we encounter it when expecting an element;
      then it is treated as an element token ",".
    - Operators like '==', '<=', '+=', etc are preserved.
    - Other single-character punctuation in SINGLE_CHAR_TOKENS becomes its own token.
    """
    inner = extract_outer_set_text(raw_set)
    elements: List[str] = []

    i = 0
    n = len(inner)
    expecting_element = True  # at start, an element may appear (or a comma-as-element)

    def skip_ws(j: int) -> int:
        while j < n and inner[j].isspace():
            j += 1
        return j

    i = skip_ws(i)
    while i < n:
        ch = inner[i]

        # Comma handling (separator vs literal element)
        if ch == ",":
            if expecting_element:
                elements.append(",")
            # comma always also acts like a separator boundary
            expecting_element = True
            i += 1
            i = skip_ws(i)
            continue

        # Treat inner braces as literal elements (outer braces already removed)
        if ch in "{}":
            elements.append(ch)
            expecting_element = False
            i += 1
            i = skip_ws(i)
            continue

        # Multi-char operators (==, <=, +=, etc.)
        if i + 1 < n:
            two = inner[i:i + 2]
            if two in MULTI_CHAR_TOKENS:
                elements.append(two)
                expecting_element = False
                i += 2
                i = skip_ws(i)
                continue

        # Single-char punctuation tokens
        if ch in SINGLE_CHAR_TOKENS:
            elements.append(ch)
            expecting_element = False
            i += 1
            i = skip_ws(i)
            continue

        # Otherwise, read a word-ish token until whitespace or delimiter
        j = i
        while j < n:
            c = inner[j]
            if c.isspace() or c == "," or c in "{}":
                break
            # stop before a single-char token (except '<' '>' which may be part of names)
            # but we already treat SINGLE_CHAR_TOKENS; here we keep scanning until a hard delimiter.
            j += 1

        token = inner[i:j].strip()
        if token:
            elements.append(token)
            expecting_element = False

        i = skip_ws(j)

    return elements


def merge_preserve_order(existing: List[str], new_items: List[str]) -> List[str]:
    """Append items from new_items into existing if not already present, preserving order."""
    seen = set(existing)
    for item in new_items:
        if item not in seen:
            existing.append(item)
            seen.add(item)
    return existing


def build_predict_set(rows: List[RowItem], merge_nonterminals: bool) -> "OrderedDict[str, List[str]]":
    """
    Build predict set dict.
    If merge_nonterminals=True: merge same keys, no duplicates, preserve insertion order.
    Else: rename duplicates with _1, _2, ...
    """
    out: "OrderedDict[str, List[str]]" = OrderedDict()
    dup_counter: Dict[str, int] = {}

    discovery_order: List[str] = []

    for r in rows:
        key = r.key
        elems = parse_set_elements(r.raw_set)

        if merge_nonterminals:
            if key not in out:
                out[key] = []
                discovery_order.append(key)
            out[key] = merge_preserve_order(out[key], elems)
        else:
            if key not in dup_counter:
                dup_counter[key] = 0
                out[key] = elems
                discovery_order.append(key)
            else:
                dup_counter[key] += 1
                new_key = f"{key}_{dup_counter[key]}"
                out[new_key] = elems
                discovery_order.append(new_key)

    # Reorder to start at <program> if it exists (only affects output ordering)
    if "<program>" in out:
        reordered: "OrderedDict[str, List[str]]" = OrderedDict()
        reordered["<program>"] = out["<program>"]
        for k, v in out.items():
            if k == "<program>":
                continue
            reordered[k] = v
        out = reordered

    return out


def format_py_dict(d: "OrderedDict[str, List[str]]") -> str:
    """Format the OrderedDict as a stable, readable Python source string."""
    lines: List[str] = []
    lines.append("# Auto-generated by predict set generator. Do not edit by hand.\n")
    lines.append("PREDICT_SET = {\n")
    for k, v in d.items():
        # Use repr for safe quoting
        items = ", ".join(repr(x) for x in v)
        lines.append(f"    {repr(k)}: [{items}],\n")
    lines.append("}\n")
    return "".join(lines)


def write_predict_set_py(csv_path: Path, predict_set: "OrderedDict[str, List[str]]") -> Path:
    out_path = csv_path.parent / OUTPUT_PY_NAME
    out_path.write_text(format_py_dict(predict_set), encoding="utf-8")
    return out_path


def main() -> None:
    root = Path(SEARCH_ROOT).expanduser().resolve()
    csv_path = find_csv(root, CSV_NAME)

    rows = read_csv_rows(csv_path, HAS_HEADER)
    if not rows:
        raise RuntimeError(f"No usable rows found in CSV: {csv_path}")

    predict_set = build_predict_set(rows, MERGE_NONTERMINALS)
    out_path = write_predict_set_py(csv_path, predict_set)

    print(f"Found CSV: {csv_path}")
    print(f"MERGE_NONTERMINALS={MERGE_NONTERMINALS}")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
