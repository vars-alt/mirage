# Mirage 🌫️

**Adversarial evasion** against ML intrusion detectors. Mirage takes real malicious traffic and nudges only the features an attacker actually controls — request rate, payload entropy, latency — just far enough to flip the model's verdict to *benign*.

> Project **[2]** in a portfolio on adversarial ML & AI security. Mirage is the attacker in the arms race: it breaks [Sentinel](https://github.com/vars-alt/sentinel), which motivates [Aegis](https://github.com/vars-alt/aegis) to defend it. Maps to **MITRE ATLAS AML.T0015 (Evade ML Model)**.

---

## Result

Against a gradient-boosted detector that catches **100%** of raw attacks:

| | Detected |
|---|---|
| Before evasion | 893 / 893 (**100%**) |
| After evasion | **0** / 893 |
| **Evasion success** | **100%** |

The attack is **black-box**: it never reads the model's internals, only its yes/no answers — the realistic threat model for a deployed detector behind an API.

## Quickstart

```bash
pip install -r requirements.txt
make run
```

## How it works

For each attack sample, Mirage checks the detector's output and, while it's still flagged, steps the attacker-controllable features toward the benign region — the smallest nudge that evades. Immutable signals are left alone, so the "attack" stays an attack.

- `mirage/attack.py` — the evasion loop (budgeted, black-box)
- `mirage/data.py` — Range-compatible traffic
- `run.py` — trains a victim detector and reports the collapse

## Why it matters

A model's test-set accuracy says nothing about its robustness to an adversary who adapts. Mirage makes that concrete — and hands the problem to Aegis.

## ⚠️ Ethics

Research code for evaluating detectors **you own**. Published for defensive study.

## License

MIT — see [LICENSE](LICENSE).
