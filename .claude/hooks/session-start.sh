#!/bin/bash
set -euo pipefail

chmod +x "$CLAUDE_PROJECT_DIR/.githooks/commit-msg"
git -C "$CLAUDE_PROJECT_DIR" config core.hooksPath .githooks

echo "Conventional Commits enforcement enabled (core.hooksPath -> .githooks)"
