# True narrow-viewport screenshots

Headless Chrome clamps its window to about 500px wide. `--window-size=390,900` therefore
renders the page at ~500px and *crops* it to 390 — which looks exactly like a mobile
overflow bug that isn't there. (This cost real time once already; see the Status Log.)

`m390.html` iframes a page at exactly 390px so the layout genuinely sees a narrow
viewport. Shoot the wrapper, not the page:

    python3 -m http.server 8961
    google-chrome --headless=new --disable-gpu --hide-scrollbars \
      --virtual-time-budget=20000 --window-size=520,1650 \
      --screenshot=/tmp/mobile.png http://127.0.0.1:8961/.viewport/m390.html

Edit the iframe `src` to point at whichever page you want to check.

Give MathJax a generous `--virtual-time-budget`. Cut it short and the maths screenshots
upright and mis-spaced, which reads as a styling bug rather than an unfinished render.


## Checking for horizontal overflow

    python3 -m http.server 8961
    .viewport/check-overflow.sh                       # both courses
    .viewport/check-overflow.sh introduction-to-statistics

Reports anything a reader would have to scroll sideways to see, ignoring the two benign
cases: a display that scrolls inside its own box, and an equation tag set in the right
margin where a book would put it.

**One Chrome run per page, deliberately.** An earlier version loaded every page into
iframes on one wrapper page and shared a single `--virtual-time-budget`. That budget
accelerates *timers*, not CPU — and MathJax typesetting is CPU work — so it dumped its DOM
after three pages and reported the remaining thirty-eight clean. A false pass is worse than
no check at all.

If you change this script, verify it on a negative control before trusting a clean run:
point it at a page with a deliberately over-wide element and confirm it reports the
overflow. A checker that silently measures nothing looks exactly like one that found
nothing.
