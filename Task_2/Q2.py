import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Pemalar
q = 1.6e-19
m = 1.67e-27
N_particles = 100 
n_steps = 200
t = 0.0
dt = 0.1         
k_constant = 8.99e9  # Pemalar Coulomb

# nilai awal
# Kedudukan dari x = 1 hingga x = 10 m
positions = np.random.uniform(1.0, 10.0, (N_particles, 2))  
velocities = np.random.uniform(-0.1, 0.1, (N_particles, 2)) # Halaju awal sedikit random

pos_values = [positions.copy()]

# Lompat katak
for i in range(n_steps):
    F = np.zeros((N_particles, 2))

    # Pengiraan daya langkah pertama
    for j in range(N_particles):
        for k in range(N_particles):
            if j != k:
                r_vec = positions[j] - positions[k]
                dist = np.linalg.norm(r_vec)
                R = max(dist, 0.1) # 'Softening' supaya tidak meletup jika terlalu dekat
                # PEMBETULAN: Formula Coulomb F = k*q1*q2 / r^2 dalam arah unit vektor
                F[j] += (k_constant * q**2 / R**2) * (r_vec / R)  # Daya Elektik partikel 1

    velocities += 0.5 * dt * F / m # Update halaju (setengah langkah)
    positions += dt * velocities   # Update posisi
    
    # Pengiraan daya baharu (langkah baharu)
    F_new = np.zeros((N_particles, 2))
    for j in range(N_particles):
        for k in range(N_particles):
            if j != k:
                r_vec = positions[j] - positions[k]
                dist = np.linalg.norm(r_vec)
                R = max(dist, 0.1)
                F_new[j] += (k_constant * q**2 / R**2) * (r_vec / R)  # Daya Elektrik partikel 2

    velocities += 0.5 * dt * F_new / m # Update halaju (baki setengah langkah)

    pos_values.append(positions.copy())

# Simulasi
fig, ax = plt.subplots()
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=20, color='blue')

def update(frame):
    scatter.set_offsets(pos_values[frame])
    return scatter,

ani = FuncAnimation(fig, update, frames=len(pos_values), interval=30, blit=True)

plt.title('Gerakan Zarah Bersalingtindak')
plt.xlabel('X-axis (meter)')
plt.ylabel('Y-axis (meter)')
plt.show()
