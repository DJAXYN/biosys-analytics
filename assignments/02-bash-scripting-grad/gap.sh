#!/usr/bin/env bash

LETTERS=$1
DIR=~/BE534/biosys-analytics/data/gapminder
echo $DIR


if [[ $# -ne 1 ]]; then
  for FILE in $DIR/*; do
    BASENAME=$(basename "$FILE")
      echo "${BASENAME%%.*}"
  done
fi
if [[ $# -eq 1 ]]; then
  for FILE in $DIR/*; do
    LIST_OF_COUNTRIES=$(grep -li ^$LETTERS "$FILE")
    BASENAME=$(basename "$LIST_OF_COUNTRIES")
    echo "${BASENAME%%.*}"
  done
fi
