# Program untuk menghitung jumlah huruf vokal dalam sebuah kalimat

# Meminta pengguna memasukkan kalimat
kalimat = input("Masukkan sebuah kalimat: ")

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf vokal
jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)

# Menampilkan hasil
print("Jumlah huruf vokal dalam kalimat tersebut:", jumlah_vokal)

#Shani_Akhmad_Kalani
#2403010072