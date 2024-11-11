# masukan suhu dalam celsius: 25
# suhu dalam fahrenheit: 77.0
def celsius_to_fahrenheit(celsius):
    #Conversion and Output
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit

# Input
celsius_input = float(input("masukan suhu dalam Celsius: "))

# Conversion and Output
fahrenheit_output = celsius_to_fahrenheit(celsius_input)
print(f"suhu dalam fahrenheit:{fahrenheit_output}")