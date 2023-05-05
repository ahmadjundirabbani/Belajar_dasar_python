# operator dalam bentuk methods

## merubah case pada string

# merubah semua ke upper case
salam = "bro!"
print("normal " + salam)
salam = salam.upper()
print("upper " + salam) # hasilnya akan menjadi BRO!

# merubah semua ke lower case
alay = "aKu KeCe AbieezzZ"
print("normal " + alay)
alay = alay.lower()
print("lower " + alay) # hasilnya akan menjadi aku kece abieezzz

## method is, untuk pengecekan

# contoh isupper()
salam = "SIST"
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper)) # hasilnya akan True
salam = salam.lower()
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper)) # hasilnya akan False

# islower() <- untuk pengecekan apakah lower case semua
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab adn enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case

judul = "It Is Okay To Not Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul)) # hasilnya True dikarenakn setiap awal kata huruf besar

# startswith() dan endswith() <-- keren
cek_start = "Sangjangmin Oppa".startswith("Sangjangmin")
print("Start " + str(cek_start)) # hasilnya True karena kata pertama sama
cek_end = "Sangjangmin Oppa".endswith("Oppak")
print("end " + str(cek_end)) # hasilnya False karena kata terakhir tidak sama

# join() dan split() <-- buat orang males
pisah = ['aku', 'sayang', 'kamu']
gabungan = ' ehm '.join(pisah)
print(pisah) # hasilnya ['aku', 'sayang', 'kamu']
print(gabungan) # hasilnya setiap setelah string akan ada penambahan ehm

gabungan = "naik vespa keliling kota"
pisah = gabungan.split()
print(gabungan) # hasilnya sama saja
print(pisah) # hasilnya akan menjadi ['naik', 'vespa', 'keliling', 'kota']

gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm") # akan menghilangkan kata ehm dan di split
print(gabungan) # hasilnya naikehmvespaehmkelilingehmkota
print(pisah) # hasilnya ['naik', 'vespa', 'keliling', 'kota']

# alokasi karakter

kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
print("'" + kanan + "'") # hasilnya (          kanan) 20 karakter dikurang kanan dan sisanya berada di sebelum kanan

kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
print("'" + kiri + "'") # hasilnya (kiri            ) 20 karakter dikurang kiri dan sisanya berada di sesudah kiri

tengah = "tengah".center(20) # rata tengah dengan 20 karakter 
print("'" + tengah + "'") # hasilnya (     tengah     ) 20 karakter dikurang tengah dan sisanya berada di sebelum dan sesudah dibagi rata

tengah = "tengah".center(20, '-') # rata tengah dengan 2- karakter
print("'" + tengah + "'") # hasilnya (-------tengah-------) 20 karakter dikurang tengah dan sisanya berada di sebelum dan sesudah dibagi rata menggunakan simbol yg diinginkan

# kebalikan dari alokasi karakter
kanan = kanan.strip()
print("'" + kanan + "'") # menghilangkan alokasi kanan sebelumnya menjadi "kanan"
tengah = tengah.strip('-')
print("'" + tengah + "'") # menghilangkan alokasi tengah (-) sebelumnya menjadi "tengah"
