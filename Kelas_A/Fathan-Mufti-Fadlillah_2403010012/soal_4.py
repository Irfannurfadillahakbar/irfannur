# Fathan Mufti Fadlillah
# NIM: 2403010012
# KELAS A

# Menghitung jumlah huruf vokal dalam kalimat
# Meminta pengguna untuk memasukkan kalimat
kalimat = input("Masukkan Kalimat: ")

# Inisialisasi huruf vokal
vokal = "aiueoAIUEO"

# Menghitung jumlah huruf vokal dalam kalimat
jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)

# Menampilkan hasil
print(f"{jumlah_vokal}")