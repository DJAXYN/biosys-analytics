#!/usr/bin/env bash


GREETING=$1
NAME=${2:-Human}

set -u
if [[ $# -eq 0 ]]; then
  echo "Usage: GREETING [NAME]"
  exit 1
fi

if [[ $# -gt 2 ]]; then
  echo "Usage: GREETING [NAME]"
  exit 2
fi

if [[ $# -eq 1 ]]; then
  echo "$GREETING, $NAME!"
fi

if [[ $# -eq 2 ]]; then
  echo "$GREETING, $NAME!"
fi
