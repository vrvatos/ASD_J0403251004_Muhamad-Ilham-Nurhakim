def mergeSort(data):
    print("Splitting ",data)
    if len(data)>1:
        mid = len(data)//2
        lefthalf = data[:mid]
        righthalf = data[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] >= righthalf[j]:
                data[k]=lefthalf[i]
                i=i+1
            else:
                data[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            data[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            data[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",data)

data = [54,26,93,17,77,31,44,55,20]
mergeSort(data)
print(data)


# Descending

# Merge sort adalah algoritma pengurutan (sorting) yang efisien, stabil, 
# dan menggunakan pendekatan divide and conquer (pecah dan taklukkan) untuk 
# mengurutkan elemen. Algoritma ini memecah data menjadi bagian kecil, 
# mengurutkannya, lalu menggabungkannya kembali. Ditemukan oleh John von 
# Neumann pada 1945, merge sort bekerja dalam waktu 
