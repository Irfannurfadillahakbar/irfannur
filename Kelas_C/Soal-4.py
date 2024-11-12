def hitung_vokal(kalimat):
    vokal = "aeiouAEIOU"
    jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)
    return jumlah_vokal

# Input dari pengguna
kalimat = input("Masukkan kalimat: ")
jumlah_vokal = hitung_vokal(kalimat)

print(f"Jumlah huruf vokal dalam kalimat: {jumlah_vokal}")