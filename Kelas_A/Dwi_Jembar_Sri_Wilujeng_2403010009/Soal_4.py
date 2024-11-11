#Dwi Jembar Sri Wilujeng
#2403010009
#Menghitung jumlah huruf vokal dari kalimat

kalimat = input ("masukkan kalimat: ")

# Imisialisai vokal
vokal = "aiueoAIUEO"

# Menghitung jumlah huruf vokal
jumlah_vokal = sum(1 for char in kalimat if char in vokal)

# Menampilkan hasil
print("Jumlah huruf vokal:", jumlah_vokal)