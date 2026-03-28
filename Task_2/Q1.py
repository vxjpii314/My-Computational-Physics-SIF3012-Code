# Medan elektrik malar .
import matplotlib.pyplot as plt
import numpy as np

q = 4.8e-19  # Cas partikel
m = 1.67e-14 # Jisim cas
E0 = 1e5 # Nilai awal medan elektrik
k = 9e9  # Pemalar Coulomb
n = 199 #bil titik
t = 0.0 # Masa awal
dt = 0.1 # Sela masa
pos = 1.0 # Posisi awal
vel = 0.0 # Halaju awal

masa = [t]
posisi = [pos]
halaju = [vel]
tenaga = []

#Lompat katak
vel = vel - 0.5 * (q / m) * E0 * dt

for i in range(n + 1):
    F = E0 * (q / m)
    vel += dt * F
    pos += 2 * dt * vel
    t += dt

    # Tenaga kinetik
    kinetic = 0.5 * m * vel**2

    # Tenaga keupayaan
    r = abs(pos)
    potential = -k * (q ** 2) / r

    # Jumlah tenaga
    Jumlah_E = kinetic + potential
    tenaga.append(Jumlah_E)

    masa.append(t)
    posisi.append(pos)
    halaju.append(vel)

# pos vs t
plt.plot(masa, posisi)
plt.title('Posisi lawan masa')
plt.xlabel('Masa (s)')
plt.ylabel('Posisi (m)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()
plt.show()

# v vs t
plt.plot(masa, halaju, color='orange')
plt.title('Halaju lawan masa')
plt.xlabel('Masa (s)')
plt.ylabel('Halaju (m/s)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()
plt.show()

# Etot vs t
plt.plot(masa[:-1], tenaga, color='green')
plt.title('Jumlah tenaga lawan Masa')
plt.xlabel('Masa (s)')
plt.ylabel('Jumlah Tenaga (J)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()
plt.show()
