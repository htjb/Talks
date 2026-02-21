#!/bin/bash
# Run once after cloning to enable the pre-commit hook that auto-generates README.md.
git config core.hooksPath .githooks
echo "Git hooks configured. README.md will be regenerated automatically on each commit."
