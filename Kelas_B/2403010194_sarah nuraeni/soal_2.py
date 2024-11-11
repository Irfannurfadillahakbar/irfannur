#Nama       : Sarah nuraeni
#NIM        : 2403010194
#Deskrifsi  : Program ini meminta pengguna untuk mengkonversikan suhu dari celcius ke fahrenheit

def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

celcius = float(input("masukkan suhu dalam celcius: "))
fahrenheit = celcius_to_fahrenheit(celcius)
print(f"{celcius} derajat celcius = {fahrenheit} derajat fahrenheit")


