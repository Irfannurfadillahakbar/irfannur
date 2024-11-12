print("\nPROGRAM MEMOTONG SUBSTRING DARI SEBUAH KATA\n")

kalimat = input("Masukkan kalimat yang akan di potong : ")

indeks_awal = int(input("masukkan indeks awal : "))
indeks_akhir = int(input("masukkan indeks akhir : "))

substring = (kalimat [indeks_awal:indeks_akhir])
print("substring hasil : ",substring)
