# Meminta input dari pengguna
kalimat = input("Masukkan kalimat: ")

# Daftar huruf vokal yang ingin dicari
vokal_dicari = "aiueo"

# Menghitung jumlah kemunculan huruf vokal
hitung_kata = sum(kalimat.lower().count(vokal) for vokal in vokal_dicari)

# Menampilkan hasil
print(f"Huruf vokal 'a', 'i', 'u', 'e' dan 'o' muncul sebanyak {hitung_kata} kali.")