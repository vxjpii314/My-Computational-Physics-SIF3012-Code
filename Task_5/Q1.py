## Mencari determinan matriks 1x1, 2x2, 3x3 sahajaS

def det_1x1(matriks):

  return matriks[0][0]

def det_2x2(matriks):

  return (matriks[0][0] * matriks[1][1]) - (matriks[0][1] * matriks[1][0])

def det_3x3(matriks):

  # Cara biasa je
  return (
      matriks[0][0] * det_2x2([[matriks[1][1], matriks[1][2]], [matriks[2][1], matriks[2][2]]])
      - matriks[0][1] * det_2x2([[matriks[1][0], matriks[1][2]], [matriks[2][0], matriks[2][2]]])
      + matriks[0][2] * det_2x2([[matriks[1][0], matriks[1][1]], [matriks[2][0], matriks[2][1]]])
  )

#Contoh
matriks_1x1 = [[1]]
matriks_2x2 = [[1, 2], [3, 4]]
matriks_3x3 = [[1, -2, 3], [4, -5, 6], [-7, 8, 9]]

print(f"Determinan matriks 1x1: {det_1x1(matriks_1x1)}")
print(f"Determinan matriks 2x2: {det_2x2(matriks_2x2)}")
print(f"Determinan matriks 3x3: {det_3x3(matriks_3x3)}")

"""
Program mencari determinan bagi matriks segiempat sama menggugunakan fungsi lelaran. Misalnya jika diberi matriks 4x4, maka kita harus mencari determinan 3x3
 seterusnya 2x2 dan barulah dapat jawapan. Maka determinan 3x3 = pekali*kofaktor*(determinan 2x2)
"""

def det(matriks):

  if len(matriks) == 1:
    return matriks[0][0]
  else:
    determinan = 0
    for i in range(len(matriks)):
      kofaktor = (-1)**i * det([
          baris[:i] + baris[i+1:] for baris in matriks[1:]
      ])
      determinan += matriks[0][i] * kofaktor
    return determinan

# Contoh
# Anda boleh memasukkan matriks bersaiz segiempat lain(cth 5x5) disini. Bebas, suka hati anda lah . Nanti ia akan memunculkan output determinan !!
matriks_1x1 = [[1]]
matriks_2x2 = [[3, 2], [-1, 7]]
matriks_3x3 = [[2, 2, 9], [5, -6, 4], [7, 9, 2]]
matriks_4x4 = [[4,0,-1,5], [6,4,2,8], [7,9,4,-1], [0,6,3,8]]
matriks_5x5 = [[7,9,-1,-1, 7], [6,4,2,8, 8], [7,9,4,-1, 9], [0,6,3,8, 10], [5,6,8,3,2]]
#matriks_nxn = ........

print(f"Det matriks 1x1: {det(matriks_1x1)}")
print(f"Det matriks 2x2: {det(matriks_2x2)}")
print(f"Det matriks 3x3: {det(matriks_3x3)}")
print(f"Det matriks 4x4: {det(matriks_4x4)}")
print(f"Det matriks 5x5: {det(matriks_5x5)}")
#print(f"Det matriks nxn : {det(matriks_nxn})

#Q1, i
"""
Program mencari determinan bagi matriks segiempat sama menggugunakan fungsi lelaran. Misalnya jika diberi matriks 4x4, maka kita harus mencari determinan 3x3
 seterusnya 2x2 dan barulah dapat jawapan. Maka determinan 3x3 = pekali*kofaktor*(determinan 2x2)
"""

def det(matriks):

  if len(matriks) == 1:
    return matriks[0][0]
  else:
    determinan = 0
    for i in range(len(matriks)):
      kofaktor = (-1)**i * det([
          baris[:i] + baris[i+1:] for baris in matriks[1:]
      ])
      determinan += matriks[0][i] * kofaktor
    return determinan

