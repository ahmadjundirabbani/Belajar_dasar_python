## Operasi logika atau boolean

# not, or, and, xor

## NOT
print("===== NOT =====")
a = False
c = not a
print('data a = ', a) # a adalah False
print('----------- NOT')
print('data c = ', c) # maka jawaban dari c adalah True

## OR (jika salah satu true, maka hasilnya adalah true)
print("==== OR ====")
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c) # dikarenakan a dan b False maka c adalah False juga

a = False
b = True
c = a or b
print(a, 'OR', b, '=', c) # dikarenakan salah satunya ada True maka akan True jawabannya

a = True
b = True
c = a or b
print(a, 'OR', b, '=', c) # Jawabannya sudah pasri True

## AND (jika dua buah nilainya True, maka hasilnya True)
print("==== AND ====")
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c) # hasilnya False

a = False
b = True
c = a and b
print(a, 'AND', b, '=', c) # hasilnya False karena keduanya tidak True

a = True
b = True
c = a and b
print(a, 'AND', b, '=', c) # hasilnya True dikarenakan keduanya True

## XOR (akan True jika salah satu True, sisanya false dan jika keduanya True maka akan False)
print("==== XOR ====")
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c) # hasilnya False

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c) # hasilnya True dikarenakan salah satunya True

a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c) # hasilnya False dikarenakan keduanya True
