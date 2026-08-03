#!/usr/bin/env python3
"""Whole-site check. Run from the repository root after rebuilding a course.

    python3 site/check-site.py

make-course.sh already warns about diagrams the HTML asks for and never got.
This looks at everything else that can go wrong silently - the failures that
produce no error, no warning, and no visible difference on the page:

  * an empty or course-name-only <title>, so the page is untitled in tabs,
    bookmarks and search results;
  * unbalanced <div>s, which nest the next page section inside the last one;
  * tex4ht internals (m@th, \\mathchar) leaking into the prose;
  * generator group names (S8A, S4Q3, ...) printed as literal text, which has
    shipped once already;
  * a section page with no question box, or two pages sharing one giscus key.

The last of those is why the key snapshot exists. Thread keys are built from
the section title, so a retitled section silently orphans its discussion - the
questions are still in GitHub Discussions but no page shows them any more.
site/discussion-keys.txt is the committed list of every key currently live.
Rewrite a heading deliberately and update it in the same commit; see a key go
missing without meaning it, and put the heading back.
"""
import glob
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "site" / "discussion-keys.txt"

fail = 0
allkeys = []
rows = []

for c in sorted(glob.glob(str(ROOT / "courses" / "*" / "build"))):
    course = Path(c).parent.name
    pages = sorted(glob.glob(c + "/*.html"))
    if not pages:
        continue
    refs, bad, empty, leak, stray, keys, boxes = set(), [], [], [], [], [], 0
    for p in pages:
        h = Path(p).read_text(encoding="utf-8")
        name = os.path.basename(p)
        refs |= {os.path.basename(x) for x in re.findall(r"src='([^']+\.svg)'", h)}
        if h.count("<div") != h.count("</div>"):
            bad.append(name)
        t = re.search(r"<title>(.*?)</title>", h, re.S)
        if not t or not t.group(1).strip():
            empty.append(name)
        if "m@th" in h or "mathchar" in h:
            leak.append(name)
        stray += [(name, m) for m in re.findall(r">\s*(S\d+[A-Z]?\d*[A-Z]?)\s*<", h)]
        k = re.search(r'data-term="([^"]+)"', h)
        if k:
            keys.append(k.group(1))
        if "giscus" in h:
            boxes += 1
        # A page with its own heading is a page a reader can be stuck on.
        elif re.search(r"class='(?:sub){0,2}sectionHead'", h):
            bad.append(f"{name} (heading but no question box)")
    have = {os.path.basename(x) for x in glob.glob(c + "/*.svg")}
    problems = [x for x in (
        f"missing diagrams {sorted(refs - have)}" if refs - have else "",
        f"empty titles {empty}" if empty else "",
        f"unbalanced or boxless {bad}" if bad else "",
        f"tex4ht leaks {leak}" if leak else "",
        f"stray group names {stray}" if stray else "",
        f"duplicate keys {sorted({k for k in keys if keys.count(k) > 1})}"
        if len(keys) != len(set(keys)) else "",
    ) if x]
    fail += len(problems)
    rows.append((course, len(pages), len(have), boxes, problems))
    allkeys += keys

for course, npages, ndia, nbox, problems in rows:
    print(f"{course:34s} {npages:3d} pages  {ndia:3d} diagrams  {nbox:3d} question boxes")
    for x in problems:
        print(f"{'':34s}   FAIL {x}")

dup = sorted({k for k in allkeys if allkeys.count(k) > 1})
print(f"\nsite total: {len(allkeys)} keys, {len(set(allkeys))} unique, "
      f"duplicates={dup or 'none'}")
fail += bool(dup)

if SNAPSHOT.exists():
    before = {l.strip() for l in SNAPSHOT.read_text().splitlines() if l.strip()}
    lost = sorted(before - set(allkeys))
    new = sorted(set(allkeys) - before)
    print(f"against {SNAPSHOT.name}: {len(before)} recorded, "
          f"{len(before & set(allkeys))} still live")
    if new:
        print(f"  NEW (add to the snapshot): {len(new)}")
        for k in new[:10]:
            print(f"    + {k}")
    if lost:
        fail += 1
        print(f"  LOST - these discussions are now orphaned: {len(lost)}")
        for k in lost:
            print(f"    - {k}")
else:
    print(f"no snapshot at {SNAPSHOT} - write one with:")
    print("  python3 site/check-site.py --write-keys")

if "--write-keys" in sys.argv:
    SNAPSHOT.write_text("\n".join(sorted(set(allkeys))) + "\n")
    print(f"\nwrote {len(set(allkeys))} keys to {SNAPSHOT}")

print("\nRESULT:", "OK" if not fail else f"{fail} PROBLEM(S)")
sys.exit(1 if fail else 0)
