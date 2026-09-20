#!/usr/bin/env bash
set -euo pipefail

docs=(README.md OFFER.md PRICING.md PILOT.md)
official_url="https://echocert-evidence.mccombsp86.chatgpt.site"

for file in "${docs[@]}"; do
  test -s "$file"
  grep -Fq "£495" "$file"
  grep -Fq "$official_url" "$file"
done

grep -Fq "paid upfront after written scope approval" OFFER.md
grep -Fq "100 approved non-sensitive files or 2 GB" OFFER.md
grep -Fq "seven business days" OFFER.md
grep -Fq "observed facts, supported inference and unresolved or unproven claims" OFFER.md

for retired_claim in \
  "£250 upfront" \
  "£245" \
  "£299/year" \
  "£999/year" \
  "£0 for 2" \
  "no licence fee" \
  "2–4 weeks" \
  "delivery within five business days"; do
  if grep -Fq "$retired_claim" "${docs[@]}"; then
    echo "RETIRED COMMERCIAL CLAIM FOUND: $retired_claim" >&2
    exit 1
  fi
done

echo "COMMERCIAL DOCS CONSISTENCY PASSED"
