# Episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++3-----10+++++

inputUser = float(input("Masukan angka kurang dari 3 atau lebih besar dari 10:"))

# +++++3-------------- (kita akan membuat logika kurang dari 3)
# memeriksa angka kurang dari 3
kurangDari = (inputUser < 3)
print("Kurang dari 3 =", kurangDari) # hasilnya True jika kurang dari 3

# ----------10+++++ (kita akan membuat logika lebih dari 10)
# memeriksa angka lebih dari 10
lebihDari = (inputUser > 10)
print("Lebih dari 10 =", lebihDari) # hasilnya True jika lebih dari 10

# kita gabungkan kedua logika yang diatas
correct = kurangDari or lebihDari
print("angka yang anda masukan: ", correct) # jika salah satunya benar maka akan benar dikarekan OR

## KASUS IRISAN
# --------3+++++++++10--------
inputUser = float(input("Masukan angka lebih dari 3 dan kurang dari 10: "))

# ------3+++++++ (kita buat logika lebih dari 3)
lebihDari = (inputUser > 3)
print("Lebih dari 3: ")

# +++++++10--------- (kita buat logika kurang dari 10)
kurangDari = (inputUser < 10)
print("Kurang dari 10: ")

# -------3++++++++10------
correct = lebihDari and kurangDari
print("Masukan angka yang anda masukan: ", correct)
