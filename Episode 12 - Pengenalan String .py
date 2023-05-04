data = "ini adalah string"
print(data, type(data))

## 1. cara membuat string
'''
  1. dengan menggunakan single quote '...'
  2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote'
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

## 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Jundi")

# tab
print("jundi\t\t\budi, semakin jauhan") # tulisan antara jundi akan di tab sebanyak 2 kali

# backspace
print("jundi \bbudi, jadi deket") # tulisan sebelum \b akan dihapus, jadinya jundibudi

# newline
print("baris pertama. \nbaris kedua.") # LF -> line feed = untuk unix, macos, linux
print("baris pertama. \rbaris kedua.") # CR -> carriage return = untuk commodore, acorn, lisp
print("baris pertama. \r\nbaris kedua.") # CRLF -> line feed carriage return = dipakai oleh windows

## 3. String literal atau raw

# hari-hati
print('C:\new folder') # akan salah pathnya dikarenakn \n adalah newline

# menggunakan raw string
print(r'C:\new folder') # menggunakan r sebelum string akan menjadi raw

# multiline literal string
print("""
Nama  : jundi
Kelas : Kuliah
""")

# multiline literal string dan raw
print(r"""
Nama  : Jundi
Kelas : Kuliah
Instagram : https://www.instagram.com/arabbani09/
""")
