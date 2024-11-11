# Meminta input dari pengguna
kalimat = input("Masukkan kalimat: ")

# Mendefinisikan huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf vokal
jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)

# Menampilkan hasil
print("Jumlah huruf vokal:", jumlah_vokal)
