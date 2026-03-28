import numpy as np
import matplotlib.pyplot as plt

particles_count = 10000 # No particles
bins_count = 100 # Number of bins
length = 5.0 # Length
e = 1.6e-19 # Elementary charge
mass = 0.001 # Mass
eps = 8.85e-12 # Vacuum permittivity
time_step = 1  # Time step

particle_positions = np.random.uniform(0, length, particles_count) # scattered partickle
particle_charges = np.random.uniform(-1, 1, particles_count) # Particle charge

charge_density = np.zeros(bins_count) #Charge density

for i in range(bins_count):
    bin_min = i * (length / bins_count)
    bin_max = (i + 1) * (length / bins_count)
    in_bin = (particle_positions >= bin_min) & (particle_positions <= bin_max)
    charge_density[i] = np.sum(particle_charges[in_bin]) / (length / bins_count)

a = 0.5
b = 1
x_val = 6
c = 3.5
electric_field = np.zeros(bins_count)
potential_term = np.zeros(bins_count)
electric_field[0] = -b / (a * x_val + b)
potential_term[0] = c * x_val / (a * x_val - b)

for j in range(0, 100):
    if j + 1 == 100:
        break
    electric_field[j + 1] = -1 / (-2 + electric_field[j])
    potential_term[j + 1] = ((-(length / bins_count) ** 2) * (charge_density[j + 1]) / eps - potential_term[j]) / (
            -2 + electric_field[j])

# Electric Potential
electric_potential = np.zeros(bins_count)
electric_potential[99] = (
        (-(length / bins_count) ** 2) * (charge_density[99]) / eps - potential_term[98]) / (-2 + electric_field[98])

for j in range(0, 100):
    electric_potential[98 - j] = (-1 / (-2 + electric_field[97 - j])) * electric_potential[99 - j] + (
            ((-(length / bins_count) ** 2) * (charge_density[98 - j]) / eps) - potential_term[97 - 1]) / (
                                         -2 + electric_field[97 - 1])

plt.plot(particle_positions[:100], electric_potential, 'rx')
plt.title("Distribution of Electric Potential of 10000 particles")
plt.xlabel("x")
plt.grid(True)
plt.ylabel("Electric Potential")
plt.show()

# a due to E field
acceleration = np.zeros(bins_count)
for i in range(0, 100):
    if i + 2 >= 100:
        acceleration[i] = (e / mass) * (electric_potential[99] - electric_potential[97]) / (2 * length / bins_count)
    else:
        acceleration[i] = (e / mass) * (electric_potential[i + 2] - electric_potential[i]) / (2 * length / bins_count)

initial_time = 0.0  # Initial time
time_values = np.arange(0, 120, time_step)
random_values = np.random.random((100, 1))
velocity_initial = np.zeros((100, 1))
positions = [random_values]
velocities = [velocity_initial + acceleration[0] * time_step]

for current_time in time_values[0:]:
    positions.append(positions[-1] + 2 * time_step * velocities[-1])
    velocities.append(velocities[-1] + 2 * time_step * acceleration[-1])

# position and velocity
positions = np.array(positions)
velocities = np.array(velocities)

plt.plot(positions[:100, 1], charge_density, 'bo')
plt.title("Particle Positions with Electric Field")
plt.xlabel("x")
plt.ylabel("Charge Density")
plt.grid(True)
plt.show()
