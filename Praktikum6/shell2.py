def shellSort(data):
    sublistcount = len(data)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(data,startposition,sublistcount)

        print("After increments of size",sublistcount,"The list is",data)
        sublistcount = sublistcount // 2

def gapInsertionSort(data,start,gap):
    for i in range(start+gap,len(data),gap):

        currentvalue = data[i]
        position = i
        while position>=gap and data[position-gap]<currentvalue:
            data[position]=data[position-gap]
            position = position-gap

        data[position]=currentvalue

data = [54,26,93,17,77,31,44,55,20]
shellSort(data)
print(data)

# Descending

# Shell Sort adalah algoritma pengurutan (sorting) berbasis perbandingan 
# yang merupakan pengembangan dari Insertion Sort dengan metode 
# pertambahan menurun (diminishing increment). Dikembangkan oleh 
# Donald Shell pada 1959, algoritma ini mengurutkan elemen yang 
# berjauhan terlebih dahulu, lalu mengurangi jarak (gap) secara 
# bertahap, menjadikannya jauh lebih efisien daripada Insertion 
# Sort tradisional.