#!/usr/bin/env bash
set -euo pipefail

# Canonical benchmark entrypoint for HUPM research
# Runs deterministic comparison of EFIM and HUI-Miner on transaction datasets
python benchmark.py
