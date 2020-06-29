data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan senggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar ?"')
print("'Halo, apa kabar ?'")
print("ini adalah hari Jum'at")

# 2. Menggunakan tanda (\)

# membuat tanda (') menjadi string
print('Mari sholat Jum\'at')
print('g\'day, isn\'t it ?')

# backslash
print("C:\\user\\Vilvact")

# tab
print("caam\t\t vilvact, semakin jauh")

# backspace
print("caam  \bvilvact, jadi dekat")

# newline
# # LF -> line feed -> unix, macos, linux
print("baris pertama.\nbaris kedua.")
# CR -> carriage return -> comodore, acorn, lisp
print("baris pertama.\rbaris kedua.")
# CRLF -> line feed carriage return -> windows
print("baris pertama.\r\nbaris kedua.")

# 3. String literal atau raw

# hati-hati
print('C:\\new folder')  # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print(
    """
Nama : Caam
Kelas : XII
    """
)

# multiline literal string dan RAW
print(r"""
Nama : Caam
Kelas : XII SMA
Website : www.caamvilvact.com/newID
""")
