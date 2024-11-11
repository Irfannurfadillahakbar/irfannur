kata = input("Masukan kata : ")
index_awal = int(input("Masukan index awal: "))
index_akhir = int(input("Masukan index akhir: "))

substring = kata[index_awal:index_akhir]
print(f"Substring: {substring}")