#Sakib Faturrahman
#Nim : 2403010015
#disini saya membuat program menampilkan huruf vokal dari sebuah kalimat dengan inputan dari user 

string = input("Input kalimat: ")

vokal = "aiueoAIUEO" 

jumlah_vokal = 0

for huruf in string:   
    if huruf in vokal:
        jumlah_vokal += 1


print("Jumlah huruf vokal: ", jumlah_vokal)