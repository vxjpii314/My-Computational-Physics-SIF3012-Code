import matplotlib.pyplot as plt
import numpy as np

def faktorial(n) :
    if n == 0 or n == 1 :
        return 1
    else :
        return n * faktorial(n-1)

# Dapatkan input pengguna
input = int(input("Sila masukkan nilai n integer : "))

# Periksa jika input int positif
if input < 0 :
    print("Sila masukkan input positf!")
else :
    print(f"Nilai faktorial bagi {input} adalah: {faktorial(input)}")
    nilai_n = np.arange(0, input + 1, 1)
    nilai_faktorial = [faktorial(n) for n in nilai_n]


# Plot untuk n! melawan n
    plt.subplot(1,2,1)
    plt.plot(nilai_n, nilai_faktorial, marker = "o", linestyle = "-", color = "b")
    plt.xlabel("n")
    plt.ylabel("n!")
    plt.title(f"Plot n! melawan n")

    # Kira e^n untuk setiap n
    eksponen = [np.exp(n) for n in nilai_n]

    # Plotkan graf e^n melawan n
    plt.subplot(1,2,2)
    plt.plot(nilai_n, eksponen, marker = "o", linestyle = "-", color = "r")
    plt.xlabel("n")
    plt.ylabel("e^n")
    plt.title(f"Plot e^n melawan n")

    plt.tight_layout()
    plt.show()
