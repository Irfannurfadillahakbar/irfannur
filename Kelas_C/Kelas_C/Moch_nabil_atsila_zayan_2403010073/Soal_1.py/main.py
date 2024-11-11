# Meminta input panjang dan lebar dari user
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

# Menghitung luas dan keliling persegi panjang
luas = panjang * lebar
keliling = 1 * (panjang + lebar)

# Menampilkan hasil
print("Luas persegi panjang:", luas)
print("Keliling persegi panjang:", keliling)

#penjelasan

#program meminta user untuk masukan nilai panjang dan lebar.
#terus,program menghitung luas dan rumus panjang * lebar.
#untuk keliling,  program menggunakan rumus 2 * (panjang + lebar)
#kenapa harus mengunakan rumus 2?
#karena:1). jika kita menjumlahkan panjang lebar 1*, kita hanya mendapatkan total satu sisi panjang dan satu sisi lebar.
        #jadi kita pakai rumus 2 untuk mendapatkan tital keliling.
# hasilnya di tampilkan ke layar.
