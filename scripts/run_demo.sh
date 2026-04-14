#!/usr/bin/env bash
set -euo pipefail

python scripts/build_bundle.py
python scripts/validate_contract.py

echo "Done. See output/ for generated files."
