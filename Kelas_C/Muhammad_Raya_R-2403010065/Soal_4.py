print("\nPROGRAM MENGHITUNG HURUF VOKAL DALAM KALIMAT\n")

kalimat = input("Masukkan kalimlat : ")
vokal = "aiueo"

hitung_vokal = 0
for huruf in kalimat:
    if huruf.lower() in vokal:
        hitung_vokal += 1

print("Jumlah huruf vokal : ", hitung_vokal)