# memotong substring dari sebuah kalimat
kata = input("masukkan kata: ")
indeks_awal = int(input("masukkan indeks awal: "))
indeks_akhir = int(input("masukkan indeks akhir: "))
substring = kata[indeks_awal:indeks_akhir]
print(f"Substring: {substring}")
