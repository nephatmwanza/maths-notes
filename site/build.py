#!/usr/bin/env python3
"""
Post-process tex4ht output into finished course pages.

tex4ht gets the *structure* right — split pages, working navigation, correct
maths — but the presentation is plain and it loses some semantics on the way.
This script closes that gap. It is deliberately a post-processing step rather
than a fork of tex4ht: the conversion stays a stock, reproducible command, and
everything opinionated lives here where it can be read and changed.

What it does, per page:

1. TAGS THEOREM BLOCKS BY TYPE. tex4ht marks Definition, Theorem, Lemma,
   Example and Remark all as `class='newtheorem'`, so they are visually
   identical. The type is only recoverable from the bold label inside the
   block, so we read that and add `nt-definition`, `nt-theorem`, etc. This is
   what lets the stylesheet colour them apart — the single biggest readability
   win in the whole pipeline.
2. WRAPS PROOFS so they can be styled as subordinate to the statement above.
3. BUILDS A SIDEBAR from the generated contents page, marks the current page,
   and injects it into every page — the persistent course tree that Paul's
   Online Notes uses and that tex4ht does not provide.
4. REPLACES the bare `[next] [prev] [up]` link row with a proper page-footer
   nav.
5. ADDS a giscus question box at the foot of each section page, so a learner
   can ask about the specific topic rather than in a general forum.

Usage:  python3 build.py <course-dir>
        e.g. python3 build.py ../courses/introduction-to-probability
"""
from __future__ import annotations

import re
import sys
from html import unescape
from pathlib import Path

# Recognised theorem-like environments, in the order we test for them.
THEOREM_TYPES = [
    "definition", "theorem", "lemma", "proposition", "corollary",
    "example", "exercise", "remark", "note", "conjecture",
    "problem", "technique", "fact",
]

# giscus - the per-section question box, backed by GitHub Discussions.
#
# To switch it on: make the repo public, enable Discussions with a "Q&A"
# category, install the giscus app (github.com/apps/giscus), then read the two
# IDs off giscus.app and paste them below with GISCUS_READY = True.
#
# It stays off until all four values are real. A half-configured widget fails
# silently in the reader's browser, which is worse than the honest placeholder
# the pages show now.
GISCUS_READY = True
GISCUS = {
    "repo": "nephatmwanza/maths-notes",
    "repo_id": "R_kgDOTowVJw",
    "category": "Q&A",
    "category_id": "DIC_kwDOTowVJ84DCaQH",
}

# Privacy-friendly page analytics, same as the climate site uses. Set the site
# code (the subdomain you choose at goatcounter.com) to switch it on. Left
# empty, no script is emitted at all - so no third-party request is made and
# nothing needs disclosing to readers.
GOATCOUNTER_CODE = "wjmaths"


def theorem_type(block: str) -> str | None:
    """Read the bold label at the head of a theorem block to recover its type."""
    head = re.search(r"<span class='head'>(.*?)</span>", block, re.S)
    text = unescape(re.sub(r"<[^>]+>", " ", head.group(1) if head else block[:400])).lower()
    for t in THEOREM_TYPES:
        if re.search(rf"\b{t}\b", text):
            return t
    return None


def tag_theorems(html: str) -> str:
    """Add a type class to each generic `newtheorem` div."""
    out, pos = [], 0
    for m in re.finditer(r"<div class='newtheorem'>", html):
        # find this div's matching close so we only inspect its own content
        start = m.end()
        depth, i = 1, start
        while depth and i < len(html):
            nxt = re.search(r"<div\b|</div>", html[i:])
            if not nxt:
                break
            i += nxt.end()
            depth += 1 if nxt.group(0) != "</div>" else -1
        t = theorem_type(html[start:i])
        cls = f"newtheorem nt-{t}" if t else "newtheorem"
        out.append(html[pos:m.start()])
        out.append(f"<div class='{cls}'>")
        pos = m.end()
    out.append(html[pos:])
    return "".join(out)


