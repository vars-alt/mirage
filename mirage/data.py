#!/usr/bin/env python3
"""Range-compatible traffic generator (shared schema with Sentinel)."""
from __future__ import annotations
import numpy as np

FEATURES = ["status", "bytes_in", "latency_ms", "requests_last_10s",
            "distinct_paths_last_60s", "payload_entropy"]

def sample(n: int, seed: int):
    rng = np.random.default_rng(seed)
    X, y = [], []
    for _ in range(n):
        mal = rng.random() < 0.3
        if mal:
            row = [rng.choice([200, 404, 500]), rng.integers(0, 50_000),
                   rng.normal(90, 40), rng.integers(20, 200),
                   rng.integers(1, 14), rng.uniform(5.5, 8.0)]
        else:
            row = [200, rng.integers(0, 60_000), rng.normal(40, 12),
                   rng.integers(1, 6), rng.integers(1, 3), rng.uniform(3.5, 5.0)]
        X.append([float(v) for v in row]); y.append(int(mal))
    return np.array(X), np.array(y)
