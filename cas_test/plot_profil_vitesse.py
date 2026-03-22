import numpy as np 
import matplotlib.pyplot as plt 
import os

print(os.getcwd())

# y = 0.05
x_1 = []
y_11 = []
y_12 = []
y_13 = []

with open(os.getcwd()+"/postProcessing/sampleUx/0.0475/line1_U.xy", "r") as f:
    for line in f:
        parts = line.split()
        x_1.append(float(parts[0]))
        y_11.append(float(parts[1]))
        y_12.append(float(parts[2]))
        y_13.append(float(parts[3]))

y_1 = []
for k in range(len(y_11)):
    y_1.append(np.sqrt(y_11[k]*y_11[k]+y_12[k]*y_12[k]+y_13[k]*y_13[k]))

plt.plot(x_1,y_1)


plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.xlabel("x")
plt.ylabel("Vitesse")
plt.title("Profil de vitesse y=0.5")
plt.legend()
plt.tight_layout()
plt.show()


# x = 0.05
x_2 = []
y_21 = []
y_22 = []
y_23 = []

with open(os.getcwd()+"/postProcessing/sampleUy/0.0475/line1_U.xy", "r") as f:
    for line in f:
        parts = line.split()
        x_2.append(float(parts[0]))
        y_21.append(float(parts[1]))
        y_22.append(float(parts[2]))
        y_23.append(float(parts[3]))

y_2 = []
for k in range(len(y_11)):
    y_2.append(np.sqrt(y_21[k]*y_21[k]+y_22[k]*y_22[k]+y_23[k]*y_23[k]))

plt.plot(y_2,x_2)


plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.xlabel("Vitesse")
plt.ylabel("y")
plt.title("Profil de vitesse x=0.5")
plt.legend()
plt.tight_layout()
plt.show()