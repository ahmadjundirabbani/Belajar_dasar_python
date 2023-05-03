# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # adalah assignment
print('nilai a =', a)

a += 1 # artinya adalah a = a + 1
print('nilai a += 1, nilai a menjadi', a)

a -= 2 # artinya adalah a = a - 2
print('nilai a -= 2, nilai a menjadi', a)

a *= 5 # artinya adalah a * 5
print('nilai a *= 5, nilai a menjadi', a)

a /= 2 # artinya adalah a = a / 2
print('nilai a /= 2, nilai a menjadi', a)

b = 10
print('nilai b =', b)

# modulus dan floor division
b %= 3
print('nilai b %= 3, nilai b menjadi', b)

b = 10
print('nilai b =', b)

b //= 3
print('nilai b //= 3, nilai b menjadi', b)

# pangkat atau eksponen
a = 5
print('nilai a =', a)

a **= 3
print('nilai a **= 3, nilai a menjadi', a)

# operasi bitwise
# OR
c = True
print('nilai c =', c)
c |= False
print('nilai c |= False, nilai c menjadi', c) # dikarenakan salah satu nilai c True maka hasilnya True
c = False
print('nilai c =', c)
c |= False
print('nilai c |= False, nilai c menjadi', c) # dikarenakan semua nilai c False maka hasilnya False

## AND (jika semuanya True maka True selainnya False)
c = True
print('nilai c =', c)
c &= False
print('nilai c &= False, nilai c menjadi', c) # dikarenakan semuanya False maka hasilnya False
c = True
print('nilai c =', c)
c &= True
print('nilai c &= True, nilai c menjadi', c) # dikarenakn semuanya True maka hasilnya True

## XOR (jika salah satunya True maka hasilnya True, dan selainnya False)
c = True
print('nilai c =', c)
c ^= False
print('nilai c ^= False, nilai c menjadi', c)
c = True
print('nilai c =', c)
c ^= True
print('nilai c ^= True, nilai c menjadi', c)

## geser geser
d = 0b0100
print('nilai d =', format(d, '04b')) # nilai binary d 0100
d >>= 2
print('nilai d >>= 2, nilai d menjadi', format(d, '04b')) # binary d bergeser ke kanan 2 menjadi 0001
d <<= 1
print('nilai d <<= 1, nilai d menjadi', format(d, '04b')) # binary d bergeser ke kiri 1 menjadi 0010
