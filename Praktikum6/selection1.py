def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1): # Ulangi dari akhir ke awal
        positionOfMax=0 # Anggap elemen pertama adalah terbesar
        for location in range(1,fillslot+1): # Cari posisi elemen terbesar
            if data[location]>data[positionOfMax]:
                positionOfMax = location # Update posisi jika ada yang lebih besar

        # Tukar elemen terbesar ke posisi akhir
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp

data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print(data)

#Ascending

# Selection sort adalah algoritma pengurutan sederhana yang bekerja dengan cara 
# berulang kali mencari elemen terkecil dari bagian yang belum terurut dan menukarnya 
# ke posisi awal, membagi data menjadi bagian terurut (kiri) dan belum terurut (kanan). 
# Algoritma ini memiliki kompleksitas waktu o(n^2) dan cocok untuk dataset kecil.