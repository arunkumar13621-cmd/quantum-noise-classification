"""
Small demo: how three single-qubit noise models show up under different
preparation/measurement settings. Uses Qiskit Aer.

Run:  python quantum_noise_demo.py
"""
import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import (NoiseModel, depolarizing_error,
                              amplitude_damping_error, phase_damping_error)

STRENGTH = 0.2      # error probability for every noise model
SHOTS = 8192
SEED = 7

def noise_model(kind):
    if kind == "None":
        return None
    err = {
        "Depolarizing": depolarizing_error(STRENGTH, 1),
        "Amplitude damping": amplitude_damping_error(STRENGTH),
        "Phase damping": phase_damping_error(STRENGTH),
    }[kind]
    nm = NoiseModel()
    nm.add_all_qubit_quantum_error(err, ["id"])   # noise only on the idle gate
    return nm

def run(circuit, kind):
    sim = AerSimulator(noise_model=noise_model(kind), seed_simulator=SEED)
    tc = transpile(circuit, sim, optimization_level=0)   # keep the id gate
    counts = sim.run(tc, shots=SHOTS).result().get_counts()
    return counts

# Setting A: prepare |1>, idle, measure in Z basis. Ideal result is always "1".
a = QuantumCircuit(1, 1)
a.x(0); a.id(0); a.measure(0, 0)

# Setting B: prepare |+>, idle, rotate back with H, measure (X basis). Ideal result is always "0".
b = QuantumCircuit(1, 1)
b.h(0); b.id(0); b.h(0); b.measure(0, 0)

kinds = ["None", "Depolarizing", "Amplitude damping", "Phase damping"]
res_a, res_b = {}, {}
for k in kinds:
    res_a[k] = run(a, k).get("0", 0) / SHOTS      # fraction of unexpected 0s
    res_b[k] = run(b, k).get("1", 0) / SHOTS      # fraction of unexpected 1s

print("Setting A (|1>, Z basis) - fraction of wrong outcomes")
for k in kinds: print(f"  {k:18s} {res_a[k]:.3f}")
print("Setting B (|+>, X basis) - fraction of wrong outcomes")
for k in kinds: print(f"  {k:18s} {res_b[k]:.3f}")

fig, axes = plt.subplots(1, 2, figsize=(7.5, 2.8), sharey=True)
colors = ["#999999", "#4C72B0", "#DD8452", "#55A868"]
for ax, res, title in zip(axes, (res_a, res_b),
        ["A: prepare |1>, measure Z", "B: prepare |+>, measure X"]):
    ax.bar(kinds, [res[k] for k in kinds], color=colors)
    ax.set_title(title, fontsize=10)
    ax.set_xticks(range(len(kinds)))
    ax.set_xticklabels(["No noise", "Depol.", "Amp.\ndamping", "Phase\ndamping"], fontsize=8)
    ax.set_ylim(0, 0.24)
    for i, k in enumerate(kinds):
        ax.text(i, res[k] + 0.005, f"{res[k]:.3f}", ha="center", fontsize=8)
axes[0].set_ylabel("Fraction of wrong outcomes")
plt.tight_layout()
plt.savefig("figs/noise_demo.png", dpi=200)
print("saved figs/noise_demo.png")
