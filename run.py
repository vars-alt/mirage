#!/usr/bin/env python3
"""
Train a victim detector on standard traffic, confirm it catches attacks, then
let Mirage evade it and report the collapse in detection.

    python run.py
"""
from __future__ import annotations
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import recall_score

from mirage.data import sample
from mirage.attack import evade

def main():
    Xtr, ytr = sample(6000, seed=0)
    victim = GradientBoostingClassifier(random_state=0).fit(Xtr, ytr)

    Xte, yte = sample(3000, seed=42)
    base_recall = recall_score(yte, victim.predict(Xte))

    X_mal = Xte[yte == 1]
    detected_before = int((victim.predict(X_mal) == 1).sum())
    _, evaded = evade(victim, X_mal)
    detected_after = len(X_mal) - evaded

    print("Mirage — black-box evasion vs a GradientBoosting detector\n" + "-"*56)
    print(f"malicious samples:           {len(X_mal)}")
    print(f"detected before evasion:     {detected_before}  ({base_recall:.1%} recall)")
    print(f"detected after evasion:      {detected_after}")
    print(f"evasion success rate:        {evaded/len(X_mal):.1%}")
    print("-"*56)
    print("The detector's recall is an illusion once the attacker adapts.")
    print("Aegis (adversarial training) is the countermeasure.")

if __name__ == "__main__":
    main()
