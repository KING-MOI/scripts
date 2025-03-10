#!/bin/bash
DRY=${1:-}
run() { [ "$DRY" = "-n" ] && echo "$@" || eval "$@"; }
run 'find ~/Downloads -name "*.dmg" -mtime +30 -delete'
run 'find ~/Downloads -name "*.zip" -mtime +30 -delete'
run 'find ~/Desktop -name "Screenshot*" -mtime +14 -delete'
