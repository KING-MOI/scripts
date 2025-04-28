#!/bin/bash
rsync -av --exclude node_modules --exclude .cache ~/Documents /Volumes/backup/