def collapse_solutions(html: str) -> str:
    """Hide practice-problem solutions behind a disclosure control.

    A solution printed directly under its problem is read instead of attempted,
    which is most of its value gone. Every solution that follows a problem
    becomes a collapsed <details> - no JavaScript, works without it, and stays
    keyboard- and screen-reader-accessible.

    Only solutions attached to a `problem` are collapsed. Worked examples in the
    body of the notes are exposition and stay open.

    Runs after tag_theorems(), which is what puts the `nt-problem` class on the
    block - tex4ht itself marks every theorem-like environment the same way.
    """
    out, pos, armed = [], 0, False
    for m in re.finditer(r"<div class='(newtheorem nt-problem|proof)'>", html):
        kind = m.group(1)
        if kind != "proof":
            armed = True
            continue
        if not armed:
            continue
        armed = False
        # find this proof div's matching close
        depth, i = 1, m.end()
        while depth and i < len(html):
            nxt = re.search(r"<div\b|</div>", html[i:])
            if not nxt:
                break
            i += nxt.end()
            depth += 1 if nxt.group(0) != "</div>" else -1
        out.append(html[pos:m.start()])
        out.append(
            "<details class='solution'><summary>Show solution</summary>"
            "<div class='proof'>" + html[m.end():i] + "</details>"
        )
        pos = i
    out.append(html[pos:])
    return "".join(out)


# NOTE: proofs need no wrapping here. tex4ht already emits `<div class='proof'>`
# around them; an earlier version of this script added a second one, which left
# an unbalanced div that browsers silently repaired. The stylesheet targets
# tex4ht's own `.proof` class directly.


def read_toc(build: Path) -> list[dict]:
    """Parse the generated contents page into a flat nav structure."""
    toc_files = sorted(build.glob("*li1.html"))
    if not toc_files:
        return []
    html = toc_files[0].read_text(encoding="utf-8", errors="replace")
    items = []
    # Which page kinds appear depends on the document class. The probability
    # notes use \chapter, so tex4ht emits chN/seN and subsections stay inside
    # their section's page. These statistics notes are an `article` with
    # \section at the top, so subsections get pages of their own (suN) - and
    # matching only ch/se left ten of nineteen pages reachable by next/prev
    # alone, absent from the sidebar entirely.
    for m in re.finditer(
        r"href='([^']*?(?:ch|se|su)\d+\.html)#[^']*'>([^<]+)", html
    ):
        href, label = m.group(1), unescape(m.group(2)).strip()
        stem = Path(href).stem
        if re.search(r"ch\d+$", stem):
            kind = "ch"
        elif re.search(r"su\d+$", stem):
            kind = "sub"
        else:
            kind = "sec"
        items.append({"href": href, "label": label, "kind": kind})

    # A document with no chapters has sections as its top level, so they should
    # read as headings rather than as indented children of nothing.
    if not any(i["kind"] == "ch" for i in items):
        for i in items:
            if i["kind"] == "sec":
                i["kind"] = "ch"
    return items


# A numbered equation environment. `equation*`/`align*` carry no number, so the
# trailing `\b` (not `[*]`) matters.
NUMBERED_EQ = re.compile(r"\\begin\s*\{(equation|align|gather|multline)\}")


def equation_numbering(build: Path, items: list[dict]) -> dict[str, tuple[int, int]]:
    """Work out what number LaTeX gives each page's equations.

    Splitting the document hands MathJax a problem it cannot see: it numbers
    equations per *page*, restarting at 1, while LaTeX numbers them per
    *chapter*, continuing across the sections a chapter is split into. So a
    display that LaTeX calls (2.2) renders as (1), and an \\eqref pointing at
    it - which tex4ht resolves using LaTeX's number - says 2.2. The two
    disagree on the same page.

    Returns {page: (chapter_number, offset)} so each page can be told which
    chapter it is in and how many numbered equations came before it.
    """
    chapter_of: dict[str, int] = {}
    order: list[str] = []
    chapter = 0
    for it in items:
        href = it["href"]
        if re.match(r".*ch\d+\.html$", href):
            chapter += 1
        if href not in chapter_of:
            chapter_of[href] = max(chapter, 1)
            order.append(href)

    numbering, seen = {}, {}
    for href in order:
        page = build / href
        if not page.is_file():
            continue
        ch = chapter_of[href]
        count = len(NUMBERED_EQ.findall(
            page.read_text(encoding="utf-8", errors="replace")))
        numbering[href] = (ch, seen.get(ch, 0))
        seen[ch] = seen.get(ch, 0) + count
    return numbering


