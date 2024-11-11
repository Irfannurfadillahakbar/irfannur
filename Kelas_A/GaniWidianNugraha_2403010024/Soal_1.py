#Buatlah program yang meminta pengguna untuk memasukkan panjang dan lebar suatu persegi panjang.
# Program harus menghitung dan menampilkan luas dan keliling dari persegi panjang tersebut.

#meminta input dari user
Panjang = float(input("masukan panjang persegi: "))
Lebar = float(input("lebar persegi "))

#prosses menghitung luas dan keliling persegi panjang
Luas = Panjang * Lebar
Keliling = 2 * (Panjang+Lebar)

# output/menampilkan hasil
print(f"Luas persegi panjang:{Luas}")
print(f"keliling persegi panjang:{Keliling}")