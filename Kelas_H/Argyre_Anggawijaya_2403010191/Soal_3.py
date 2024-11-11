# Nama : Argyre Anggawijaya
# NIM : 2403010191
# Program ini menggabungkan dua kata menjadi satu string tanpa spasi

def gabungkan_kata():
    kata_pertama = input("Masukkan kata pertama: ")
    kata_kedua = input("Masukkan kata kedua: ")

    # Memeriksa apakah input ada atau tidak kosong
    if not kata_pertama or not kata_kedua:
        print("Kedua kata harus diisi. Harap masukkan kata.")
        return

    # Menggabungkan kedua kata
    hasil_gabungan = kata_pertama + kata_kedua

    # Menampilkan hasil
    print(f"Hasil penggabungan: {hasil_gabungan}")

# Memanggil fungsi
gabungkan_kata()