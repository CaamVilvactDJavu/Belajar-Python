# Operator Bitwize, Operasi Biner, Binary

a = 9
b = 5

# Bitwize OR (|)
c = a | b
print("\n======OR======")
print("nilai a = ", a, " binary = ", format(a, "08b"))
print("nilai b = ", b, " binary = ", format(b, "08b"))
print("-----------------------------------------------(|)")
print("nilai c = ", c, "binary = ", format(c, "08b"))

# Bitwize AND (&)
c = a & b
print("\n======AND======")
print("nilai a = ", a, " binary = ", format(a, "08b"))
print("nilai b = ", b, " binary = ", format(b, "08b"))
print("-----------------------------------------------(&)")
print("nilai c = ", c, " binary = ", format(c, "08b"))

# Bitwize XOR (^)
c = a ^ b
print("\n======XOR======")
print("nilai a = ", a, " binary = ", format(a, "08b"))
print("nilai b = ", b, " binary = ", format(b, "08b"))
print("-----------------------------------------------(^)")
print("nilai c = ", c, "binary = ", format(c, "08b"))

# Bitwize NOT (~)
c = ~a
print("\n======NOT======")
print("nilai a = ", a, "  binary = ", format(a, "08b"))
print("-----------------------------------------------(~)")
print("nilai c = ", c, "binary = ", format(c, "08b"))
print("-----------------------------------------------(^)")
d = 0b0000001001
e = 0b1111111111
print("nilai =", e ^ d, "  binary = ", format(e ^ d, "08b"))

# Shifting

# Shift right (>>)
c = a >> 2
print("\n======(>>)======")
print("nilai a = ", a, "  binary = ", format(a, "08b"))
print("-----------------------------------------------(>>)")
print("nilai c = ", c, "  binary = ", format(c, "08b"))

# Shift left (<<)
c = a << 2
print("\n======(<<)======")
print("nilai a = ", a, "  binary = ", format(a, "08b"))
print("-----------------------------------------------(<<)")
print("nilai c = ", c, " binary = ", format(c, "08b"))
