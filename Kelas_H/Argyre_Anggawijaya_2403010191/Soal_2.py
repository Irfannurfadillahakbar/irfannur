# Nama : Argyre Anggawijaya
# NIM : 2403010191
# Program ini mengonversi suhu dari Celcius ke Fahrenheit

def konversi_suhu():
    try:
        celcius = float(input("Masukkan suhu dalam Celcius: "))

        # Menghitung suhu dalam Fahrenheit
        fahrenheit = (celcius * 9/5) + 32

        # Menampilkan hasil
        print(f"Suhu dalam Fahrenheit adalah: {fahrenheit:.2f}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

# Memanggil fungsi
konversi_suhu()