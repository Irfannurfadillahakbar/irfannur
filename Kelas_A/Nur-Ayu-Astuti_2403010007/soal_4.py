# Menghitung Luas dan Keliling Persegi Panjang
# Nur Ayu Astuti TI A 24

# Menghitung Jumlah Huruf Vokal dalam Kalimat

# Input kalimat
kalimat = input("Masukkan kalimat: ")

# Inisialilasi huruf vokal
vokal = "aiueoAIUEO"

# Menghitung Jumlah huruf vokal
jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)

# Menampilkan hasil
print(f"Jumlah huruf vokal dalam kalimat '{kalimat}' adalah {jumlah_vokal}")
