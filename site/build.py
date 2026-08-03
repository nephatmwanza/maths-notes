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
from html import escape, unescape
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


# Both courses now write every worked example as a real LaTeX environment -
# \begin{example}, \begin{solution}, \begin{definition} and so on - so tex4ht
# emits proper theorem markup and tag_theorems() styles and numbers it.
#
# It used to be otherwise. The statistics notes marked examples with a bold word,
# \textbf{Example}, and this file gave those paragraphs a class so the stylesheet
# could fake a label and a number. That worked until it silently did not: a marker
# only becomes its own paragraph if a BLANK LINE precedes it, so after `\\` it
# stayed inline, matched nothing, and lost its label, its rule and its number
# while every other example on the page kept theirs. Nine markers were affected.
#
# The lesson is that a presentational convention enforced by a regex over
# generated HTML has no way to fail loudly. An environment does: unbalanced
# \begin/\end stops the build. So the markers were converted rather than
# patched, and what remains here is only the check that they stay converted.
MARKER_WORDS = ("Example", "Examples", "Solution", "Exercise", "Note", "Remark",
                "Definition", "Theorem", "Proof")

BOLD_MARKER_RE = re.compile(
    r"<span class='cm(?:bx|ti)[^']*'>\s*"
    r"(" + "|".join(MARKER_WORDS) + r")\s*:?\s*</span>"
)


def report_stray_markers(html: str, page: str) -> int:
    """Warn about an Example/Solution heading not written as an environment.

    Ignores headings emitted by a real LaTeX environment - `\\begin{solution}`
    and friends render inside `<span class='head'>`, which tag_theorems() has
    already styled and numbered. Anything else matching a marker word is a bold
    paragraph pretending to be a heading: unnumbered, unstyled, and invisible to
    the counter, so every later example on that page is misnumbered too.
    """
    strays = []
    for m in BOLD_MARKER_RE.finditer(html):
        # Anchor to the enclosing paragraph rather than guessing a window size:
        # tex4ht pads its output with runs of whitespace hundreds of characters
        # long, so a fixed lookback silently misses the `head` span it is meant
        # to find and reports every environment heading as a defect.
        para = html.rfind("<p", 0, m.start())
        before = html[para:m.start()] if para != -1 else html[:m.start()]
        if "class='head'" in before:
            continue
        # `(Exercise)` and the like are deliberate inline labels, not headings.
        if before.rstrip().endswith("("):
            continue
        strays.append(m.group(1))
    for word in strays:
        print(f"    WARNING {page}: bold '{word}' is not an environment, so it "
              f"gets no label or number. Use \\begin{{{word.lower().rstrip('s')}}} "
              f"... \\end{{{word.lower().rstrip('s')}}} in the .tex.")
    return len(strays)


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


def slug(s: str) -> str:
    s = unescape(re.sub(r"<[^>]+>", " ", s)).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"^-+|-+$", "", s)[:70]


def discussion_term(course_slug: str, section_title: str) -> str:
    """A stable, readable key for the discussion thread behind a page.

    giscus offers `pathname` or a page-stem term. Both are fragile here:
    inserting one section renumbers every page after it, so `intro_probse4`
    silently becomes a different topic and its thread orphans. A slug built
    from the section's own title survives insertions, and it also means the
    Discussions tab lists something legible - "counting-techniques" rather than
    "intro_probse5" - so it is possible to see at a glance which topics readers
    are actually stuck on.

    The course half of the key is the *directory* name, deliberately not the
    display title. Display titles get reworded, and if the key tracked the
    wording then every thread on a course would orphan the moment someone
    improved its title. The directory name is the one identifier nobody edits
    for cosmetic reasons.
    """
    return f"{course_slug}/{slug(section_title)}"


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


