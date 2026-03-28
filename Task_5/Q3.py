import numpy as np

# Matriks rawak 6x6
A = np.random.randint(1, 11, size=(6, 6))

#Vektor tekaan awal x
x0 = np.random.rand(6)

#Tetapkan tolerans untuk konvergensi dalam lelaran songsang
ketepatan = 1e-6

#lelaran songsang
def lelaran_songsang(A, x, tol):

    lelaran = 100
    for _ in range(lelaran):
        x_baru = np.linalg.inv(A) @ x
        x = x_baru / np.linalg.norm(x_baru)
        if np.linalg.norm(x - x_baru) < tol:
            break
    return x

#Selesaikan Ax = kx
vektor_eigen_songsang = lelaran_songsang(A, x0, ketepatan)

#Kira nilai eigen yang sepadan
nilai_eigen_songsang = np.dot(A, vektor_eigen_songsang) / np.dot(vektor_eigen_songsang, vektor_eigen_songsang)

#Cetak hasil
print("Matriks Rawak A:")
print(A)

print("\nVektor Eigen dari Lelaran Songsang:")
print(vektor_eigen_songsang)

print("\nNilai Eigen yang Sepadan:")
print(nilai_eigen_songsang)

#Q3, part 2
import numpy as np

#Matriks rawak 6x6 A dengan unsur dalam julat 1 hingga 10
A = np.random.randint(1, 11, size=(6, 6))

# Cari nilai eigen matriks A
nilai_eigen = np.linalg.eigvals(A)

#Kira determinan matriks A
determinan_A = np.linalg.det(A)

#Kira hasil darab nilai eigen
hasil_darab_nilai_eigen = np.prod(nilai_eigen)

#Cetak hasil
print("Matriks Rawak 6x6 A:")
print(A)

print("\nNilai Eigen Matriks A:")
print(nilai_eigen)

print("\nDeterminan Matriks A:", determinan_A)
print("Hasil Darab Nilai Eigen:", hasil_darab_nilai_eigen)

#semak jika determinan sama dengan hasil darab nilai eigen
if np.isclose(determinan_A, hasil_darab_nilai_eigen):
    print("\nDeterminan A sama dengan hasil darab nilai eigen.")
else:
    print("\nDeterminan A tidak sama dengan hasil darab nilai eigen.")
