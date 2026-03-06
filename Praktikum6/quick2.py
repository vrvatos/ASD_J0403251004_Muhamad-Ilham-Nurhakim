def quickSort(data):
    quickSortHelper(data, 0, len(data)-1)

def quickSortHelper(data, first, last):
    if first < last:
        splitpoint = partition(data, first, last)
        quickSortHelper(data, first, splitpoint-1)
        quickSortHelper(data, splitpoint+1, last)

def partition(data, first, last):
    pivotvalue = data[first]
    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and data[leftmark] >= pivotvalue:  # > saja
            leftmark = leftmark + 1

        while data[rightmark] <= pivotvalue and rightmark >= leftmark:  # < saja
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp
    return rightmark

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(data)
print(data)


# Descending

# Quick Sort adalah algoritma pengurutan data yang sangat efisien menggunakan 
# pendekatan divide and conquer (bagi dan taklukkan). Algoritma ini bekerja 
# dengan memilih sebuah elemen sebagai pivot, lalu mempartisi array agar elemen 
# lebih kecil berada di kiri dan lebih besar di kanan. Rata-rata kompleksitas waktunya adalah 
