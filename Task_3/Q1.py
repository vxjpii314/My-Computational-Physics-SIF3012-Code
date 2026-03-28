
    m3 = h*(v + 0.5*k2)
    k3 = h*F(u+0.5*m2, v+0.5*k2, t+0.5*h)

    m4 = h*(v + k3)
    k4 = h*F(u+m3, v+k3, t+h)

    u += (m1 + 2*m2 + 2*m3 + m4)/6
    v += (k1 + 2*k2 + 2*k3 + k4)/6

t_value = 1
index = min(range(len(tpoints)), key=lambda i: abs(tpoints[i] - t_value))
u_value = upoints[index]
print(f"For t = {t_value}, u = {u_value}")
a = abs(u_value - 1)   #|u(1) - 1|
print("The value of |u(1) - 1| is  ", a)"""


## Cara 2 : Lebih cepat .
"""import numpy as np
import matplotlib.pyplot as plt

n = 100
ni = 10
m = 5
h = 1.0 / n

def main():
    del_val = 1e-6
    alpha0 = 1
    dalpha = 0.01
    y1 = np.zeros(n+1)
    y2 = np.zeros(n+1)
    y = np.zeros(2)

    y[0] = y1[0] = 0
    y[1] = y2[0] = secant(ni, del_val, alpha0, dalpha)

    for i in range(n):
        x = h * i
        y = runge_kutta(y, x, h)
        y1[i+1] = y[0]
        y2[i+1] = y[1]

    for i in range(0, n+1, m):
        print(f"x: {h * i}, y1: {y1[i]}")

    # Plot
    plt.plot(np.arange(0, 1.01, h), y1)
    plt.title('Function y1(x)')
    plt.grid(True)
    plt.axvline(0, color = 'black', linewidth = 1)
    plt.axhline(0, color='black', linewidth=1)
    plt.xlabel('x')
    plt.ylabel('y1')
    plt.show()

def secant(n, del_val, x, dx):
    # Kaedah sekan
    for _ in range(n):
        f_x = f(x)
        x -= f_x * dx / (f(x + dx) - f_x)
        if abs(f_x) < del_val:
            break
    return x

def f(x):
    # Mencari punca f(x)
    y = np.zeros(2)
    y[0] = 0
    y[1] = x
    for i in range(n-1):
        xi = h * i
        y = runge_kutta(y, xi, h)
    return y[0] - 1

def runge_kutta(y, t, dt):
    # RK4
    k1 = dt * g(y, t)
    k2 = dt * g(y + 0.5 * k1, t + 0.5 * dt)
    k3 = dt * g(y + 0.5 * k2, t + 0.5 * dt)
    k4 = dt * g(y + k3, t + dt)

    y += (k1 + 2*k2 + 2*k3 + k4) / 6
    return y

def g(y, t):
    # ODE
    k = len(y)
    v = np.zeros(k)
    v[0] = y[1]
    v[1] = -np.pi**2 * (y[0] + 1) / 4
    return v
main()"""
