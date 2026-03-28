"""
#Persamaan tangsi :

f(x) = x/2 ; 0 < x < 2
     = -x/2 + 2 ; 2 < x < 4

ak = 2/J Sigma(j = 1 to J) fj * sin(pi*j*k/J) ; J = 16
"""
import numpy as np
import matplotlib.pyplot as plt

# Persamaan tangsi
def f(x):
    if 0 < x < 2:
        return x / 2
    elif 2 <= x <= 4:
        return -x / 2 + 2
    else:
        return 0

# Mengira pekali ak
def pekali(k):
    ak_tot = sum((f(x) * np.sin(k * x * np.pi / 4)) for x in np.linspace(0, 16))
    ak = (2 / 16) * ak_tot
    return ak

# Fungsi siri Fourier
def siri_fx(x, N):
    siri_tot = sum(pekali(k) * np.sin(k * x * np.pi / 4) for k in range(1, N + 1))
    return siri_tot

# nilai x = k pada sela 16/1000 .
xval = np.linspace(0, 16, 1000)

# f(x) berlainan N
for N in [1, 2, 3, 4, 8, 16]:
    yval = [siri_fx(x, N) for x in xval]
    plt.plot(xval, yval, label=f'N = {N}')

# f(x) asal
fx_asal = [f(x) for x in xval]
plt.plot(xval, fx_asal, label='f(x) asal')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Penghampiran siri Fourier pada nilai N berbeza')
plt.grid(True)
plt.axhline(0, color = 'black', linewidth = 1)
plt.axvline(0, color = 'black', linewidth = 1)
plt.show()

# PART 2
import numpy as np
import matplotlib.pyplot as plt

L = 4.0 # Panjang tangsi
T = 1.0 # jumlah masa
Nx = 100 # Jumlah grid
Nt = 200 # Langkah masa
k = 1 # Nombor gelombang

# Pendiskretan
dx = L / (Nx - 1)
dt = T / Nt

x = np.linspace(0, L, Nx)

# Nilai awal
f = np.piecewise(x, [x <= 2, x > 2], [lambda x: x / 2, lambda x: -(x / 2 + 2)])

# Keadaan sempadan
f[0] = 0
f[-1] = 0


for n in range(0, Nt):
    # pembezaan kedua
    df2dx2 = np.diff(f, 2) / dx**2
    f[1:-1] += dt * (df2dx2 * np.sin(k * np.pi * x[1:-1] / 4))

# Plotkan
plt.plot(x, f)
plt.title('f(t) melawan t')
plt.xlabel('x')
plt.ylabel('f(x, t)')
plt.show()
