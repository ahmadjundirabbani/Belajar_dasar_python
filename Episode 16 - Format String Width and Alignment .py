# Width and Multiline

# Data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(5*"=" + " Data String " + 5*"=")
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print("\n" + 5*"=" + " Data String " + 5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n" + 5*"=" + " Data String " + 5*"=")
print(data_string)

# mengatur lebar
data_nama = "Ucup Surucup"
data_umur = 21
data_tinggi = 105.17
data_nomor_sepatu = 25
data_string = f"""
nama    = {data_nama:>5}
umur    = {data_umur:>5}
tinggi  = {data_tinggi:>5}
sepatu  = {data_nomor_sepatu:>5}
"""
print("\n" + 5*"=" + " Data String " + 5*"=")
print(data_string)
