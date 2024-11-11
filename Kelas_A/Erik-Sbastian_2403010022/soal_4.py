# Erik Sbastian TI 24 A
# NIM: 2403010022

# Menghitung jumlah huruf vokal dari kalimat

# input kalimat
kalimat = input("Masukkan kalimat: ")

# inisialisai huruf vokal
vokal = "aiueoAIUEO"

# Menghitung huruf vokal 
jumlah_vokal = sum(1 for char in kalimat if char in vokal)

# menampilkan hasil
print("Jumlah huruf vokal di dalam kalimat:", jumlah_vokal)