print("Nama : Muhammad Riziq Ramdhani")
print("NIM  : 2403010023")
print("------------------------------------------")

# input kalimat
kalimat = input("Masukkan kalimat: ")

# inisialisai huruf vokal
vokal = "aiueoAIUEO"

# Menghitung huruf vokal 
jumlah_vokal = sum(1 for char in kalimat if char in vokal)

# menampilkan hasil
print("Jumlah huruf vokal di dalam kalimat:",jumlah_vokal)

print("-------------------------------------------")
