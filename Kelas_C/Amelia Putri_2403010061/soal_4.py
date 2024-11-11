# soal 4: menghitung jumlah huruf vocal dalam kalimat
kalimat = input("masukkan kalimat: ")
vocal = "aeiouAEIOU"
jumlah_vocal = sum(1 for huruf in kalimat if huruf in vocal)
print(f"jumlah huruf vocal: {jumlah_vocal}")
