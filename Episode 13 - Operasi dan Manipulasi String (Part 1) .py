## Operasi dan Memanipulasi String

# 1. Menyambung String (concatenate)
nama_pertama  = "Ahmad"
nama_tengah   = "Jundi"
nama_akhir    = "Rabbani"

nama_lengkap  = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap) # hasilnya tidak ada spaci dikarenakan tidak ada tambahan dari nama_lengkapnya ataupun dari nama_pertama, nama_tengah dan nama_akhir

nama_lengkap  = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap) # hasilnya ada spaci setiap digabungkan

# 2. Menghitung panjang string
panjang = len(nama_lengkap) # akan menghitung panjang setiap karakter dari nilai nama_lengkap
print("panjang " + nama_lengkap + " adalah " + str(panjang))

# 3. Operator untuk string

# cek apakah ada komponen pada sebuah string
d = "d"
status = d in nama_lengkap
print("apakah ", + d + " ada di " + nama_lengkap + ", " + str(status))

D = "d"
status = D in nama_lengkap
print("apakah " + D + " ada di " + nama_lengkap + ", " + str(status))

x = "x"
status = x not in nama_lengkap
print("apakah " + x " tidak ada di " + nama_lengkap + ", " str(status))

# mengulang string
print("wk"*100)
print(100*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0]) # klo index dimulai dari 0
print("index ke-6 : " + nama_lengkap[6]) # index bebas
print("index ke-(-1) : " + nama_lengkap[-1]) # index nya mulai dari belakang
print("index ke-[6,8] : " + nama_lengkap[6:8]) # dimulai dari index 6 sampai sebelum 8
print("index ke-[0,2,4,6,8] : " + nama_lengkap[0:10:2]) # diambil index 0,2,4,6,8 (maksudnya 0 itu awalnya 10 panjangnya 2 itu membaginya)

# item paling kecil
print("nilai terkecil : " + min(nama_lengkap))

# item paling besar
print("nilai terbesar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII number dari spaci : " + str(ascii_code))
data = 117
print("Character dari ascii code 117 : " + chr(data))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o di " + data + " : " + str(jumlah)) # menghitung karakter o di data tersebut
