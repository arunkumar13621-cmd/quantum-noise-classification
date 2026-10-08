# Identifying Simulated Quantum Noise from Measurement Data

Directed Studies project, M.Eng. Applied Data Science, University of Victoria.
Supervisor: Dr. Ulrike Stege. Student: Arunkumar Krishnamoorthy (V01096197).

## Question

How accurately can machine learning models tell simulated quantum noise types apart
(depolarizing, amplitude damping, phase damping), and does performance change with
noise strength and the number of measurements?

Models: Gaussian Naive Bayes, Random Forest, and an MLP neural network (scikit-learn).
Simulator: Qiskit Aer.

## What is here so far (Deliverable 1: Background Summary)

| File | What it does |
|---|---|
| `make_bloch.py` | Draws how each noise type moves a qubit state (Figure 1) |
| `quantum_noise_demo.py` | Runs the small Qiskit Aer experiment behind Figure 2 |
| `figs/` | Output figures |
| `docs/Background_Summary.pdf` | The submitted Background Summary |

## Run it

```
pip install -r requirements.txt
python make_bloch.py
python quantum_noise_demo.py
```

`quantum_noise_demo.py` uses a fixed seed (7), 8192 shots and noise strength 0.2, so the
numbers repeat: wrong-outcome fractions of 0.095 / 0.198 / 0.000 (setting A, |1> in Z basis)
and 0.100 / 0.055 / 0.055 (setting B, |+> in X basis) for depolarizing / amplitude / phase damping.

## Plan

1. Background Summary (done)
2. Experimental / data-collection plan
3. Data and analysis notebook
4. Final report
