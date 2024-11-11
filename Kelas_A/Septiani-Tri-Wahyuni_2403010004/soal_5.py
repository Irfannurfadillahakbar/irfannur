# Septiani Tri Wahyuni
# 2403010004
# Kelas A
# Memotong Substring dari Sebuah Kata

# input kata
kata = input("Masukkan kata: ")

# input indeks awal dan akhir
awal = int(input("Masukkan indeks awal: "))
akhir = int(input("Masukkan indeks akhir: "))

# memotong substring dari kata
substring = kata[awal:akhir]

# output substring
print("Substring dari kata adalah:", substring)