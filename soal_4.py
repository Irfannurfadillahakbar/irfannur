kata = input ("masukkan kata: ")

vokal = ["a", "e", "i", "o", "u"]

jumlah_vokal = 0

for huruf in kata:
    if huruf in vokal:
        jumlah_vokal += 1

print ("jumlah huruf vokal: ", jumlah_vokal)