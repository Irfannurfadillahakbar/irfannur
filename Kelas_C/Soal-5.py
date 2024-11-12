def potong_substring(kata, awal, panjang):
    substring = kata[awal:awal + panjang]
    return substring

# Input dari pengguna
kata = input("Masukkan kata: ")
awal = int(input("Masukkan indeks awal untuk memotong: "))
panjang = int(input("Masukkan panjang substring: "))

substring = potong_substring(kata, awal, panjang)
print(f"Substring yang dipotong: {substring}")