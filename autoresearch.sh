#!/usr/bin/env bash
set -euo pipefail

# Compile any modified Java classes into build/
mkdir -p build
javac -encoding ISO-8859-1 -cp lib/spmf.jar -d build src_spmf/ca/pfv/spmf/algorithms/frequentpatterns/efim/*.java

# Canonical benchmark entrypoint for HUPM research
python benchmark.py
