import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

# Pemalar
hbar = 1.0
m = 1.0
L = 10.0  # Panjang
N = 500  # Berapa banyak grid
dx = L / N
dt = 0.01  # Langkah masa
t_max = 5.0  # Masa simulasi

# Grid
x_values = np.linspace(0, L, N + 1)

# Paket gelomabng Gauss
sigma = 0.5
k0 = 5.0
psi = np.exp(-(x_values - 2.0) ** 2 / (2.0 * sigma ** 2)) * np.exp(1.0j * k0 * x_values)

# Telaga empat segi
V = np.zeros(N + 1)
V[4:7] = 50.0 

# Kaedah Crank-Nicolson
alpha = 0.5 * 1j * hbar / (m * dx ** 2)
beta = 0.5 * 1j * hbar / (m * dx ** 2)

# sistem matriks A tridiagonal
A_upper = np.diag(-beta * np.ones(N), k=1)
A_lower = np.diag(-beta * np.ones(N), k=-1)
A_main = np.diag(1.0 + 2.0 * alpha + V * dt / hbar, k=0)
A = A_upper + A_lower + A_main

# sistem matriks B tridiagonal
B_upper = np.diag(beta * np.ones(N), k=1)
B_lower = np.diag(beta * np.ones(N), k=-1)
B_main = np.diag(1.0 - 2.0 * alpha - V * dt / hbar, k=0)
B = B_upper + B_lower + B_main

# Evolusi masa
for t in np.arange(0, t_max, dt):
    b = B @ psi
    psi = solve(A, b)

# Plotkan
plt.plot(x_values, np.abs(psi) ** 2)
plt.title('Kedudukan melawan kebarangkalian')
plt.xlabel('Kedudukan')
plt.ylabel('Kebarangkalian')
plt.show()
