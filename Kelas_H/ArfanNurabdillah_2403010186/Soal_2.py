# Fungsi untuk mengonversi suhu dari Celcius ke Fahrenheit
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

# Input suhu dalam Celcius
celcius = float(input("Suhu dalam Celcius: "))

# Mengonversi suhu ke Fahrenheit
fahrenheit = celcius_ke_fahrenheit(celcius)

# Output suhu dalam Fahrenheit
print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f}")
