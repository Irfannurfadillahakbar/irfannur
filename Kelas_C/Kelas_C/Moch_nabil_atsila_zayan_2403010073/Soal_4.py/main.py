# Meminta input dari pengguna(string)
kalimat = input("Masukkan kalimat: ")

# Inisialisasi variabel untuk menghitung jumlah vokal
jumlah_vokal = 0

# Daftar huruf vokal
vokal = "AEIOUaeiou"

# Menghitung jumlah huruf vokal dalam kalimat
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

# Menampilkan hasil
print("Jumlah huruf vokal:", jumlah_vokal)

# contoh output:
# jika pengguna memasukan:
        # "selamat datang di dunia pemrograman"
# maka program akan mengitung total huruf vokal(e,a,a,a,a,i,u,i,a,o,a),dan menghasilkan ouput:
        # "jumlah huruf vokal: 11"

                    # penjelasan 
    # 1).meminta input:
        # program meminta untuk memasukan kalimat dalam bentuk string.
    # 2).inisialisasi varialbel untuk jumlah vokal:
        # "jumlah_vokal" di inisialisasi dengan nilai 0 untuk menyimpan total jumlah huruf vokal. 
    # 3).mengitung vokal:
        # si program memproses setiap huruf dalam kalimat. 
    # 4).menampilkan hasil:
        # program tampilkan total jumlah hurup dalam kalimat.