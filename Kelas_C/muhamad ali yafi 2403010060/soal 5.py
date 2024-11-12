#tugas 5
word=input("masukkan kata: ")
start_indeks=int(input("masukkan indeks awal:"))
end_indeks=int(input("  masukkan indeks akhir:"))

substring=word[start_indeks:end_indeks]
print(f"substring: {substring}")