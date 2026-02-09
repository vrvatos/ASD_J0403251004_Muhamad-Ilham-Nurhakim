#======================================================================
#PrAKTIKUM 2 : Konsep ADT dan File Handling (Studi Kasus)
#Latihan 1 : MMembuat Fungsi Load Data dari File 
#======================================================================

# Variabel menyimpan data file

nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {}  #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data perbaris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] = {"nama" : nama, "nilai" : int(nilai)}
    return data_dict

#buka_data = baca_data(nama_file) 
#print("jumlah data terbaca", len(buka_data)) #melihat berapa banyak data di load

#======================================================================
#PrAKTIKUM 2 : Konsep ADT dan File Handling (Studi Kasus)
#Latihan 2 : MMembuat Fungsi Menampilkan Data 
#======================================================================

def tampilkan_data(data_dict):
    #membuat header tabel
    print("\n=== DAFRTAR MAHASISWA ===")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}")
    '''
    Untuk tampilan yang rapi, atur lebar kolom
    {'NIM' : <10} nim akan rata kiri dengan lebar 10 karalter
    {'Nama' : <12} nama akan rata kiri dengan lebar 12 karakter
    {'Nilai' :>5} nilai akan rata kanan lebar 5
    '''
    print("-"*32) #garis

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")


#tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

#======================================================================
#PrAKTIKUM 2 : Konsep ADT dan File Handling (Studi Kasus)
#Latihan 3 : MMembuat Fungsi Mencari Data 
#======================================================================

#membuat fungsi pencarian

def cari_data(data_dict):
    #pencarian data berdasrkan nim sebagai ke dict
    #membuat input nim mahasiswa yg akan di cari
    nim_cari = input("Masukkan NIM mahasiswa yang ingin di cari : ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n=== Data Mahasiswa Ditemukan ===")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else :
        print("\nData tidak Ditemukan. Pastikn NIM yang dimasukkan benar.")

#======================================================================
#PrAKTIKUM 2 : Konsep ADT dan File Handling (Studi Kasus)
#Latihan 4 : MMembuat Fungsi Update Data 
#======================================================================

#membuat fungsi update data
def ubah_data(data_dict):
    #diawali dengan mencari nim/data mahasiswa yang ingin di update
    nim = input("Masukkan NIM mahasiswa yang ingin dicari : ").strip()

    if nim not in data_dict:

        print("NIM tidak ditemukan. Update Nilai dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan Nilai baru 0-100 : ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update Nilai dibatalkan")

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update Nilai dibatalkan")
        

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil data
    #ubah_data(buka_data)

#======================================================================
#PrAKTIKUM 2 : Konsep ADT dan File Handling (Studi Kasus)
#Latihan 5 : MMembuat Fungsi Update Data 
#======================================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#manggil fungsi data
#simpan_data(nama_file, buka_data)
print("\nData Berhasil Disimpan ke file: ", nama_file)

#======================================================================
#PrAKTIKUM 2 : Konsep ADT dan File Handling (Studi Kasus)
#Latihan 6 : MMembuat Menu Interaktif 
#======================================================================

def main():
    #load data otomatis saat program di mulai
    buka_data = baca_data(nama_file) #fungsi pertama (fungsi load data)

    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilakan Data Mahasiswa")
        print("2. Cari Data berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu : ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data) #2 mencari data

        elif pilihan == "2":
            cari_data(buka_data) #3 mencari data

        elif pilihan == "3":
            ubah_data(buka_data) #4 mengubah Data

        elif pilihan == "4":
            simpan_data(nama_file, buka_data) #5 menyimpan data ke file
            print("Data Berhasil Disimpan")

        elif pilihan == "0":
            print("Program Selesai")
            break

        else:
            print("Pilihan Tidak Valid. Silahkan Coba lagi")

if __name__ == "__main__":
    main()