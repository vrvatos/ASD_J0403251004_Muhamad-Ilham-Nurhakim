#========================================================
#PrAKTIKUM 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#========================================================

print("===Membuka file dalam satu string===")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("Tipe data : ", type(isi_file))


#membuka file per baris
print("===Membuka file dalam satu string===")
jumlah_baris = 0 #inisialisasi variabel untuk menghitung jumlah baris
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip() #menghitug baris baru
        print("Baris ke -", jumlah_baris)
        print("isinya : ", baris)
        
#========================================================
#PrAKTIKUM 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : 
#========================================================

#parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghitug baris baru
        nim, nama, nilai = baris.split(",")
        print(f"NIM: {nim} | Nama: {nama} | Nilai: {int(nilai)}")

#======================================================================
#PrAKTIKUM 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca Data dan Menyimpannya ke Struktur Data List
#======================================================================

data_list = []
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghitug baris baru
        nim, nama, nilai = baris.split(",")
        data_list.append([nim, nama, int(nilai)])
print("=== menampilkan list ===")
print(data_list)
print("Contoh record pertama", data_list[0])
print("Contoh record pertama", data_list[1])

#======================================================================
#PrAKTIKUM 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca Data dan Menyimpannya ke Struktur Data Dictionary
#======================================================================
data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghitug baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        #simpan data dalam dictionary (key, value)
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("=== Menampilkan Data dictionary ===")
print(data_dict)
