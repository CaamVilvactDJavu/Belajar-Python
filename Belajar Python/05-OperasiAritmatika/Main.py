# Operasi Aritmatika

# operasi penjumlahan (+)
a = 10
b = 3
hasil = a+b
print(a, "+", b, "=", hasil)

# operasi pengurangan (-)
a = 10
b = 3
hasil = a-b
print(a, "-", b, "=", hasil)

# operasi perkalian (*)
a = 10
b = 3
hasil = a*b
print(a, "*", b, "=", hasil)

# operasi pembagian (/)
a = 10
b = 3
hasil = a/b
print(a, "/", b, "=", hasil)

# operasi modulus (%)
a = 10
b = 3
hasil = a % b
print(a, "%", b, "=", hasil)

# operasi eksponen / pangkat (**)
a = 10
b = 3
hasil = a**b
print(a, "**", b, "=", hasil)

# operasi floor devision (//) dibulatkan ke bawah
a = 10
b = 3
hasil = a//b
print(a, "//", b, "=", hasil)


# prioritas operasi
'''
    1. ()
    2. exponen **
    3. pekalian dan teman teman * / ** % //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil = x + y * z
print(x, "+", y, "*", z, "=", hasil)
hasil = (x + y) * z  # kurung akan didulukan
print("(", x, "+", y, ")", "*", z, "=", hasil)