def process(path: Path, items: list[dict], course_title: str, course_slug: str,
            numbering: tuple[int, int] | None = None) -> bool:
    html = path.read_text(encoding="utf-8", errors="replace")

    # Not idempotent: a second pass would nest another layout shell and a second
    # sidebar inside the first. Always run this on fresh conversion output.
    if MARKER in html:
        return False

    html = tag_theorems(html)
    report_stray_markers(html, path.name)
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

    # The page's own heading keys its discussion thread. Use the *numbered*
    # heading ("1.1 Introduction"), not the bare <title>: two sections in this
    # document are both called "Introduction", and without the number they would
    # share a single thread.
    #
    # Subsection heads count, not just section heads. Where a course splits at
    # subsection level the subsection page *is* the content page, and keying it
    # off <title> would have collapsed every "Introduction" in the course onto
    # one thread. Section pages are unaffected: a section head always precedes
    # its own subsections, so re.search still finds it first and the keys minted
    # before this change keep pointing at the same threads.
    m = re.search(r"class='(?:sub){0,2}sectionHead'>(.*?)</h\d>", html, re.S)
    if not m:
        m = re.search(r"<title>(.*?)</title>", html, re.S)
    section_title = (unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(1)))).strip()
                     if m else path.stem)

    # tex4ht leaves <title> empty on the title page and, on every other page,
    # fills it with the bare section name. Both are poor: a browser tab reading
    # "Introduction" says nothing about which course it belongs to, several
    # sections across the site share that name, and the landing page - the one
    # the catalogue links to - had no title at all, so it showed as untitled in
    # tabs, bookmarks and search results.
    #
    # Whether a page gets a heading in its title is decided by whether it *has*
    # a heading, not by its filename. A filename test would have to enumerate
    # tex4ht's stem conventions (se, su, li, ch, ...) and would silently
    # mistreat any it did not know about.
    #
    # Match every heading class tex4ht emits, not just sectionHead. The six in
    # use across these courses are chapterHead, sectionHead, subsectionHead,
    # subsubsectionHead and the "like" variants of the first two - and the
    # subsection pages are the bulk of the site, so matching only sectionHead
    # left 99 of 139 pages titled with the bare course name.
    head = re.search(r"class='(?:like)?(?:chapter|(?:sub){0,2}section)Head'>(.*?)</h\d>",
                     html, re.S)
    heading = (unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", head.group(1)))).strip()
               if head else "")
    page_title = escape(f"{heading} — {course_title}" if heading else course_title)
    html = re.sub(r"<title>.*?</title>", f"<title>{page_title}</title>",
                  html, count=1, flags=re.S)

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
        # A page gets a question box if it has a topic to ask about - that is,
        # if it carries a section or subsection heading of its own. The title
        # page, the chapter landings and the contents page do not, and an empty
        # thread on each would just look abandoned.
        #
        # This used to test the filename for tex4ht's "se" stem, which quietly
        # assumed every course splits at section level. Two of them do not:
        # Foundation Maths and Introduction to Statistics use \section for what
        # a reader calls a chapter, so their real content pages carry the "su"
        # stem and 97 of 117 of them were shipping with nowhere to ask a
        # question - exactly the pages a learner is stuck on. Asking what the
        # page contains rather than what it is called cannot drift that way
        # again when a course is structured differently.
        + (qa_block(discussion_term(course_slug, section_title))
           if re.search(r"class='(?:sub){0,2}sectionHead'", html) else "")
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

    # Display title. Derived from the directory name only as a fallback:
    # .title() mangles real titles - it produced "Introduction To Probability"
    # and, after the course directory was renamed, "Foundation Maths Social
    # Sciences". A one-line title.txt in the course directory overrides it.
    title_file = course / "title.txt"
    title = (title_file.read_text(encoding="utf-8").strip() if title_file.is_file()
             else course.name.replace("-", " ").title())
    items = read_toc(build)
    if not items:
        print("warning: no contents entries found — sidebar will be empty",
              file=sys.stderr)

    # Must be computed before any page is rewritten: it counts equations in the
    # raw conversion output, in document order.
    eqnums = equation_numbering(build, items)

    pages = sorted(build.glob("*.html"))
    done = sum(process(p, items, title, course.name, eqnums.get(p.name))
               for p in pages)
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
