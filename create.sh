#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "usage: ./create.sh <problem_number> <problem_title>" >&2
  echo "example: ./create.sh 42 Trapping Rain Water" >&2
  exit 1
fi

number="$1"
shift
title="$*"

if ! [[ "$number" =~ ^[0-9]+$ ]]; then
  echo "error: problem_number must be numeric" >&2
  exit 1
fi

slug="$(printf '%s' "$title" \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[^a-z0-9]+/_/g; s/^_+//; s/_+$//; s/_+/_/g')"

if [ -z "$slug" ]; then
  echo "error: problem_title must contain letters or numbers" >&2
  exit 1
fi

dir="$(printf '%04d_%s' "$number" "$slug")"

mkdir -p "$dir"
touch "$dir/solution.py"
echo "# $number. $title" > "$dir/description.md"

printf 'created %s\n' "$dir"