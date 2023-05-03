# Episode Operator bitwise, operasi biner, binary

a = 9
b = 5

## bitwise OR (|)
c = a | b
print("===== OR =====")
print('nilai : ', a, ' , binary :', format(a, '08b')) # binary dari 9 adalah 00001001
print('nilai : ', b, ' , binary :', format(b, '08b')) # binary dari 5 adalah 00000101
print('--------------------------(|)')
print('nilai : ', c, ' , binary :', format(c, '08b')) # maka hasilnya adalah 13 dikarenakan binarynya adalah 00001101

## bitwise AND (&)
c = a & b
print("===== AND =====")
print('nilai : ', a, ' , binary :', format(a, '08b'))
print('nilai : ', a, ' , binary :', format(b, '08b'))
print('--------------------------(&)')
print('nilai :', c, ' , binary :', format(c, '08b'))

## bitwise XOR (^)
c = a ^ b
print("===== XOR =====")
print('nilai :', a, ' , binary :', format(a, '08b'))
print('nilai :', b, ' , binary :', format(b, '08b'))
print('-------------------------(^)')
print('nilai :', c, ' , binary :', format(c, '08b'))

## bitwise NOT (~)
c = a ~ b
print("===== NOT =====")
print('nilai :', a, ' , binary :', format(a, '08b'))
print('nilai :', b, ' , binary :', format(b, '08b'))
print('-------------------------(~)')
print('nilai :', c, ' , binary :', format(c, '08b'))

### shifting

# shift right (>>)
c = a >> 2
print("===== >> =====")
print('nilai :', a, ' , binary :', format(a, '08b'))
print('nilai :', b, ' , binary :', format(b, '08b'))
print('------------------(>>)')
print('nilai :', c, ' , binary :', format(c, '08b'))

# shift left (<<)
c = a << b
print("===== << =====")
print('nilai :', a, ' , binary :', format(a, '08b'))
print('nilai :', b, ' , binary :', format(b, '08b'))
print('----------------(<<)')
print('nilai :', c, ' , binary :', format(c, '08b'))
