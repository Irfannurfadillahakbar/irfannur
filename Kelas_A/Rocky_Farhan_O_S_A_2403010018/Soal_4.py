kalimat = input("Masukkan kalimat: ")
huruf_a = "a"
huruf_i = "i"
huruf_u = "u"
huruf_e = "e"
huruf_o = "o"
huruf_A = "A"
huruf_I = "I"
huruf_U = "U"
huruf_E = "E"
huruf_O = "O"
jumlah_vokal_1 = kalimat.count(huruf_a)
jumlah_vokal_2 = kalimat.count(huruf_i)
jumlah_vokal_3 = kalimat.count(huruf_u)
jumlah_vokal_4 = kalimat.count(huruf_e)
jumlah_vokal_5 = kalimat.count(huruf_o)
jumlah_vokal_6 = kalimat.count(huruf_A)
jumlah_vokal_7 = kalimat.count(huruf_I)
jumlah_vokal_8 = kalimat.count(huruf_U)
jumlah_vokal_9 = kalimat.count(huruf_E)
jumlah_vokal_0 = kalimat.count(huruf_O)
jumlah_vokal = jumlah_vokal_1 + jumlah_vokal_2 + jumlah_vokal_3 + jumlah_vokal_4 + jumlah_vokal_5 + jumlah_vokal_6 + jumlah_vokal_7 + jumlah_vokal_8 + jumlah_vokal_9 + jumlah_vokal_0

print(f"Jumlah huruf vokal: {jumlah_vokal}")