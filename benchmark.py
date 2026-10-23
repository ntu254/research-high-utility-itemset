#!/usr/bin/env python3
"""
High Utility Pattern Mining Benchmark Harness
Compares EFIM vs HUI-Miner on standard and retail transaction datasets.
Measures execution time, memory usage, and verifies output equivalence.
"""

import os
import sys
import subprocess
import re
import tempfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
JAR_PATH = BASE_DIR / "lib" / "spmf.jar"

BENCHMARK_CONFIGS = [
    {
        "name": "foodmart",
        "dataset": BASE_DIR / "data" / "foodmart.txt",
        "min_utility": 10000,
    },
    {
        "name": "ecommerce",
        "dataset": BASE_DIR / "data" / "ecommerce_dense.txt",
        "min_utility": 1200000,
    },
]


def run_spmf(algorithm: str, dataset_path: Path, output_path: Path, min_util: int):
    cp = f"build{os.pathsep}{JAR_PATH}"
    cmd = [
        "java",
        "-XX:+UseG1GC",
        "-Xms256m",
        "-Xmx2g",
        "-XX:CICompilerCount=2",
        "-XX:+AlwaysPreTouch",
        "-cp",
        cp,
        "ca.pfv.spmf.gui.Main",
        "run",
        algorithm,
        str(dataset_path),
        str(output_path),
        str(min_util),
    ]
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if proc.returncode != 0:
        print(f"Error running {algorithm} on {dataset_path}:", file=sys.stderr)
        print(proc.stderr, file=sys.stderr)
        sys.exit(1)

    stdout = proc.stdout

    # Parse time
    time_match = re.search(r"Total time ~:?\s*(\d+)\s*ms", stdout)
    exec_time = int(time_match.group(1)) if time_match else 0

    # Parse memory
    mem_match = re.search(r"(?:Max memory:|Memory ~)\s*([\d\.]+)", stdout)
    memory = float(mem_match.group(1)) if mem_match else 0.0

    # Parse count
    count_match = re.search(r"High-?utility itemsets count\s*:?\s*(\d+)", stdout)
    count = int(count_match.group(1)) if count_match else 0

    return {
        "time_ms": exec_time,
        "memory_mb": memory,
        "hui_count": count,
    }


def load_itemsets(file_path: Path):
    itemsets = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(" #UTIL: ")
            if len(parts) == 2:
                items = tuple(sorted(map(int, parts[0].split())))
                util = int(parts[1])
                itemsets[items] = util
    return itemsets


def main():
    if not JAR_PATH.exists():
        print(f"Error: JAR not found at {JAR_PATH}", file=sys.stderr)
        sys.exit(1)

    total_efim_time = 0
    total_huiminer_time = 0
    max_efim_memory = 0.0
    max_huiminer_memory = 0.0
    total_hui_count = 0

    temp_dir = Path(tempfile.mkdtemp(prefix="hupm_bench_"))

    try:
        for cfg in BENCHMARK_CONFIGS:
            name = cfg["name"]
            dataset = cfg["dataset"]
            min_u = cfg["min_utility"]

            if not dataset.exists():
                print(f"Error: Dataset {dataset} missing!", file=sys.stderr)
                sys.exit(1)

            out_efim = temp_dir / f"{name}_efim.txt"
            out_hui = temp_dir / f"{name}_hui.txt"

            res_efim = run_spmf("EFIM", dataset, out_efim, min_u)
            res_hui = run_spmf("HUI-Miner", dataset, out_hui, min_u)

            # Verification: result sets must be identical
            set_efim = load_itemsets(out_efim)
            set_hui = load_itemsets(out_hui)

            if set_efim != set_hui:
                print(
                    f"Correctness validation FAILED for {name}! "
                    f"EFIM count: {len(set_efim)}, HUI-Miner count: {len(set_hui)}",
                    file=sys.stderr,
                )
                sys.exit(1)

            total_efim_time += res_efim["time_ms"]
            total_huiminer_time += res_hui["time_ms"]
            max_efim_memory = max(max_efim_memory, res_efim["memory_mb"])
            max_huiminer_memory = max(max_huiminer_memory, res_hui["memory_mb"])
            total_hui_count += len(set_efim)

            print(
                f"[{name.upper()}] EFIM: {res_efim['time_ms']}ms / {res_efim['memory_mb']:.1f}MB | "
                f"HUI-Miner: {res_hui['time_ms']}ms / {res_hui['memory_mb']:.1f}MB | "
                f"HUIs: {len(set_efim)}"
            )

        speedup = (
            total_huiminer_time / total_efim_time if total_efim_time > 0 else 1.0
        )

        # Output canonical metrics
        print(f"METRIC efim_exec_time_ms={total_efim_time}")
        print(f"METRIC huiminer_exec_time_ms={total_huiminer_time}")
        print(f"METRIC efim_memory_mb={round(max_efim_memory, 2)}")
        print(f"METRIC huiminer_memory_mb={round(max_huiminer_memory, 2)}")
        print(f"METRIC hui_count={total_hui_count}")
        print(f"METRIC speedup_ratio={round(speedup, 3)}")

    finally:
        # Cleanup temp directory
        for p in temp_dir.glob("*"):
            try:
                p.unlink()
            except Exception:
                pass
        try:
            temp_dir.rmdir()
        except Exception:
            pass


if __name__ == "__main__":
    main()
