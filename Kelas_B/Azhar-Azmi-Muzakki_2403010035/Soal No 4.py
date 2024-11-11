a = input("Masukan Kalimat:")
b = "a,i,u,e,o"

jumlah_huruf = sum(1 for char in a if char in b)

print ("Jumlah Huruf Vokal :", jumlah_huruf)