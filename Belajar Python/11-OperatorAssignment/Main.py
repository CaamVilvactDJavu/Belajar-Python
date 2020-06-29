# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 5   # adalah assignment
print("nilai a =", a)
a += 1  # artinya adalah a = a + 1
print("nilai a += 1, nilai a menjadi ", a)
a = 5   # adalah assignment
print("nilai a =", a)
a -= 2  # artinya adalah a = a - 2
print("nilai a -= 2, nilai a menjadi ", a)
a = 5   # adalah assignment
print("nilai a =", a)
a *= 5  # artinya adalah a = a * 2
print("nilai a *= 5, nilai a menjadi ", a)
a = 5   # adalah assignment
print("nilai a =", a)
a /= 2  # artinya adalah a = a / 2
print("nilai a /= 2, nilai a menjadi ", a)

# modulus dan floor division
b = 10
print("\nnilai b =", b)
b %= 3
print("nilai b %= 3, nilai b menjadi", b)
b = 10
print("nilai b =", b)
b //= 2
print("nilai b //= 2, nilai b menjadi", b)
# pangkat atau eksponen
a = 5
print("nilai a =", a)
a **= 3
print("nilai a **= 3, nilai a menjadi", a)

# Operasi Bitwize

# OR
c = True
print("\nnilai c =", c)
c |= False
print("nilai c |= False, nilai c menjadi", c)
c = False
print("nilai c =", c)
c |= False
print("nilai c |= False, nilai c menjadi", c)
# AND
d = True
print("\nnilai d =", d)
d &= False
print("nilai d &= False, nilai d menjadi", d)
d = True
print("nilai d =", d)
d &= True
print("nilai d &= True, nilai d menjadi", d)
# XOR
e = True
print("\nnilai e =", e)
e ^= False
print("nilai e ^= False, nilai e menjadi", e)
e = True
print("nilai e =", e)
e ^= True
print("nilai e ^= True, nilai e menjadi", e)
# geser geser
d = 0b0100
print("\nnilai d =", format(d, '04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi", format(d, '04b'))
d <<= 1
print("nilai d <<= 1, nilai d menjadi", format(d, '04b'))
