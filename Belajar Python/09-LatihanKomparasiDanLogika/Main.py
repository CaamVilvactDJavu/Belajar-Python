# Latihan Logika dan Komparasi

# Membuat gabungan area rentang dari angka

print("========== GABUNGAN ==========")
# ++++++3------10++++++
inputUser = float(
    input("Masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10 \n= "))

# ++++++3--------------------
# Memeriksa angka kurang dari 3
isKurangDari = inputUser < 3
print(inputUser, "<", "3", "=", isKurangDari)

# ------10++++++
# Memeriksa angka lebih dari 10
isLebihDari = inputUser > 10
print(inputUser, ">", "10", "=", isLebihDari)

# ++++++3------10++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan = ", isCorrect)


print("========== IRISAN ==========")
# ------3++++++10------
# Kasus irisan
inputUser = float(input(
    "Masukkan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10 \n= "))

# ------3++++++
isLebihDari = inputUser > 3
print(inputUser, ">", "3", "=", isLebihDari)

# ++++++10------
isKurangDari = inputUser < 10
print(inputUser, "<", "10", "=", isKurangDari)

# ------3++++++10------
isCorrect = isLebihDari and isKurangDari
print("Angka yang anda masukkan = ", isCorrect)


print("========== LATIHAN 1 ==========")
# ------0++++++5------8++++++11------
# Latihan 1

inputUser = float(input(
    "Masukkan angka yang bernilai \nlebih dari 0 \ndan \nkurang dari 5 \natau \nlebih dari 8 \ndan \nkurang dari 11 \n= "))

# ------0++++++
isLebihDari0 = inputUser > 0
print(inputUser, ">", "0", "=", isLebihDari0)

# ++++++5------
isKurangDari5 = inputUser < 5
print(inputUser, "<", "5", "=", isKurangDari5)

# ------8++++++
isLebihDari8 = inputUser > 8
print(inputUser, ">", "8", "=", isLebihDari8)

# ++++++11------
isKurangDari11 = inputUser < 11
print(inputUser, "<", "11", "=", isKurangDari11)

# ------0++++++5------8++++++11------
isCorrect = (isLebihDari0 and isKurangDari5) or (
    isLebihDari8 and isKurangDari11)
print("Angka yang anda masukkan = ", isCorrect)


print("========== LATIHAN 2 ==========")
# ++++++0------5++++++8------11++++++
# Latihan 2

inputUser = float(input(
    "Masukkan angka yang bernilai \nkurang dari 0 \natau \nkurang dari 5 \ndan \nlebih dari 8 \natau \nkurang dari 11 \n= "))

# ++++++0------
isKurangDari0 = inputUser < 0
print(inputUser, "<", "0", "=", isKurangDari0)

# ------5++++++
isLebihDari5 = inputUser > 5
print(inputUser, ">", "5", "=", isLebihDari5)

# ++++++8------
isKurangDari8 = inputUser < 8
print(inputUser, "<", "8", "=", isKurangDari8)

# ------11++++++
isLebihDari11 = inputUser > 11
print(inputUser, ">", "11", "=", isLebihDari11)

# ++++++0------5++++++8------11++++++
isCorrect = (isKurangDari0 or isLebihDari5) and (
    isKurangDari8 or isLebihDari11)
print("Angka yang anda masukkan = ", isCorrect)
