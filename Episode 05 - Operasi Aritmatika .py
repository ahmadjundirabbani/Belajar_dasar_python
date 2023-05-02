# Operasi matematika adalah cara untuk menghitung atau memanipulasi angka atau variabel matematika. 
# Contohnya adalah penjumlahan, pengurangan, perkalian, pembagian, pangkat, dan akar.

a = 20 # variabel a mempunyai nilai 20
b = 3 # variable b mempunyai nilai 3

# operasi tambah tandanya (+)
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi pengurangan tandanya (-)
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi perkalian tandanya (*)
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi pembagian tandanya (/)
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponen pangkat tandanya (**)
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi modulus atau biasanya mod tandanya (%)
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor division tandanya (//)
hasil = a // b
print(a, '//', b, '=', hasil)

## Prioritas operasi, operational precedence
'''
  1. ()
  2. exponen tandanya (**)
  3. perkalian dan teman-teman tandanya (*), (%), (/), (//)
  4. pertambahan dan pengurangan tandanya (+), (-)
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x, '**', y, '*', (z + x), '/', y, '-', y, '%', z, '//', x, '=', hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z 
print('(',x,'+',y,') *',z,'=',hasil)
