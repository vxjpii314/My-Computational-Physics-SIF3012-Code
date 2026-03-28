import numpy as np
import matplotlib.pyplot as plt

def solve_pendulum(q, b, w0, t_max=100, dt=0.01):
    # Bilangan langkah
    n_steps = int(t_max / dt)
    t = np.linspace(0, t_max, n_steps)
    
    # Untuk menyimpan nilai (theta, omega)
    # y = [theta, omega]
    y = np.zeros((n_steps, 2))
    
    # Keadaan awal: bermula dari rehat
    y[0] = [0.0, 0.0] 

    # Fungsi bezaan(Persamaan Peringkat Pertama)
    def f(t_val, state):
        theta, omega = state
        d_theta = omega
        d_omega = -q * omega - np.sin(theta) + b * np.cos(w0 * t_val)
        return np.array([d_theta, d_omega])

    # Gelung RK4
    for i in range(n_steps - 1):
        ti = t[i]
        yi = y[i]
        
        k1 = dt * f(ti, yi)
        k2 = dt * f(ti + 0.5*dt, yi + 0.5*k1)
        k3 = dt * f(ti + 0.5*dt, yi + 0.5*k2)
        k4 = dt * f(ti + dt, yi + k3)
        
        y[i+1] = yi + (k1 + 2*k2 + 2*k3 + k4) / 6
        
        # Normalkan theta ke dalam julat [-pi, pi] supaya plot fasa kemas
        y[i+1, 0] = (y[i+1, 0] + np.pi) % (2 * np.pi) - np.pi

    return t, y[:, 0], y[:, 1]

# Parameter kes
cases = [
    {'params': (0.5, 0.9, 2/3), 'title': 'Kes A: q=0.5, b=0.9, w0=2/3 (Berkala)'},
    {'params': (0.5, 1.15, 2/3), 'title': 'Kes B: q=0.5, b=1.15, w0=2/3 (Kalut)'}
]

plt.figure(figsize=(12, 5))

for i, case in enumerate(cases):
    q, b, w0 = case['params']
    t, theta, omega = solve_pendulum(q, b, w0, t_max=200) # t_max lebih lama untuk lihat kestabilan
    
    plt.subplot(1, 2, i+1)
    # Plot fasa (Hanya plot 100 saat terakhir untuk hilangkan kesan transien awal)
    start_idx = len(t) // 2
    plt.plot(theta[start_idx:], omega[start_idx:], lw=0.5, color='blue')
    plt.title(case['title'])
    plt.xlabel('Theta (rad)')
    plt.ylabel('Omega (rad/s)')
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