def sidebar(items: list[dict], current: str, course_title: str) -> str:
    rows = [
        '<aside class="sidebar" id="sidebar">',
        '<a class="sb-brand" href="../../../site/index.html">'
        '<span class="tile">WJ</span>WJ <span>Maths</span></a>',
        f'<div class="sb-course">{course_title}</div>',
        '<ul class="sb-nav">',
    ]
    for it in items:
        cls = {"ch": "ch", "sub": "sub"}.get(it["kind"], "sec")
        cur = " current" if it["href"] == current else ""
        rows.append(
            f'<li class="{cls}"><a class="{cur.strip()}" href="{it["href"]}">'
            f'{it["label"]}</a></li>'
        )
    rows += ["</ul>", "</aside>"]
    return "\n".join(rows)


def page_nav(html: str) -> str:
    """Turn tex4ht's `[next] [prev] [up]` row into a styled footer nav."""
    links = dict(re.findall(r"<a href='([^']+)'>(next|prev|up)</a>", html))
    inv = {v: k for k, v in links.items()}
    parts = []
    if "prev" in inv:
        parts.append(f'<a class="prev" href="{inv["prev"]}">&larr; Previous</a>')
    if "up" in inv:
        parts.append(f'<a class="up" href="{inv["up"]}">Contents</a>')
    if "next" in inv:
        parts.append(f'<a class="next" href="{inv["next"]}">Next &rarr;</a>')
    return f'<nav class="pagenav">{"".join(parts)}</nav>' if parts else ""


def discussion_term(course_title: str, section_title: str) -> str:
    """A stable, readable key for the discussion thread behind a page.

    giscus offers `pathname` or a page-stem term. Both are fragile here:
    inserting one section renumbers every page after it, so `intro_probse4`
    silently becomes a different topic and its thread orphans. A slug built
    from the section's own title survives insertions, and it also means the
    Discussions tab lists something legible - "counting-techniques" rather than
    "intro_probse5" - so it is possible to see at a glance which topics readers
    are actually stuck on.
    """
    def slug(s: str) -> str:
        s = unescape(re.sub(r"<[^>]+>", " ", s)).lower()
        s = re.sub(r"[^a-z0-9]+", "-", s)
        return re.sub(r"^-+|-+$", "", s)[:70]
    return f"{slug(course_title)}/{slug(section_title)}"


def qa_block(page_id: str) -> str:
    heading = (
        '<section class="qa"><h2>Questions on this section</h2>'
        "<p>Stuck on something here? Ask below and it stays attached to this topic.</p>"
    )
    if not GISCUS_READY:
        return heading + (
            '<p style="opacity:.65">Discussion will be enabled when the site goes live.</p>'
            "</section>"
        )
    return heading + (
        '<script src="https://giscus.app/client.js"'
        f' data-repo="{GISCUS["repo"]}" data-repo-id="{GISCUS["repo_id"]}"'
        f' data-category="{GISCUS["category"]}" data-category-id="{GISCUS["category_id"]}"'
        f' data-mapping="specific" data-term="{page_id}"'
        ' data-reactions-enabled="1" data-emit-metadata="0" data-input-position="top"'
        ' data-loading="lazy"'
        ' data-theme="preferred_color_scheme" data-lang="en" crossorigin="anonymous" async>'
        "</script></section>"
    )


MARKER = "<!-- built by site/build.py -->"


