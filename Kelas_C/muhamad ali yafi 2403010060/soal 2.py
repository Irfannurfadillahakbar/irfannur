indeks = {   
 "celcius       " : "c",
 "fahrenheit     " : "f"
}

print("==indeks satuan skala suhu==")
for i in indeks:
    print("satuan suhu :", i, "\t indeks :", indeks[i])

suhu = float(input("masukan suhu : "))
satuan = input("masukan indeks satuan skala suhu : ")

if (satuan == "c"):
    print (suhu, "derajat celcius :")
    print ("fahrenheit = ",(suhu*9/5))