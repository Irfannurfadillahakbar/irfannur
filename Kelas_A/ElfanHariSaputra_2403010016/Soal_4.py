# Nama: Elfan Hari Saputra
# NIM: 2403010016
# Kelas: TI-A-24
# Deskripsi: Program ini berfungsi untuk menghitung jumlah huruf vokal dalam sebuah kalimat, user diminta untuk input kalimat

print('--- Menghitung Jumlah Huruf Vokal dalam Kalimat ---') # judul program,cuma layouting :D
print('') # agar ada jarak setelah judul

kalimat = input("Masukkan kalimat (kecil semua yaa!): ") # input kalimat
vokal = 'aeiou' # deklarasikan yg termasuk huruf vokal

jumlah_a = kalimat.count('a') # hitung jumlah huruf a
jumlah_i = kalimat.count('i') # hitung jumlah huruf i
jumlah_u = kalimat.count('u') # hitung jumlah huruf u
jumlah_e = kalimat.count('e') # hitung jumlah huruf e
jumlah_o = kalimat.count('o') # hitung jumlah huruf o

jumlahVokal = jumlah_a + jumlah_i + jumlah_u + jumlah_e + jumlah_o # hitung jumlah huruf vokal
print(f"Jumlah huruf vokal: {jumlahVokal}") # show hasil
