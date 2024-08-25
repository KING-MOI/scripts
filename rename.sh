#!/bin/bash
DRY=${1:-}
for f in *; do [ -f "$f" ] || continue
  nf=$(echo "$f" | tr ' ' '_')
  [ "$DRY" = "-n" ] && echo "$f -> $nf" || mv "$f" "$nf"; done
