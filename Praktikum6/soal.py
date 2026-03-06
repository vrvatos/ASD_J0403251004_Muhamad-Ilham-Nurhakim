def insertionSort(data_potensi):
    data_potensi = data_potensi.copy()
    for index in range(1,len(data_potensi)): 

        currentvalue = data_potensi[index] 
        position = index

        while position>0 and data_potensi[position-1] < currentvalue:
            data_potensi[position]=data_potensi[position-1] 
            position = position-1
            
        data_potensi[position]=currentvalue 

    return data_potensi

data_potensi = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# pengseleksian

seleksi_data = insertionSort(data_potensi)
top_5 = seleksi_data[:5]

print("=" * 42)
print(f"\n  = Data Awal    : {data_potensi}")
print(f"  = Data Terurut : {seleksi_data}")

print(f"\n  = 5 Skor Tertinggi (Tertinggi → Terendah):")
for i, nilai in enumerate(top_5, 1):
    print(f"     Peringkat {i}: {nilai}")

print(f"\n  = Hasil Seleksi Kandidat:")
lolos = []
for i, nilai in enumerate(data_potensi, 1):
    if nilai in top_5:
        status = "Kandidat Lolos"
        lolos.append(i)
    else:
        status = "Kandidat Tidak Lolos"
    print(f"     Kandidat {i:2d} (skor: {nilai:3d}) → {status}")

print(f"\n  = Kandidat lolos: {', '.join(f'Kandidat {k}' for k in lolos)}")
print("=" * 42)