#!/usr/bin/env bash
# Report anything a reader would have to scroll sideways to see.
# Usage: .viewport/check-overflow.sh [course-name]
set -uo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
port=8961; filter="${1:-}"
curl -s -o /dev/null "http://127.0.0.1:$port/" || { echo "start: python3 -m http.server $port" >&2; exit 1; }
total=0; bad=0
for dir in "$root"/courses/*/build; do
  course=$(basename "$(dirname "$dir")")
  [ -n "$filter" ] && [ "$course" != "$filter" ] && continue
  for f in "$dir"/*.html; do
    rel="courses/$course/build/$(basename "$f")"
    total=$((total+1))
    res=$(timeout 60 google-chrome --headless=new --disable-gpu --no-sandbox \
            --virtual-time-budget=25000 --window-size=1500,1300 \
            --dump-dom "http://127.0.0.1:$port/.viewport/measure.html?u=/$rel" 2>/dev/null \
          | sed -n 's|.*<pre id="out">\(.*\)</pre>.*|\1|p' | head -20)
    if [ -n "$res" ] && [ "$res" != "OK" ] && [ "$res" != "pending" ]; then
      bad=$((bad+1)); echo "  $rel"; echo "$res" | sed 's/^/      /'
    fi
  done
done
echo "checked $total pages; $bad with overflow"
