#!/bin/bash
rsync -av --exclude node_modules --exclude .cache --exclude target ~/Documents /Volumes/backup/
