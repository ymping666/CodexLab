# Offline toy experiment

Run from the repository root with Python 3.11 or newer:

```console
python examples/toy_regression.py --output examples/output/toy-regression
```

The standard-library script generates independent training and test samples for five fixed seeds, fits a constant mean baseline and ordinary least squares, and measures held-out mean squared error. There are no dependencies, downloads, API calls, model sessions, or tuning. Results are genuinely computed from the script; the problem intentionally matches the treatment's assumptions and demonstrates reproducible artifact plumbing only.

`summary.json` preserves per-seed measurements, source/data hashes, environment, and descriptive paired differences. `runs.jsonl` references that raw file. Repeating the command in the same Python environment produces the same numeric measurements. Platform/environment strings can differ between machines. A null effect or a worse treatment would remain in the raw records.

The first local run on Python 3.14.7 produced a baseline mean MSE of **1.339995** and treatment mean MSE of **0.067533**, with positive paired differences in all five seeds. These are measured toy values for this constructed data generator, not paper results or a benchmark advantage.

This script does not test native Codex multi-agent execution, establish a novel method, or validate a paper claim. It is a small runnable example of the experiment specialist's evidence contract. A real project must replace the synthetic task with a justified dataset and strong domain baselines.
