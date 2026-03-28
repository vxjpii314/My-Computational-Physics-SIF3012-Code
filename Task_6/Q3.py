"""# Plot X dan Y terhadap ruang

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
A = 1.0
B = 1.0
Rx = 0.1
Ry = 0.05
L = 1.0
Nx = 40
T = 1.0
Nt = 100
alpha = 0.01

dx = L / (Nx - 1)
dt = T / Nt

# Initial conditions
X = np.zeros(Nx)
Y = np.zeros(Nx)
X[0] = 1.0  # Initial value for X
Y[0] = 0.5  # Initial value for Y

# Function to update X and Y using Euler method
def update_system_euler(X, Y, A, B, Rx, Ry, dt, dx):
    dX_dt = A - (B + 1) * X + X**2 * Y + Rx * np.gradient(np.gradient(X, dx), dx)
    dY_dt = B * X - X**2 * Y + Ry * np.gradient(np.gradient(Y, dx), dx)
    X_new = X + dt * dX_dt
    Y_new = Y + dt * dY_dt
    return X_new, Y_new

# Plotting for different time steps using Euler method
plt.figure(figsize=(12, 6))

for t in range(1, Nt + 1):
    X, Y = update_system_euler(X, Y, A, B, Rx, Ry, dt, dx)

    if t % 10 == 0:  # Plot every 10 time steps
        plt.subplot(1, 2, 1)
        plt.plot(np.linspace(0, L, Nx), X, label=f'Time Step {t} (X)')
        plt.xlabel('Space')
        plt.ylabel('Density (X)')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(np.linspace(0, L, Nx), Y, label=f'Time Step {t} (Y)')
        plt.xlabel('Space')
        plt.ylabel('Density (Y)')
        plt.legend()

# Show the subplots
plt.tight_layout()
plt.show()"""


"""## Dengan usikan .
import numpy as np
import matplotlib.pyplot as plt

# parameter
L = 1.0
Nx = 40
T = 1.0
Nt = 100
alpha = 0.01

dx = L / (Nx - 1)
dt = T / Nt

# Nilai awalan
X = np.zeros(Nx)
Y = np.zeros(Nx)
X[0] = 1.0 
Y[0] = 0.5  

# selesaikan fungsi X dan Y menggunakan kaedah euler
def update_system_euler(X, Y, A, B, Rx, Ry, dt, dx):
    dX_dt = A - (B + 1) * X + X**2 * Y + Rx * np.gradient(np.gradient(X, dx), dx)
    dY_dt = B * X - X**2 * Y + Ry * np.gradient(np.gradient(Y, dx), dx)
    X_new = X + dt * dX_dt
    Y_new = Y + dt * dY_dt
    return X_new, Y_new

# Usikan rawak
def generate_random_perturbation():
    perturbation = np.random.uniform(-0.1, 0.1, Nx)
    return perturbation

plt.figure(figsize=(12, 6))

# Nilai-nilai A, B, RX, RY
A = 1.0
B = 1.5
RX = 1e-3
RY = 4e-3

for t in range(1, Nt + 1):
    X, Y = update_system_euler(X, Y, A, B, RX, RY, dt, dx)

    if t % 10 == 0: 
        plt.subplot(1, 2, 1)
        plt.plot(np.linspace(0, L, Nx), X, label=f'Time Step {t} (X)')
        plt.xlabel('Space')
        plt.ylabel('Density (X)')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(np.linspace(0, L, Nx), Y, label=f'Time Step {t} (Y)')
        plt.xlabel('Space')
        plt.ylabel('Density (Y)')
        plt.legend()

X += generate_random_perturbation()
Y += generate_random_perturbation()

plt.tight_layout()
plt.show()"""