def process(path: Path, items: list[dict], course_title: str,
            numbering: tuple[int, int] | None = None) -> bool:
    html = path.read_text(encoding="utf-8", errors="replace")

    # Not idempotent: a second pass would nest another layout shell and a second
    # sidebar inside the first. Always run this on fresh conversion output.
    if MARKER in html:
        return False

    html = tag_theorems(html)
    html = collapse_solutions(html)

    # our stylesheet, after tex4ht's so it wins
    head_extra = '<link rel="stylesheet" href="../../../site/assets/notes.css">'
    if GOATCOUNTER_CODE:
        head_extra += (
            f'\n<script data-goatcounter="https://{GOATCOUNTER_CODE}.goatcounter.com/count"'
            ' async src="//gc.zgo.at/count.js"></script>'
        )
    html = html.replace("</head>", head_extra + "\n</head>")

    # Serve MathJax from this site rather than jsDelivr. tex4ht hardcodes the
    # CDN, which means every reader waits on a ~1MB third-party download before
    # any formula is legible - on a slow mobile connection the page sits there
    # showing upright, mis-spaced maths for several seconds. Same-origin means
    # it caches with the rest of the site and works offline once visited.
    html = re.sub(
        r"https://cdn\.jsdelivr\.net/npm/mathjax@3/es5/([\w.-]+\.js)",
        r"../../../site/assets/mathjax/es5/\1",
        html,
    )

    # Make MathJax's equation tags agree with the numbers LaTeX assigned (and
    # that \eqref links already use). See equation_numbering().
    if numbering and NUMBERED_EQ.search(html):
        chapter, offset = numbering
        html = html.replace(
            'MathJax = { tex: { tags: "ams", }, };',
            "MathJax = { tex: { tags: \"ams\", tagformat: { "
            f"number: (n) => `{chapter}.` + (n + {offset}) "
            "} }, };",
        )

    # The page's section heading keys its discussion thread. Use the *numbered*
    # heading ("1.1 Introduction"), not the bare <title>: two sections in this
    # document are both called "Introduction", and without the number they would
    # share a single thread.
    m = re.search(r"class='sectionHead'>(.*?)</h\d>", html, re.S)
    if not m:
        m = re.search(r"<title>(.*?)</title>", html, re.S)
    section_title = (unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(1)))).strip()
                     if m else path.stem)

    nav = page_nav(html)
    body = re.search(r"<body>(.*)</body>", html, re.S)
    if not body:
        return False
    inner = body.group(1)

    shell = (
        '<div class="layout">'
        + sidebar(items, path.name, course_title)
        + '<main class="content"><div class="inner">'
        + inner
        + nav
        # Only section pages get a question box. The title page, the chapter
        # landings and the contents page have no topic to ask about, and an
        # empty thread on each would just look abandoned.
        + (qa_block(discussion_term(course_title, section_title))
           if re.search(r"se\d+$", path.stem) else "")
        + "</div></main></div>"
        + '<button class="sb-toggle" onclick="document.getElementById(\'sidebar\')'
          '.classList.toggle(\'open\')">Contents</button>'
    )
    html = html[: body.start(1)] + MARKER + shell + html[body.end(1):]
    path.write_text(html, encoding="utf-8")
    return True


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    course = Path(sys.argv[1]).resolve()
    build = course / "build"
    if not build.is_dir():
        print(f"no build directory at {build}", file=sys.stderr)
        return 1

    title = course.name.replace("-", " ").title()
    items = read_toc(build)
    if not items:
        print("warning: no contents entries found — sidebar will be empty",
              file=sys.stderr)

    # Must be computed before any page is rewritten: it counts equations in the
    # raw conversion output, in document order.
    eqnums = equation_numbering(build, items)

    pages = sorted(build.glob("*.html"))
    done = sum(process(p, items, title, eqnums.get(p.name)) for p in pages)
    skipped = len(pages) - done
    print(f"processed {done} pages, {len(items)} sidebar entries")
    if skipped:
        print(f"SKIPPED {skipped} already-built page(s). Re-run the conversion "
              f"first — this script must see fresh tex4ht output.", file=sys.stderr)
        return 1

    # Cheap structural check: the conversion output is balanced, so if our
    # rewriting unbalances a page we want to hear about it now, not from a
    # browser quietly repairing the DOM.
    for p in pages:
        t = p.read_text(encoding="utf-8", errors="replace")
        if t.count("<div") != t.count("</div>"):
            print(f"WARNING unbalanced divs in {p.name}: "
                  f"{t.count('<div')} open / {t.count('</div>')} close",
                  file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
