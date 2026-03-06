def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]<data[i+1]:
                # Tukar dua data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [54,26,93,17,77,31,44,55,20]
bubbleSort(data)
print(data)

# Descending
# Output
# [93, 77, 55, 54, 44, 31, 26, 20, 17]

# Bubble Sort adalah algoritma pengurutan yang bekerja dengan 
# membandingkan dua elemen yang berdekatan dan menukarnya jika 
# urutannya salah, sehingga nilai terbesar secara bertahap "mengapung" 
# ke posisi akhir seperti gelembung. Karena kesederhanaannya, algoritma 
# ini mudah dipahami namun kurang efisien untuk data berjumlah besar dengan 
# kompleksitas waktu sebesar o(n^2).