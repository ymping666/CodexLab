"""Offline workflow demonstration; synthetic results are not research validation."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import random
import shlex
import statistics
import subprocess
import sys
from pathlib import Path


def dataset(rng: random.Random, count: int) -> list[tuple[float, float]]:
    return [(x, 2.0 * x + 0.5 + rng.gauss(0.0, 0.25))
            for x in (rng.uniform(-1.0, 1.0) for _ in range(count))]


def run(seed: int) -> dict:
    rng = random.Random(seed)
    train = dataset(rng, 80)
    test = dataset(rng, 80)
    mean_x = statistics.mean(x for x, _ in train)
    mean_y = statistics.mean(y for _, y in train)
    slope = (sum((x - mean_x) * (y - mean_y) for x, y in train)
             / sum((x - mean_x) ** 2 for x, _ in train))
    intercept = mean_y - slope * mean_x
    baseline = statistics.mean((y - mean_y) ** 2 for _, y in test)
    treatment = statistics.mean((y - (slope * x + intercept)) ** 2 for x, y in test)
    data_hash = hashlib.sha256(json.dumps([train, test]).encode()).hexdigest()
    return {"seed": seed, "baseline_mse": baseline, "treatment_mse": treatment,
            "paired_improvement": baseline - treatment, "slope": slope,
            "intercept": intercept, "data_sha256": data_hash}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("examples/output/toy-regression"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    seeds = [11, 23, 37, 51, 71]
    rows = [run(seed) for seed in seeds]
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    summary = {
        "label": "TOY SYNTHETIC DEMONSTRATION — not a scientific contribution",
        "hypothesis": "OLS outperforms a training-mean predictor on known linear synthetic data.",
        "protocol": {"train_samples": 80, "test_samples": 80, "seeds": seeds,
                     "baseline": "training target mean", "treatment": "ordinary least squares",
                     "primary_metric": "held-out MSE", "tuning": "none",
                     "data_generator": "y = 2*x + 0.5 + Normal(0, 0.25); x ~ Uniform(-1,1)"},
        "environment": {"python": platform.python_version(), "platform": platform.platform()},
        "code_sha256": code_hash,
        "observed": {
            "baseline_mean_mse": statistics.mean(row["baseline_mse"] for row in rows),
            "treatment_mean_mse": statistics.mean(row["treatment_mse"] for row in rows),
            "paired_mean_improvement": statistics.mean(row["paired_improvement"] for row in rows),
            "paired_min_improvement": min(row["paired_improvement"] for row in rows),
            "paired_max_improvement": max(row["paired_improvement"] for row in rows),
            "improved_seed_count": sum(row["paired_improvement"] > 0 for row in rows)},
        "runs": rows,
        "limits": ["Designed linear toy problem favors OLS; this is a plumbing smoke test.",
                   "Seed variation is descriptive; no confidence interval or population claim.",
                   "No external dataset, model inference, or native subagent invocation occurs."]}
    raw_path = args.output / "summary.json"
    raw_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    command_args = ["python", *sys.argv]
    command = (subprocess.list2cmdline(command_args) if sys.platform == "win32"
               else shlex.join(command_args))
    with (args.output / "runs.jsonl").open("w", encoding="utf-8") as stream:
        for row in rows:
            record = {"run_id": f"toy-seed-{row['seed']}", "command": command,
                      "seed": row["seed"], "status": "completed",
                      "metrics": {name: row[name] for name in
                                  ("baseline_mse", "treatment_mse", "paired_improvement")},
                      "artifact_path": "summary.json", "code_sha256": code_hash,
                      "data_sha256": row["data_sha256"]}
            stream.write(json.dumps(record) + "\n")
    print(json.dumps({"output": str(raw_path), "label": summary["label"],
                      "observed": summary["observed"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
