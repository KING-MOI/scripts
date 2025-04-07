#!/bin/bash
for d in ~/dev/*/; do
  (cd $d || continue
  [ -n "$(git status --porcelain)" ] && continue
  git pull -q && git push -q) &
done
wait
