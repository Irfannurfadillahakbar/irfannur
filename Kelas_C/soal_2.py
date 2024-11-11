soal_2.py
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
celsius_temp = float(input("Masukan suhu dalam Celsius: "))
fahrenheit_temp = float(input("Masukan suhu dalam Fahrenheit: "))
print(f"{celsius_temp}°C = {celsius_to_fahrenheit(celsius_temp)}°F")
print(f"{fahrenheit_temp}°F = {fahrenheit_to_celsius(fahrenheit_temp)}°C")
hasilnya
Masukan suhu dalam Celsius: 25
Masukan suhu dalam Fahrenheit: 86
25.0°C = 77.0°F
86.0°F = 30.0°C
