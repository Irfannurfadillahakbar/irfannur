kata_pertama = input("Masukan kata pertama : ")
kata_kedua = input("Masukan kata kedua : ")

kata_pertama_tanpa_spasi = kata_pertama.replace(" ","")
kata_kedua_tanpa_spasi = kata_kedua.replace(" ","")

print(f"Hasil Penggabungan :", kata_pertama_tanpa_spasi + kata_kedua_tanpa_spasi)