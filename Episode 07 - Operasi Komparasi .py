## operasi komparasi 

# setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari >
print("===== Lebih besar dari (>) =====")
hasil = a > 3
print(a, '>', 3, '=', hasil)

hasil = b > 3
print(b, '>', 3, '=', hasil)

hasil = b > 2
print(b, '>', 2, '=', hasil)

# Kurang dari <
print("===== Kurang dari (<) =====")
hasil = a < 3
print(a, '<', 3, '=', hasil)

hasil = b < 3
print(b, '<', 3, '=', hasil)

hasil = b < 2
print(b, '<', 2, '=', hasil)

# Lebih dari sama dengan >=
print("===== Lebih dari sama dengan (>=) =====")
hasil = a >= 3
print(a, '>=', 3, '=', hasil)

hasil = b >= 3
print(b, '>=', 3, '=', hasil)

hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# Kurang dari sama dengan <=
print("====== Kurang dari sama dengan (<=) =====")
hasil = a <= 3
print(a, '<=', 3, '=', hasil)

hasil = b <= 3
print(b, '<=', 3, '=', hasil)

hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# Sama dengan ==
print("====== Sama dengan (==) =====")
hasil = a == b
print(a, '==', b, '=', hasil)

hasil = a == 4
print(a, '==', 4, '=', hasil)

# tidak sama dengan !=
print("===== Tidak sama dengan (!=) =====")
hasil = a != b
print(a, '!=', b, '=', hasil)

hasil = a != 4
print(a, '!=', 4, '=', hasil)

## 'is' sebagai komparasi object identity
print("===== Object Identity (is) =====")
x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =', x, ', id = ', hex(id(x)))
print('nilai y =', y, ', id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil) # maka akan menghasilkan False dikarenakan nilai x bukan y

x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =', x, ', id = ',hex(id(x)))
print('nilai y =', y,' , id = ',hex(id(y)))
hasil = x is y
print('x is y =', hasil) # makan akan menghasilkan True dikarenakan nilai x sama dengan y

## 'is not' sebagai komparasi object identity
print("===== Object Identity (is not) =====")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =', x, ', id = ', hex(id(x)))
print('nilai y =', y, ', id = ', hex(id(y)))
hasil = x is not y
print('x is y =', hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =', x, ' ,id = ', hex(id(x)))
print('nilai y =', y, ', id = ', hex(id(y)))
hasil = x is not y
print('x is y =', hasil)
