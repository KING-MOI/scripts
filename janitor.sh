#!/bin/bash
find ~/Downloads -name '*.dmg' -mtime +30 -delete
find ~/Downloads -name '*.zip' -mtime +30 -delete
