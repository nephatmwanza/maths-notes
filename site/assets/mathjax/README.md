# Vendored MathJax 3.2.2

Not written here — this is [MathJax](https://www.mathjax.org/) v3.2.2, Apache-2.0
(see `LICENSE`), copied unmodified from the npm tarball:

    curl -sL https://registry.npmjs.org/mathjax/-/mathjax-3.2.2.tgz | \
      tar xz --strip-components=1 \
        package/es5/tex-chtml-full.js \
        package/es5/output/chtml/fonts/woff-v2 \
        package/LICENSE

## Why it is vendored rather than loaded from a CDN

tex4ht hardcodes `cdn.jsdelivr.net` into every generated page. That makes each reader wait
on ~1MB of third-party JavaScript and fonts before a single formula is legible; until it
lands, the maths renders upright and mis-spaced. For students on slow or metered mobile
data — the audience for this site — that is the normal experience, not an edge case.

Served from this origin it caches with the rest of the site and works offline after the
first visit. `site/build.py` rewrites the CDN URL during the build; nothing else changes.

Only `tex-chtml-full.js` and the woff-v2 fonts are kept (1.7MB), not the full 6MB package.
