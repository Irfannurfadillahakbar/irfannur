# Meminta input dari pengguna
kata = input("Masukkan kata: ")
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring berdasarkan indeks yang diberikan
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil substring
print("Substring yang diambil dari indeks", indeks_awal, "hingga", indeks_akhir, "adalah:", substring)
                # penjelasan
    # 1).input kata: program akan minta untuk memasukan kata (string)
    # 2).indeks awal dan indeks akhir:program akan untuk memasukan dua angka bulat yaitu indeks awal dan indeks akhir(integer)
    # 3).slicing string: dengan menggunakan syntax kata["indeks_awal:indeks_akhir"],program akan mengambil substring dari indeks awal dan akhir(indeks akhir tdk termasuk)
    # 4).output program akan menampilkan substring yg di ambil. 
    
                    # contoh pengguanaan
        # masukan kata:"algoritma"
        # masukan indeks awal:"2"
        # masukan indeks akhir:"6"
        # substring yg di ambil dari indeks 2 hingga 6 adalah:"gori"