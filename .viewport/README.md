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
