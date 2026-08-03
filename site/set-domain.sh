#!/usr/bin/env bash
# Point the site at a custom domain.
#
#   site/set-domain.sh wjmaths.com            # show what would happen
#   site/set-domain.sh wjmaths.com --confirm  # actually do it
#
# Writes the CNAME file GitHub Pages reads, commits and pushes. The workflow
# uploads the repository root as the Pages artifact, so a root CNAME is picked
# up with no other change.
#
# Committing CNAME also SETS the domain in Settings -> Pages. Do not type it
# into that box as well: if the two ever disagree, whichever was written last
# wins and the other silently reverts on the next deploy.
#
# --confirm is required because this script publishes, and publishing a domain
# nobody owns takes the site OFF the air: Pages stops answering on the
# github.io address and starts answering on a name that does not resolve.
# That happened once, while testing this script with a real argument. A script
# whose dry run is its live run is a trap, so the default is now dry.

set -euo pipefail

domain="${1:?usage: site/set-domain.sh <domain> [--confirm]   e.g. site/set-domain.sh wjmaths.com}"
confirm="${2:-}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Hostnames are case-insensitive but GitHub wants the CNAME lowercase. Someone
# typing WJMaths.com has not made a mistake, so fold it rather than refuse it.
# Strip a trailing dot too - valid in DNS, rejected by Pages.
domain="$(printf '%s' "$domain" | tr '[:upper:]' '[:lower:]' | sed 's/\.$//')"

# A bare hostname only - no scheme, no path, no trailing dot. GitHub rejects
# anything else, and the failure shows up as a deploy error rather than a
# useful message.
if [[ ! "$domain" =~ ^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$ ]]; then
  echo "error: '$domain' is not a bare hostname (expected e.g. wjmaths.com)" >&2
  exit 1
fi

cd "$root"

if [[ "$confirm" != "--confirm" ]]; then
  cat <<EOF
DRY RUN - nothing written, nothing pushed.

Would write CNAME containing:  $domain
Would commit and push to:      $(git rev-parse --abbrev-ref HEAD)

Do this only once the domain is registered and you own it. Re-run with:

  site/set-domain.sh $domain --confirm
EOF
  exit 0
fi

printf '%s\n' "$domain" > CNAME
git add CNAME
git commit -q -m "Serve the site from $domain

CNAME at the repository root, which is what the Pages workflow uploads.
Every internal path is relative and the giscus thread keys are tied to
course directory and section title rather than URL, so nothing else needs
to change and no discussion is orphaned by the move."
git push -q origin main

cat <<EOF

CNAME written and pushed: $domain

Now set these at the registrar (Porkbun: Details -> DNS Records).

  DELETE the default records Porkbun creates first. It adds an A record and an
  ALIAS/CNAME pointing at its own parking page, and they will fight the records
  below - the symptom is a site that works for some visitors and not others.

  Type   Host    Answer
  ----   ----    ------------------------
  A      (blank) 185.199.108.153
  A      (blank) 185.199.109.153
  A      (blank) 185.199.110.153
  A      (blank) 185.199.111.153
  CNAME  www     nephatmwanza.github.io

Then wait for DNS, and turn on "Enforce HTTPS" in Settings -> Pages once the
box stops being greyed out. That can take up to an hour after DNS resolves;
it is not broken.

Check propagation with:
  dig +short $domain
  dig +short www.$domain
EOF
