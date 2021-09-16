#!/bin/bash
set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "Pushing modified and new PDF documents…"
rclone copy --progress --update --fast-list --size-only --include 'source.pdf' `dirname "$SCRIPT_DIR"` echemdb-private-crypt:
echo "Ok. Documents have been uploaded."
