#!/bin/bash
for f in *.jpg; do mv "$f" "$(echo $f | tr ' ' '_')"; done
