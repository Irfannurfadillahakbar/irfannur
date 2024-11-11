# Nama : Argyre Anggawijaya
# NIM : 2403010191
# Program untuk memotong substring dari sebuah kata

def ambil_substring():
    kata = input("Masukkan kata: ")

    try:
        indeks_awal = int(input("Masukkan indeks awal: "))
        indeks_akhir = int(input("Masukkan indeks akhir: "))

        # Memeriksa apakah indeks valid
        if indeks_awal < 0 or indeks_akhir > len(kata) or indeks_awal > indeks_akhir:
            print("Indeks tidak valid. Pastikan indeks awal dan akhir berada dalam rentang yang benar.")
            return
       # Code memotong string
        substring = kata[indeks_awal:indeks_akhir]

        # Menampilkan hasil
        print(f"Substring: {substring}")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk indeks, jangan yang lain :).")

# Memanggil fungsi
ambil_substring()