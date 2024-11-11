# Fungsi untuk mengonversi suhu dari Celcius ke Fahrenheit
def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * (9/5)) + 32
    return fahrenheit

# Meminta input dari pengguna
try:
    celcius_input = float(input("Masukkan suhu dalam Celcius: "))
    fahrenheit_output = celcius_to_fahrenheit(celcius_input)
    print(f"Suhu dalam Fahrenheit: {fahrenheit_output:.1f}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka yang valid.")