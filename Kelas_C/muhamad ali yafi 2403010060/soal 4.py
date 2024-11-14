#tugas 4

kata = input("masukan kata = ")

panjangkata = len (kata)
i = 0
jumlahVokal = 0
while i <panjangkata:
    if (kata[i] == "a" or kata[i] == "i" or kata[i] == "u" or kata[i] == "e" or kata[i] == "o") :
        jumlahVokal += 1
        print("jumlah huruf vokal = ", jumlahVokal)