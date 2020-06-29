# Operasi Komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih dari (>)
print("=============== lebih dari (>)")
hasil = a > 5
print(a, ">", 5, "=", hasil)
hasil = b > 1
print(b, ">", 1, "=", hasil)
hasil = a > 4
print(a, ">", 4, "=", hasil)

# kurang dari (<)
print("=============== kurang dari (<)")
hasil = a < 5
print(a, "<", 5, "=", hasil)
hasil = b < 1
print(b, "<", 1, "=", hasil)
hasil = a < 4
print(a, "<", 4, "=", hasil)

# lebih dari sama dengan (>=)
print("=============== lebih dari sama dengan (>=)")
hasil = a >= 5
print(a, ">=", 5, "=", hasil)
hasil = b >= 1
print(b, ">=", 1, "=", hasil)
hasil = a >= 4
print(a, ">=", 4, "=", hasil)

# kurang dari sama dengan (<=)
print("=============== kurang dari sama dengan (<=)")
hasil = a <= 5
print(a, "<=", 5, "=", hasil)
hasil = b <= 1
print(b, "<=", 1, "=", hasil)
hasil = a <= 4
print(a, "<=", 4, "=", hasil)

# sama dengan (==)
print("=============== sama dengan (==)")
hasil = a == 4
print(a, "==", 4, "=", hasil)
hasil = b == 4
print(b, "==", 4, "=", hasil)

# tidak sama dengan (!=)
print("=============== tidak sama dengan (!=)")
hasil = a != 4
print(a, "!=", 4, "=", hasil)
hasil = b != 4
print(b, "!=", 4, "=", hasil)

# 'is' sebagai komparasi object identity
print("=============== object identity (is)")
x = 5  # ini adalah assignment membuat object
y = 5
print("nilai x = ", x, ",id = ", hex(id(x)))
print("nilai y = ", y, ",id = ", hex(id(y)))
hasil = x is y
print("x is y = ", hasil)
x = 5  # ini adalah assignment membuat object
y = 6
print("nilai x = ", x, ",id = ", hex(id(x)))
print("nilai y = ", y, ",id = ", hex(id(y)))
hasil = x is y
print("x is y = ", hasil)

# 'is not' sebagai komparasi object identity
print("=============== object identity (is not)")
x = 5  # ini adalah assignment membuat object
y = 5
print("nilai x = ", x, ",id = ", hex(id(x)))
print("nilai y = ", y, ",id = ", hex(id(y)))
hasil = x is not y
print("x is not y = ", hasil)
x = 5  # ini adalah assignment membuat object
y = 6
print("nilai x = ", x, ",id = ", hex(id(x)))
print("nilai y = ", y, ",id = ", hex(id(y)))
hasil = x is not y
print("x is not y = ", hasil)
