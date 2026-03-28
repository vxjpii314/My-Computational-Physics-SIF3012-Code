import numpy as np
import matplotlib.pyplot as plt

nx = 500
m = 10
ni = 10
x1, x2 = -10, 10
h = (x2 - x1) / nx
nr, nl = 0, 0
ul = np.zeros(nx + 1)
ur = np.zeros(nx + 1)
ql = np.zeros(nx + 1)
qr = np.zeros(nx + 1)
s = np.zeros(nx + 1)
u = np.zeros(nx + 1)


def main():
    del_val = 1e-6
    e = 2.4
    de = 0.1

    # Kaedah sekan
    e = secant(ni, del_val, e, de)

    # output fungsi gelombang
    with open("fungsi gelombang.oxh", "w") as w:
        x = x1
        mh = m * h
        for i in range(0, nx + 1, m):
            w.write(f"{x} {u[i]}\n")
            x += mh

    # Nilai output eigen
    print("The eigenvalue:", e)

    # Plotkan V(x) dan phi(x)
    x_vals = np.linspace(x1, x2, nx + 1)
    v_vals = [v(x_val) for x_val in x_vals]
    plt.figure(figsize=(10, 5))

    plt.subplot(2, 1, 1)
    plt.plot(x_vals, v_vals, label='$V(x)$')
    plt.title('$V(x)$')
    plt.xlabel('$x$')
    plt.ylabel('$V(x)$')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(x_vals, u, label='$\phi(x)$', color='orange')
    plt.title('$\phi(x)$')
    plt.xlabel('$x$')
    plt.ylabel('$\phi(x)$')
    plt.legend()

    plt.tight_layout()
    plt.grid(True)
    plt.show()

# kaedah sekan
def secant(n, del_val, x, dx):

    def f(x_val):
        wave(x_val)
        f0 = ur[nr - 1] + ul[nl - 1] - ur[nr - 3] - ul[nl - 3]
        return f0 / (2 * h * ur[nr - 2])

    while True:
        psi1, psi2 = f(x + dx), f(x)
        x, dx = x - psi2 * (dx / (psi1 - psi2)), psi2 * (dx / (psi1 - psi2))
        if abs(dx) < del_val:
            break

    return x


def wave(energy):
    y = np.zeros(nx + 1)
    u0, u1 = 0, 0.01

    # fungsi q(x)
    for i in range(0, nx + 1):
        x_val = x1 + i * h
        ql[i] = 2 * (energy - v(x_val))
        qr[nx - i] = ql[i]

    im = 0
    for i in range(nx):
        if ql[i] * ql[i + 1] < 0 and ql[i] > 0:
            im = i

    # Kaedah Numerov
    global nl, nr, ul, ur
    nl = im + 2
    nr = nx - im + 2
    ul = numerov(nl, h, u0, u1, ql, s)
    ur = numerov(nr, h, u0, u1, qr, s)

    # Fungsi gelombang di kiri
    ratio = ur[nr - 2] / ul[im]
    for i in range(0, im + 1):
        u[i] = ratio * ul[i]
        y[i] = u[i] * u[i]

    # Fungsi gelombang di kanan
    for i in range(0, nr - 1):
        u[i + im] = ur[nr - i - 2]
        y[i + im] = u[i + im] * u[i + im]

    # Normalkan fungsi gelombang
    global simpson
    sum_y = simpson(y, h)
    sum_y = np.sqrt(sum_y)
    for i in range(0, nx + 1):
        u[i] /= sum_y

def numerov(m_val, h_val, u0_val, u1_val, q_val, s_val):
    u_val = np.zeros(m_val)
    u_val[0], u_val[1] = u0_val, u1_val
    g_val = h_val * h_val / 12

    for i in range(1, m_val - 1):
        c0 = 1 + g_val * q_val[i - 1]
        c1 = 2 - 10 * g_val * q_val[i]
        c2 = 1 + g_val * q_val[i + 1]
        d = g_val * (s_val[i + 1] + s_val[i - 1] + 10 * s_val[i])
        u_val[i + 1] = (c1 * u_val[i] - c0 * u_val[i - 1] + d) / c2

    return u_val
# Kaedah simpson
def simpson(y_val, h_val):
    n_val = len(y_val)
    if n_val % 2 == 0:
        h_val *= 2
        return np.sum(y_val[0:n_val - 2:2] + 4 * y_val[1:n_val - 1:2] + y_val[2:n_val:2]) * h_val / 3
    else:
        return np.sum(y_val[0:n_val - 2:2] + 4 * y_val[1:n_val - 1:2] + y_val[2:n_val:2]) * h_val / 3 + (
                y_val[-2] + y_val[-1]) * h_val / 2


def v(x_val):
    alpha = 1
    lambda_val = 4
    return alpha * alpha * lambda_val * (lambda_val - 1) * (0.5 - 1 / np.cosh(alpha * x_val) ** 2) / 2


main()
