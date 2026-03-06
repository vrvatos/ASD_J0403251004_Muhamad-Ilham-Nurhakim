def insertionSort(data):
    for index in range(1,len(data)): # Mulai dari elemen ke-2

        currentvalue = data[index] # Simpan elemen saat ini
        position = index

        # Geser elemen yang lebih besar ke kiri
        while position > 0 and data[position-1] < currentvalue:
            data[position]=data[position-1] # Geser elemen ke kiri
            position = position-1
            
        data[position]=currentvalue # Sisipkan elemen ke posisi yang tepat

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(data)
print(data)

# Descending

# Insertion sort adalah algoritma pengurutan sederhana yang 
# menyusun data secara terurut dengan menyisipkan elemen satu 
# per satu ke posisi yang tepat dalam bagian array yang sudah terurut. 
# Proses ini mirip seperti menyusun kartu di tangan, di mana elemen 
# diambil dari bagian yang belum terurut dan dimasukkan ke posisi 
# yang sesuai.