# Ini hanya contoh matriks 10x10. Anda boleh mengubahnya sesuka hati anda dengan syarat ianya matriks nxn berbentuk segitiga.
matriks_10x10 =\
[[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [3, 0, 2, 0, 0, 0, 0, 0, 0, 0],
 [4, 1, 0, 3, 0, 0, 0, 0, 0, 0],
 [5, 0, 7, 0, 7, 0, 0, 0, 0, 0],
 [4, 0, 6, 0, 0, 9, 0, 0, 0, 0],        #Matriks 10x10 berbentuk segitiga atas
 [5, 0, 0, 0, 0, 0, -1, 0, 0, 0],
 [7, 8, 0, 0, 9, 0, 0, 4, 0, 0],
 [9, 0, 0, 0, 0, 0, 0, 0, 3, 0],
 [10, 0, 0, 3, 0, 0, 0, 0, 0, 9]]

hasil_darab_penjuru = 1
for i in range(1, len(matriks_10x10)):
  hasil_darab_penjuru *= matriks_10x10[i][i]

print(f"determinan adalah : {det(matriks_10x10)}")
print(f"Hasil darab pepenjuru: {hasil_darab_penjuru}")

## Jika kedua output sama maka TERBUKTI ##

#Q1, ii
def det(matriks):

  if len(matriks) == 1:
    return matriks[0][0]
  else:
    determinan = 0
    for i in range(len(matriks)):
      kofaktor = (-1)**i * det([
          baris[:i] + baris[i+1:] for baris in matriks[1:]
      ])
      determinan += matriks[0][i] * kofaktor
    return determinan

# Ini hanya contoh matriks 10x10. Anda boleh mengubahnya sesuka hati anda dengan syarat ianya matriks nxn berbentuk segitiga.
matriks_10x10 =\
[[2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [3, 0, 2, 0, 0, 0, 0, 0, 0, 0],
 [4, 1, 0, 3, 0, 0, 0, 0, 0, 0],
 [5, 0, 7, 0, 7, 0, 0, 0, 0, 0],     # Disini saya menukargantikan baris 1 menjadi baris 2 daripada matriks asal.
 [4, 0, 6, 0, 0, 9, 0, 0, 0, 0],
 [5, 0, 0, 0, 0, 0, -1, 0, 0, 0],
 [7, 8, 0, 0, 9, 0, 0, 4, 0, 0],
 [9, 0, 0, 0, 0, 0, 0, 0, 3, 0],
 [10, 0, 0, 3, 0, 0, 0, 0, 0, 9]]
"""
Matriks asal tadinya : 
[[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [3, 0, 2, 0, 0, 0, 0, 0, 0, 0],
 [4, 1, 0, 3, 0, 0, 0, 0, 0, 0],
 [5, 0, 7, 0, 7, 0, 0, 0, 0, 0],       Output determinan = -40824
 [4, 0, 6, 0, 0, 9, 0, 0, 0, 0],        
 [5, 0, 0, 0, 0, 0, -1, 0, 0, 0],
 [7, 8, 0, 0, 9, 0, 0, 4, 0, 0],
 [9, 0, 0, 0, 0, 0, 0, 0, 3, 0],
 [10, 0, 0, 3, 0, 0, 0, 0, 0, 9]]
"""

print(f"Det matriks 10x10: {det(matriks_10x10)}") ##Output deteminan = 40824

##TERBUKTI##

#Q1, iii
def det(matriks):

  if len(matriks) == 1:
    return matriks[0][0]
  else:
    determinan = 0
    for i in range(len(matriks)):
      kofaktor = (-1)**i * det([
          baris[:i] + baris[i+1:] for baris in matriks[1:]
      ])
      determinan += matriks[0][i] * kofaktor
    return determinan

# Ini hanya contoh matriks 10x10. Anda boleh mengubahnya sesuka hati anda dengan syarat ianya matriks nxn berbentuk segitiga.
matriks_10x10 =\
[[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [3, 0, 2, 0, 0, 0, 0, 0, 0, 0],
 [4, 1, 0, 3, 0, 0, 0, 0, 0, 0],
 [5, 0, 7, 0, 7, 0, 0, 0, 0, 0],     # Disini saya menduakan(duplicate) baris 2 menjadi baris 1 supaya terdapat 2 baris yg serupa.
 [4, 0, 6, 0, 0, 9, 0, 0, 0, 0],
 [5, 0, 0, 0, 0, 0, -1, 0, 0, 0],
 [7, 8, 0, 0, 9, 0, 0, 4, 0, 0],
 [9, 0, 0, 0, 0, 0, 0, 0, 3, 0],
 [10, 0, 0, 3, 0, 0, 0, 0, 0, 9]]

matriks_10x10_lajur =\
[[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
 [3, 3, 2, 0, 0, 0, 0, 0, 0, 0],
 [4, 4, 0, 3, 0, 0, 0, 0, 0, 0],
 [5, 5, 7, 0, 7, 0, 0, 0, 0, 0],     # Disini saya menduakan(duplicate) lajur 2 menjadi lajur 1 supaya terdapat 2 lajur yg serupa.
 [4, 4, 6, 0, 0, 9, 0, 0, 0, 0],
 [5, 5, 0, 0, 0, 0, -1, 0, 0, 0],
 [7, 7, 0, 0, 9, 0, 0, 4, 0, 0],
 [9, 9, 0, 0, 0, 0, 0, 0, 3, 0],
 [10, 10, 0, 3, 0, 0, 0, 0, 0, 9]]

"""
Matriks asal tadinya : 
[[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [3, 0, 2, 0, 0, 0, 0, 0, 0, 0],
 [4, 1, 0, 3, 0, 0, 0, 0, 0, 0],
 [5, 0, 7, 0, 7, 0, 0, 0, 0, 0],       Output determinan = -40824
 [4, 0, 6, 0, 0, 9, 0, 0, 0, 0],        
 [5, 0, 0, 0, 0, 0, -1, 0, 0, 0],
 [7, 8, 0, 0, 9, 0, 0, 4, 0, 0],
 [9, 0, 0, 0, 0, 0, 0, 0, 3, 0],
 [10, 0, 0, 3, 0, 0, 0, 0, 0, 9]]
"""

print(f"Det matriks 10x10 2 baris serupa: {det(matriks_10x10)}") ##Output deteminan = 0
print(f"Det matriks 10x10 2 lajur serupa: {det(matriks_10x10_lajur)}") ##Output deteminan = 0

##TERBUKTI##

#Q1, iv
def Darab(Matriks_A, Matriks_B):

  # Periksa jika bil lajur matriks A sepadan dengan bil baris matriks B (Syarat pendaraban matriks) .
  if len(Matriks_A[0]) != len(Matriks_B):
    raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

  # Nilai awal bagi matriks A dan B sebagai tatasusunan = 0.
  Hasil_darab_matriks = [[0 for _ in range(len(Matriks_B[0]))] for _ in range(len(Matriks_A))]

  # Darab menggunakan kaedah ulangan bagi setiap baris darab lajur matriks A dan B .
  for i in range(len(Hasil_darab_matriks)):
    for j in range(len(Hasil_darab_matriks[0])):
        Hasil_darab_matriks[i][j] = sum(Matriks_A[i][k] * Matriks_B[k][j] for k in range(len(Matriks_B)))

  return Hasil_darab_matriks

def det(matriks):

  if len(matriks) == 1:
    return matriks[0][0]
  else:
    determinan = 0
    for i in range(len(matriks)):
      kofaktor = (-1)**i * det([
          baris[:i] + baris[i+1:] for baris in matriks[1:]
      ])
      determinan += matriks[0][i] * kofaktor
    return determinan

# Definisikan matriks A dan B .
Matriks_A = [[1, 0, 0, 0, 0, -1, 0, 0, 0, 6],
            [2, 1, 0, 0, 0, 0, -1, 0, 0, 0],
            [3, 0, 2, 0, 0, 4, 0, 9, 0, 0],
            [4, 1, 0, 3, 0, 0, 0, 0, 0, 0],
            [5, 0, 7, 0, 7, 0, 0, 4, 0, 0],
            [4, 0, 6, 0, 0, 9, 0, 5, 0, 0],
            [5, 0, 0, 0, 0, 0, -1, 0, 0, 0],
            [7, 8, 0, 0, 9, 0, 0, 4, 0, 0],
            [9, 0, 0, 0, 9, 0, 0, 0, 3, 0],
            [10, 0, 0, 3, 0, 0, 9, 0, 0, 9]]

Matriks_B = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 1, 5, 0, 3, 0, 0, 0, 0, 0],
            [3, 0, 2, 0, 0, 0, 0, 0, 0, 0],
            [4, 1, 0, 3, 0, 6, 0, 0, 0, 0],
            [5, 0, 7, 0, 7, 0, 6, 0, 0, 0],
            [4, 0, 6, 0, 0, 9, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, -1, 0, 0, 0],
            [7, 8, 0, 0, 9, -1, 0, 4, 0, 0],
            [9, 0, 0, 0, 9, 0, 0, 0, 3, 0],
            [10, 0, 0, 3, 0, 0, 9, 0, 0, 9]]

# Kira hasil darab  mereka
Hasil_darab_matriks = Darab(Matriks_A, Matriks_B)

# Cetak diatas .
print("Hasil darab matriks A dan B:")
for row in Hasil_darab_matriks:
  print(row)

# Kira determinan matriks yang terhasil .
Determinant_AB = det(Hasil_darab_matriks)

# Cetak diatas !
print("Det (AB):", Determinant_AB)
# Cetak hasil darab determinan individu. Adakah ia sama bila kita darab kemudian dapatkan determinan ?
print(f"Det(A) * Det(B): {det(Matriks_A) * det(Matriks_B)}")

## Terbukti ianya sama ##

#Q1, v
def transpos_mat(matriks):

  baris = len(matriks)
  lajur = len(matriks[0])

  Hasil = [[0 for _ in range(baris)] for _ in range(lajur)]

  for i in range(baris):
    for j in range(lajur):
      Hasil [j][i] = matriks[i][j]

  return Hasil

# Define the matrix A.
Matriks_10x10 =     [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [3, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                    [4, 1, 0, 3, 0, 0, 0, 0, 0, 0],
                    [5, 0, 7, 0, 7, 0, 0, 0, 0, 0],
                    [4, 0, 6, 0, 0, 9, 0, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0, -1, 0, 0, 0],
                    [7, 8, 0, 0, 9, 0, 0, 4, 0, 0],
                    [9, 0, 0, 0, 0, 0, 0, 0, 3, 0],
                    [10, 0, 0, 3, 0, 0, 0, 0, 0, 9]]

# Find and print the transpose of the matrix.
Hasil = transpos_mat(Matriks_10x10)
print("Transpose bagi matriks A ialah :")
for row in Hasil:
  print(row)

def det(matriks):

  if len(matriks) == 1:
    return matriks[0][0]
  else:
    determinan = 0
    for i in range(len(matriks)):
      kofaktor = (-1)**i * det([
          baris[:i] + baris[i+1:] for baris in matriks[1:]
      ])
      determinan += matriks[0][i] * kofaktor
    return determinan

# DARIPADA OUTPUT TRANSPOS MATRIKS, SALIN OUTPUT MASUK KE PEMBOLEHUBAH DIBAWAH !!
Matriks_10x10_transpos = [[1, 2, 3, 4, 5, 4, 5, 7, 9, 10],
                           [0, 1, 0, 1, 0, 0, 0, 8, 0, 0],
                           [0, 0, 2, 0, 7, 6, 0, 0, 0, 0],
                            [0, 0, 0, 3, 0, 0, 0, 0, 0, 3],
                            [0, 0, 0, 0, 7, 0, 0, 9, 0, 0],        #SALIN OUTPUT TRANPOS A DISINI !!Pastikan sintaks betul dan jangan lupa tambah koma bila salin tu .
                            [0, 0, 0, 0, 0, 9, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 9]]


print(f"Maka determinan A ialah : {det(Matriks_10x10)}")
print(f"Maka determinan A transpos ialah : {det(Matriks_10x10_transpos)}")
##ADAKAH OUTPUT DIATAS SAMA ??##)

#Q1, vi
# Kita cari songsang matriks A dulu pakai program baru.

import numpy as np
from scipy.linalg import inv

# Fungsi untuk mengira determinan matriks secara fungsi lelaran
def determinan(matriks):
    if len(matriks) == 1:
        return matriks[0][0]
    else:
        hasil_determinan = 0
        for i in range(len(matriks)):
            kofaktor = (-1)**i * determinan([baris[:i] + baris[i+1:] for baris in matriks[1:]])
            hasil_determinan += matriks[0][i] * kofaktor
        return hasil_determinan

# Tetapkan matriks A
A = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [3, 0, 2, 0, 0, 0, 0, 0, 0, 0],
               [4, 1, 0, 3, 0, 0, 0, 0, 0, 0],
               [5, 0, 7, 0, 7, 0, 0, 0, 0, 0],
               [4, 0, 6, 0, 0, 9, 0, 0, 0, 0],
               [5, 0, 0, 0, 0, 0, -1, 0, 0, 0],
               [7, 8, 0, 0, 9, 0, 0, 4, 0, 0],
               [9, 0, 0, 0, 0, 0, 0, 0, 3, 0],
               [10, 0, 0, 3, 0, 0, 0, 0, 0, 9]])

try:
    # Kira songsang matriks A
    songsang_A = inv(A)

    # Cetak matriks songsang
    print("Songsang matriks A:")
    print(songsang_A)

    # Periksa jika songsang wujud (jika det(A) adalah 0,tiada songsang !!)
    if np.linalg.det(A) == 0:
        print("Amaran: Determinan A adalah 0, bermakna songsang mungkin tidak tepat.")
    else:
        # Kira songsang dari determinan A
        songsang_det_A = 1 / np.linalg.det(A)

        print(f"Determinan matriks 1/A ialah: {1/np.linalg.det(A)}")
        print(f"Determinan songsangan matriks A ialah: {songsang_det_A}")
except Exception as ralat:
    print("Ralat: Tidak dapat mencari songsang matriks A.")
    print(ralat)

##Perhatikan jikalau outputnya sama .

#Q1, vii
import numpy as np

# Tetapkan matriks A berukuran 10x10
A = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [3, 0, 2, 0, 0, 0, 0, 0, 0, 0],
               [4, 1, 0, 3, 0, 0, 0, 0, 0, 0],
               [5, 0, 7, 0, 7, 0, 0, 0, 0, 0],
               [4, 0, 6, 0, 0, 9, 0, 0, 0, 0],
               [5, 0, 0, 0, 0, 0, -1, 0, 0, 0],
               [7, 8, 0, 0, 9, 0, 0, 4, 0, 0],
               [9, 0, 0, 0, 0, 0, 0, 0, 3, 0],
               [10, 0, 0, 3, 0, 0, 0, 0, 0, 9]])

# Pilih baris untuk dimodifikasi (i dan k, dalam hal ini)
i = 1
k = 5

# Tetapkan pemalar a (dalam hal ini, 1)
a = 1

# Cipta matriks A' yang telah dimodifikasi
A_prime = A.copy()
A_prime[i] += a * A_prime[k]

# Kira determinan matriks A dan A'
det_A = np.linalg.det(A)
det_A_prime = np.linalg.det(A_prime)

# Bandingkan determinan
if np.isclose(det_A, det_A_prime):
  print(f"Berjaya sepadan! det(A) = {det_A} dan det(A') = {det_A_prime}")
else:
  print("Ralat: Nilai determinan tidak sepadan. Sila periksa kod.")
