#program to extract a substring based on given start andindices 
#get inputs from the user 
word = input ("masukkan kata:")
start_index = int(input ("masukkan indeks awal:"))
end_indeks = int (input("masukkan indeks akhir"))

#get the substring 
substring = word [start_index:end_indeks]

#display the result
print ("substring:", substring)