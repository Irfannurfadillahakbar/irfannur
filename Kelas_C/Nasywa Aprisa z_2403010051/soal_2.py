#masukan suhu dalam celcius: 25
#suhu dalam fahrenheit: 77.0
def celcius_to_fahrenheit(celcius):
    #conversion and output
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

#input
celcius_input = float(input("masukan suhu dalam celcius: "))

#conversion and output
fahrenheit_output = celcius_to_fahrenheit(celcius_input)
print(f"suhu dalam fahrenheit: {fahrenheit_output}")

