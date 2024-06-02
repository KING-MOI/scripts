#!/bin/bash
for d in ~/dev/*/; do (cd $d && git pull -q && git push -q); done
