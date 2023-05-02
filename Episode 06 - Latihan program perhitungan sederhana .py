# Latihan konversi satuan temperature

# program konversi celcius ke satuan lainnya

print("\n PROGRAM KONVERSI TEMPERATUR \n")

# CELCIUS
celcius = float(input("Masukan suhu dalam celcius: "))
print("suhu adalah: ", celcius, "celcius")

# REAMUR
reamur = (4/5) * celcius # 4/5 adalah rumus dari celcius ke reamur dan dikalikan sama nilai dari variabel celcius
print("suhu dalam reamur adalah: ", reamur, "Reamur")

# FAHRENHEIT
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam farenheit adalah: ", fahrenhiet, "Fahrenheit")

# KELVIN
kelvin = celcius + 273
print("suhu dalam kelvin adalah: ", kelvin, "Kelvin")
