# Septiani Tri Wahyuni
# 2403010004
# Kelas A
# Menghitung jumlah huruf vokal

# input kalimat
kalimat = input("Masukkan kalimat: ")

# inisialisasi variabel jumlah huruf vokal
vokal = "aiueoAIUEO"

# Menghitung jumlah huruf vokal
jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)

# output jumlah huruf vokal
print("Jumlah huruf vokal dalam kalimat:", jumlah_vokal)