#!/bin/bash
F=~/todo.txt
[ -f $F ] || touch $F
case $1 in
  add) echo "$2" >> $F ;;
  ls) cat -n $F ;;
  done) sed -i '' "$2d" $F ;;
  edit) ${EDITOR:-vi} $F ;;
  clear) > $F ;;
esac
