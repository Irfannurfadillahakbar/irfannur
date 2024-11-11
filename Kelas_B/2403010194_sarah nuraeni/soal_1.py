#Nama       : Sarah nuraeni
#NIM        : 2403010194
#Deskrifsi  : Program ini meminta pengguna untuk memasukkan panjang dan luas persegi panjang lalu meghitung dan menampilkan luas dan keliling persegi panjang


print("menghitung luas & keliling persegi panjang")

p = float(input('masukkan nilai panjang : '))
l = float(input('masukkan nilai lebar   : '))

luas = p*l
keliling = 2*(p+l)
print('luasnya ', str(luas))
print('kelilingnnya', str(keliling))