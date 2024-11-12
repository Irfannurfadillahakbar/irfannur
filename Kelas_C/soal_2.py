# Program untuk mengonversi suhu dari Celcius ke Fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Meminta input suhu dalam Celcius dari pengguna
celsius = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

# Menampilkan hasil konversi
print(f"Suhu dalam Fahrenheit: {fahrenheit} °F")

#Shani_Akhmad_Kalani
#2403010072