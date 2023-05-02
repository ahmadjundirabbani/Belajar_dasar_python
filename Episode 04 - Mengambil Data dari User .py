# Input adalah mengambil data dari user ketika memasukan data tersebut

# data yang dimasukan berupa string
data = input("Masukan data: ")

print("data: ", data, ", type: ", type(data))

# jika kita ingin mengambil data integer ataupun float
integer = int(input("Masukan angka: "))
data = float(input("Masukan angka: "))
print("data: ", integer, ", type: ", type(integer))
print("data: ", data, ", type: ", type(data))

# bagaimana dengan boolean
biner = bool(int(input("Masukan nilai boolean: ")))

print("data: ", biner, ", type: ", type(biner))
