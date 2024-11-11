# Meminta input kalimat dari pengguna
kalimat=input("masukkan kalimat:")
# Daftar huruf vokal
vokal="aiueoAIUEO"
# Menghitung jumlah huruf vokal
jumlah_vokal=sum(1 for huruf in kalimat if huruf in vokal)
# Menampilkan hasil
print("jumlah huruf vokal",jumlah_vokal)