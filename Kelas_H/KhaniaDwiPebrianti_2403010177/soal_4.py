kalimat = input("Masukan kalimat : ")
vokal = 'aiueoAIUEO'

jumlah_vokal = sum(kalimat.count(char) for char in vokal)

# Menampilkan hasil
print(f"Jumlah huruf vokal: {jumlah_vokal}")