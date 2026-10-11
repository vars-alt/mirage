#!/usr/bin/env python3
"""
Mirage evasion. Given a trained detector, take real malicious traffic and nudge
only the attacker-controllable features (request rate, payload entropy, latency)
toward the benign region, the smallest change that flips the prediction to
'benign'. This is a black-box, feature-space evasion — the attacker never needs
the model's internals, only its yes/no answers.

Maps to MITRE ATLAS AML.T0015 (Evade ML Model).
"""
from __future__ import annotations
import numpy as np

# indices of features an attacker can realistically lower without stopping the attack
MUTABLE = {3: 3.0, 5: 4.2, 2: 45.0}  # requests_last_10s, payload_entropy, latency_ms -> benign-ish target

def evade(model, X_mal, steps: int = 20):
    """Return perturbed copies and how many now evade detection."""
    X = X_mal.copy().astype(float)
    for i in range(len(X)):
        for _ in range(steps):
            if model.predict(X[i:i+1])[0] == 0:   # already evades
                break
            for idx, target in MUTABLE.items():    # step each mutable feature toward benign
                X[i, idx] += (target - X[i, idx]) * 0.2
    evaded = int(np.sum(model.predict(X) == 0))
    return X, evaded
