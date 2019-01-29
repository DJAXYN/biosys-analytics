#!/usr/bin/env bash

FILE=$1
CLINE=${2:-3}
i=0
if [[ $# -eq 0 ]]; then
  echo "Usage: FILE [COUNT]"
  exit 1
fi

if [[ ! -f "$FILE" ]]; then
  echo "$FILE is not a file"
  exit 2

fi

while read -r LINE; do
  let i++
  echo "$LINE"
  if [[ $i -eq $CLINE ]]; then
    break
  fi
done < "$FILE"
