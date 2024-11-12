def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

# Input dari pengguna
celcius = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = celcius_ke_fahrenheit(celcius)

print(f"Suhu dalam Fahrenheit: {fahrenheit} °F")