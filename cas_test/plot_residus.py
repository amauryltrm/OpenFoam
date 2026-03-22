import numpy as np 
import matplotlib.pyplot as plt 
import os

print(os.getcwd())

x = []
title = ["p_0","Ux_0","Uy_0"]
y = []

# Récupération des données
for k in title:
    a = []
    b = []
    with open("logs/" + k, "r") as f:
        for line in f:
            parts = line.split()
            a.append(float(parts[1]))
            b.append(float(parts[0]))
    x.append(b)
    y.append(a)


# Plot
plt.figure(figsize=(8,5))
for k in range(len(title)):
    plt.plot(x[k], y[k], label=title[k])

plt.yscale("log")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.xlabel("Temps")
plt.ylabel("Résidu final")
plt.title("Convergence des résidus (Ux, Uy, p) Maillage 1")
plt.legend()
plt.tight_layout()
plt.show()