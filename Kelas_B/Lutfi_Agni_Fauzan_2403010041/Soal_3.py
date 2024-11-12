#menggabungkan 2 kata tanpa spasi

#variabel input kata pertama dengan tipe data string
kata_pertama = str(input("masukan kata pertama: "))

#variabel input kata kedua dengan tipe data string
kata_kedua = str(input("masukan kata kedua: "))
#menggabungkan 2 kata menjadi satu 
penggabungan = kata_pertama + kata_kedua

#menggunakan replace untuk menghapus spasi
print("kata pertama=",kata_pertama,"+","kata kedua= ",kata_kedua,"penggabungan",penggabungan.replace(" ",""))