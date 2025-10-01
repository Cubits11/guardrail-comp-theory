#!/usr/bin/env bash
set -euo pipefail

# 1) Python – create and activate venv
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

# 2) Upgrade pip/setuptools/wheel
python -m pip install --upgrade pip setuptools wheel

# 3) Install deps (requirements first for Codex; then editable for our package extras)
pip install -r requirements.txt
pip install -e .[dev] || pip install -e .

# 4) Quick sanity: print versions
python - << 'PY'
import sys, numpy, sklearn
print("Python:", sys.version.split()[0])
print("NumPy:", numpy.__version__)
print("Sklearn:", sklearn.__version__)
PY

# 5) Run tests (fast)
pytest -q
