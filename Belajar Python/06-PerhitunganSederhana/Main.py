# Latihan konversi satuan temperature

# program konversi celcius ke satuan yang lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input("Masukkan Suhu Dalam Celcius = "))
print("suhu adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu adalah", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu adalah", kelvin, "Kelvin")

# program konversi fahrenheit ke kelvin

fahrenheit = float(input("Masukkan Suhu Dalam Fahrenheit = "))
print("suhu adalah", fahrenheit, "Fahrenheit")

kelvin = (fahrenheit-32) * (5 / 9) + (5463 / 20)
print("suhu dalam", kelvin, "Kelvin")

# program konversi kelvin ke fahrenheit

kelvin = float(input("Masukkan Suhu Dalam Kelvin = "))
print("suhu adalah", kelvin, "Kelvin")

fahrenheit = (kelvin-(5463 / 20)) * (9 / 5) + 32
print("suhu dalam", fahrenheit, "Fahrenheit")
