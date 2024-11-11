#Sony Gunawan TI A 24
#memotong substring dari sebuah kata
kata = input("masukan kata")

#inisialisasi indeks awal dan akhir
indeks_awal = int(input("masukan indeks awal: "))
indeks_akhir = int(input("masukakn indeks akhir: "))

#substring
substring = kata [indeks_awal:indeks_akhir]
#menampilkan hasil subustring
print(f"substring dari indeks {indeks_awal} hingga {indeks_akhir} adalah: {substring}")