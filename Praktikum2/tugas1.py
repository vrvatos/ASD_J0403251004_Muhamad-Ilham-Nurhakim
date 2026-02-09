#=======================================================================================
# Tugas HANDS-ON MODUL 1
# Studi Kasus : Sistem Stock Barang Mainan (Berbasis File .txt)
# 
# Nama      : Muhamad Ilham Nurhakim
# NIM       : J0403251004
# Kelas     : A - A2 - P2
#=======================================================================================

#---------------------------------------------------------------------------------------
# Fungsi Tambahan Untuk Tampilan
#---------------------------------------------------------------------------------------

def garis(panjang = 50):
    print("=" * panjang)

def garis_tipis(panjang = 50):
    print("=" * panjang)

#---------------------------------------------------------------------------------------
# Fungsi 1 : Membaca Data dari File
#---------------------------------------------------------------------------------------

nama_file = "stock_barang.txt"
'''
Membaca data stok dari file text
Dengan Format : KodeBarang, NamaBarang, Stock
'''
def baca_stok(nama_file):
    stok_dict = {} # Inisialisasi dictionary kosong untuk menampung data stok
    with open(nama_file, "r", encoding="utf-8") as file: # Membuka file dalam mode read ("r")
        for baris in file: # Membaca file baris demi baris
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
            stok_dict[kode] = {"nama" : nama, "stok" : int(stok)}
    return stok_dict

#---------------------------------------------------------------------------------------
# Fungsi 2 : Menyimpan Data ke File
#---------------------------------------------------------------------------------------

def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file: # Membuka file dalam mode write ("w") -> menimpa isi file lama
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode}, {nama}, {stok}\n") # Menulis data ke file sesuai format yang ditentukan

#---------------------------------------------------------------------------------------
# Fungsi 3 : Menampilkan semua data dari File
#---------------------------------------------------------------------------------------

def tampilkan_semua(stok_dict):
    if len(stok_dict) == 0:
        garis()
        print("📦 STOK BARANG KOSONG!")
        garis()
        return

    garis()
    print("📑 Daftar STOK BARANG MAINAN")
    garis()

    print(f"{'Kode Barang':<12} | {'Nama Barang':<20} | {'Stok Barang':>6}")
    garis_tipis()

    for kode in sorted(stok_dict.keys()): #nampilin semua data berdasarkan urutan kode
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<12} | {nama:<20} | {stok:>6}")
    garis()

#---------------------------------------------------------------------------------------
# Fungsi 4 : Memcari Barang Berdasarkan Kode
#---------------------------------------------------------------------------------------

def cari_barang(stok_dict):
    garis()
    print("🔍 CARI BARANG")
    garis()

    kode = input("Masukkan Kode Barang : ").strip()

    if kode in stok_dict:
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]

        garis()
        print("✅ BARANG DITEMUKAN")
        garis()
        print(f"Kode Barang   : {kode}")
        print(f"Nama Barang   : {nama}")
        print(f"Stok Barang   : {stok}")
        garis()
    else:
        garis()
        print("❌ BARANG TIDAK DITEMUKAN.")
        garis()

#---------------------------------------------------------------------------------------
# Fungsi 5 : Fitur Menambah Barang Baru
#---------------------------------------------------------------------------------------

def tambah_barang(stok_dict):
    garis()
    print("➕ Tambah Barang Baru")
    garis()

    kode = input("Masukkan Kode Barang Baru : ").strip()

    if kode in stok_dict: # kode tidak boleh sama dengan yg sudah ada
        print("⚠️ Kode Sudah Digunakan. Tambah barang dibatalkan.")
        garis()
        return

    nama = input("Masukkan nama Barang: ").strip()

    try:
        stok_awal = int(input("Masukkan stok awal : ").strip())
    except ValueError:
        print("⚠️ Stok harus berupa angka. Tambah barang dibatalkan")
        garis()
        return

    if stok_awal < 0:
        print("⚠️ Stok tidak boleh negatif. Tambah barang dibatalkan")
        garis()
        return

    stok_dict[kode] = {"nama" : nama, "stok" : stok_awal} # menyimpan barang baru ke dictionary
    print("✅ Barang berhasil ditambahkan")
    garis()

#---------------------------------------------------------------------------------------
# Fungsi 6 : Membaca data dari File
#---------------------------------------------------------------------------------------

def update_stok(stok_dict):
    garis()
    print("🔃 UPDATE STOK BARANG")
    garis()

    kode = input("Masukkan kode barang yang ingin di update").strip()

    if kode not in stok_dict: # Validasi kode harus ada di dictionary
        print("❌ Barang tidak ditemukan. Update dibatalkan")
        garis()
        return

    print("\nPilih jenis Update:")
    print("[1] Tambah stok")
    print("[2] Kurangi stok")

    pilihan = input("Masukkan Pilihan : ").strip()

    try:
        jumlah = int(input("Masukkan Jumlah : ").strip())
    except ValueError:
        print("⚠️ Jumlah harus berupa angka. Tambah barang dibatalkan")
        garis()
        return

    if jumlah < 0:
        print("⚠️ Jumlah tidak boleh negatif. Tambah barang dibatalkan")
        garis()
        return

    stok_lama = stok_dict[kode]["stok"] # menyimpan stok lama untuk perhitungan

    if pilihan == "1":
        stok_dict[kode]["stok"] = stok_lama + jumlah
        print("✅ Stok berhasil ditambah. Stok di gudang sekarang: {stok_dict[kode]['stok']}")
        garis()

    elif pilihan == "2":
        stok_baru = stok_lama - jumlah

        if stok_baru < 0:
            print("❌ Stok tidak boleh negatif. Update dibatalkan")
            garis()
            return

        stok_dict[kode]["stok"] = stok_baru
        print("✅ Stok berhasil dikurangi. Stok di gudang sekarang: {stok_dict[kode]['stok']}")
        garis()

    else:
        print("⚠️ Pilihan tidak valdi. Update dibatalkan")
        garis()

#---------------------------------------------------------------------------------------
# Program Utama
#---------------------------------------------------------------------------------------

def main():
    stok_barang = baca_stok(nama_file)

    while True:
        garis()
        print("🏪 SISTEM STOK BARANG MAINAN")
        garis()
        print("[1] Tampilkan semua barang")
        print("[2] Cari barang berdasarkan kode")
        print("[3] Tambah barang baru")
        print("[4] Update stok barang")
        print("[5] Simpan ke file")
        print("[0] Keluar")
        garis_tipis()

        pilihan = input("Pilih menu: ").strip() # membaca data stok dari filr saat program dimulai

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            garis()
            print("💾 Data berhasil disimpan ke file!")
            garis()

        elif pilihan == "0":
            garis()
            print("👋 Program selesai. Terima kasih!")
            garis()
            break

        else:
            print("⚠️  Pilihan tidak valid. Silakan coba lagi.")

# menjalankan program utama
if __name__ == "__main__":
    main()