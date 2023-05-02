## Casting adalah merubah dari suatu tipe data ke tipe data lainnya

# tipe data : 1. integer ditulis dalam codingan int
              2. float ditulis dalam codingan float
              3. string ditulis dalam codingan str
              4. booelan ditulis dalam codingan bool

## INTEGER
print("=====INTEGER=====")
data_int = 9;
print("data = ", data_int, ", type = ", type(data_int))

data_flaot  = float(data_int)
data_str    = str(data_int)
data_bool   = bool(data_int) # akan false jika nilai int = 0
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

## FLOAT
print("=====FLOAT=====")
data_float = 1.5; # komanya menggunakan tanda (.) bukan koma pada umumnya seperti (,)
print("data = ", data_float, ", type = ", type(data_flaot))

data_int = int(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

## BOOLEAN
print("=====BOOLEAN=====")
data_bool = True;
print("data = ", data_bool, ", type = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_float, ", type = ", type(data_float))

## STRING
print("=====STRING=====")
data_str = "10";
print("data = ", data_str, ", type = ", type(data_str))

data_int = int(data_str) # string harus angka
data_float = float(data_str) # string harus angka
data_bool = bool(data_str) # false jika string kosong
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_bool, ", type = ", type(data_bool))
