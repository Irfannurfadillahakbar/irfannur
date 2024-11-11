# Nama: Elfan Hari Saputra
# NIM: 2403010016
# Kelas: TI-A-24
# Deskripsi: Program ini mengonversi suhu dari Celcius ke Fahrenheit berdasarkan suhu celcius yang diinput oleh user

print('--- Konversi Suhu Celcius ke Fahrenheit ---') # judul program, cuma layouting :D
print('') # agar ada jarak setelah judul

celcius = float(input("Berapa suhu dalam Celcius nya?: ")) # input suhu dalam Celcius
fahrenheit = (celcius * 9 / 5) + 32 # menghitung suhu dalam Fahrenheit
print(f"Suhu dalam Fahrenheit adalah: {fahrenheit}") # menampilkan hasil
