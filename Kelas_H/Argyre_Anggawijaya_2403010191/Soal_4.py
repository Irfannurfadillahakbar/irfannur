# Nama : Argyre Anggawijaya
# NIM : 2403010191
# Program untuk menghitung jumlah huruf vokal dalam kalimat

def hitung_jumlah_vokal():
    kalimat = input("Masukkan kalimat: ")

    # Memeriksa apakah input tidak kosong
    if not kalimat:
        print("Kalimat tidak boleh kosong ya, yang kosong hanya hatiku aja. Jadi harap masukan kalimat.")
        return
     # Mengihtung Huruf Vokal   
    vokal = 'aeiouAEIOU'
    jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)

    # Menampilkan hasil
    print(f"Jumlah huruf vokal dalam kalimat: {jumlah_vokal}")

# Memanggil fungsi
hitung_jumlah_vokal()