import numpy as np
import matplotlib.pyplot as plt

s = 0.5                                   # noise strength, large so the movement is visible
start = np.array([np.sin(np.pi/4), np.cos(np.pi/4)])   # (x, z) of a pure state

def depol(v):   return (1 - s) * v
def amp(v):     return np.array([np.sqrt(1 - s) * v[0], s + (1 - s) * v[1]])
def phase(v):   return np.array([np.sqrt(1 - s) * v[0], v[1]])

panels = [("Depolarizing", depol), ("Amplitude damping", amp), ("Phase damping", phase)]
fig, axes = plt.subplots(1, 3, figsize=(7.5, 2.7))
t = np.linspace(0, 2*np.pi, 200)
for ax, (name, f) in zip(axes, panels):
    ax.plot(np.cos(t), np.sin(t), color="#bbbbbb", lw=1)
    ax.axhline(0, color="#dddddd", lw=0.8); ax.axvline(0, color="#dddddd", lw=0.8)
    end = f(start)
    ax.annotate("", xy=start, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="#999999", lw=1.4))
    ax.annotate("", xy=end, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="#C44E52", lw=1.8))
    ax.text(0, 1.12, "|0>", ha="center", fontsize=9)
    ax.text(0, -1.27, "|1>", ha="center", fontsize=9)
    ax.text(1.08, -0.04, "x", fontsize=8, color="#777777")
    ax.set_title(name, fontsize=10)
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.4, 1.3)
    ax.set_aspect("equal"); ax.axis("off")
fig.text(0.5, 0.01, "grey = starting state, red = after noise (strength 0.5, x-z slice of the Bloch sphere)",
         ha="center", fontsize=8, color="#555555")
plt.tight_layout(rect=(0, 0.04, 1, 1))
plt.savefig("figs/bloch_slices.png", dpi=200)
print("ok")
