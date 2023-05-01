## Variabel adalah tempat dimana kita menyimpan data 

# menaru / assignment nilai
a = 10
x = 5
y = 99

# pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai y = ", y)

# penamaan
nilai_y = 15 # jika lebih dari 2 kata maka menggunakan underscore bukan spaci
ribu3 = 3000 # ini boleh tapi tidak boleh diawalin dengan angka
nilaiX = 5 # ini boleh kata kedua dijadikan huruf besar untuk membedakannya

# pemanggilan kedua
print("Nilai a = ", a)
a = 7
print("Nilai a = ", a) # nilai yang akan muncul adalah angka 7, dia akan menimpah nilai sebelumnya

# assignment indirect
b = a
print("Nilai b = ", b) # nilai b akan menjadi variabel a
