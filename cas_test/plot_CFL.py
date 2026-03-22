import numpy as np 
import matplotlib.pyplot as plt 
import os

print(os.getcwd())


x_max = []
x_mean = []
CFL_max = []
CFL_mean = []

with open("logs/CourantMax_0", "r") as f:
    for line in f:
        parts = line.split()
        x_max.append(float(parts[0]))
        CFL_max.append(float(parts[1]))
        
with open("logs/CourantMean_0", "r") as f:
    for line in f:
        parts = line.split()
        x_mean.append(float(parts[0]))
        CFL_mean.append(float(parts[1]))

#plt.yscale("log")
plt.plot(x_mean,CFL_mean,label="CFL moyen")
plt.plot(x_max,CFL_max,label="CFL Max")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.xlabel("Temps")
plt.ylabel("CFL")
plt.title("Valeurs du nombre CFL")
plt.legend()
plt.tight_layout()
plt.show()