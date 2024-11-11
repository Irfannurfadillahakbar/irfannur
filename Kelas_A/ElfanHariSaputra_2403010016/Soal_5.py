# Nama: Elfan Hari Saputra
# NIM: 2403010016
# Kelas: TI-A-24
# Deskripsi: Program ini berfungsi untuk memotong substring dari sebuah kata, user diminta untuk input kata, indeks awal, dan indeks akhir

print('--- Memotong Substring dari Sebuah Kata ---') # judul program,cuma layouting :D
print('') # agar ada jarak setelah judul

kata = input("Masukkan kata: ") # input kata
indeksAwal = int(input("Masukkan indeks awal (angka): ")) # input indeks awal
indeksAkhir = int(input("Masukkan indeks akhir (angka): ")) # input indeks akhir
substring = kata[indeksAwal:indeksAkhir] # mengambil substring
print(f"Substring: {substring}") # show hasil
