#!/bin/bash
for f in *; do [ -f "$f" ] && mv "$f" "$(echo "$f" | tr ' ' '_')"; done
