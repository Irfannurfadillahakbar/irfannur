#Muhamad Khalif Shiddiq Saputra
#NIM: 2403010003 / TI 2024 A
#program yang meminta pengguna untuk memasukkan sebuah kalimat, lalu menghitung dan menampilkan jumlah huruf vokal (a, e, i, o, u) di dalam kalimat tersebut.
kalimat = input("Masukkan kalimat: ")

vokal = "aiueoAIUEO"

jumlah_vokal = sum(1 for char in kalimat if char in vokal)

print("Jumlah huruf vokal:", jumlah_vokal)