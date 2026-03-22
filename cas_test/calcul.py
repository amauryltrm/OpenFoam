import numpy as np 

nu = 0.01
L = 0.1
U = 1

print("Re =", L*U/nu)

L = 0.1
nbr_cell = 20
CFL = 0.5
delta_t = CFL*L/(nbr_cell*U)

print("\u0394t = ", delta_t)