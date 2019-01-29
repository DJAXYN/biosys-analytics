#!/usr/bin/env bash

FILE=$1
i=0
if [[ $# -eq 0 ]]; then
  echo "Usage: cat-n.sh FILE"
  exit 1
fi

if [[ ! -f "$FILE" ]]; then
  echo "$FILE is not a file"
  exit 2

else
  while read -r LINE; do
    let i++
    echo "$i $LINE"

  done < "$FILE"

fi
