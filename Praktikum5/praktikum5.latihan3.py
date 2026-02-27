# ========================================================== 
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : A - A2 - P2
# ==========================================================
# Latihan 3 : Mencari Nilai Maksimum 
# ========================================================== 

def cari_maks(data, index=0): 
    # Base case 
    if index == len(data) - 1: 
        return data[index] 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) 
    if data[index] > maks_sisa: 
        return data[index] 
    else: 
        return maks_sisa 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka)) 

# Fungsi cari_maks bekerja dengan prinsip divide and conquer secara rekursif: 
# memecah masalah mencari maksimum dari seluruh list menjadi membandingkan elemen 
# pertama dengan maksimum dari sisa list. Prosesnya berlanjut hingga mencapai elemen terakhir (base case).

# BASE CASE
# Base case terjadi ketika index sama dengan indeks terakhir list (len(data)-1). 
# Pada titik ini, tidak ada lagi elemen setelahnya, sehingga nilai maksimum dari 
# sublist yang hanya berisi satu elemen adalah elemen itu sendiri. Fungsi langsung mengembalikan data[index].

# REKURSIF CASE
# Jika index belum mencapai elemen terakhir, fungsi akan:
# Memanggil dirinya sendiri dengan index+1 untuk mendapatkan nilai maksimum dari sisa list 
# (dari index+1 hingga akhir). Hasilnya disimpan dalam variabel maks_sisa.
# Membandingkan data[index] dengan maks_sisa.
# Mengembalikan nilai yang lebih besar di antara keduanya.
# Dengan cara ini, setiap panggilan rekursif akan "menyerahkan" tanggung jawab mencari 
# maksimum kepada panggilan berikutnya, hingga mencapai base case, lalu hasilnya dikembalikan ke atas 
# sambil dibandingkan.

# GARIS BESAR
# Base case menghentikan rekursi pada elemen terakhir.
# Recursive call memperkecil masalah dengan memproses sisa list.
# Perbandingan dilakukan saat kembali dari rekursi, sehingga nilai maksimum "merambat" 
# naik ke panggilan teratas.