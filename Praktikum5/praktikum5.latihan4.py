# ========================================================== 
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : A - A2 - P2
# ==========================================================
# Latihan 4 : Kombinasi Huruf
# ========================================================== 

def kombinasi(n, hasil=""): 
    if len(hasil) == n: 
        print(hasil) 
        return 
    kombinasi(n, hasil + "A") 
    kombinasi(n, hasil + "B") 
kombinasi(2) 

# Mengapa Jumlahnya Tepat 2ⁿ?
# Karena setiap level rekursi (penambahan karakter) menggandakan jumlah cabang. 
# Pada level pertama (panjang 0), ada 1 cabang. Setelah menambahkan karakter pertama, 
# menjadi 2 cabang. Setelah menambahkan karakter kedua, masing-masing cabang bercabang lagi menjadi 2, 
# total 4 cabang, dan seterusnya. Jadi pada level ke-n, jumlah cabang (kombinasi) adalah 2ⁿ.

# BASE CASE : berhenti ketika panjang string mencapai n dan mencetak hasil.
# REKURSIF CASE : memanggil dirinya sendiri dua kali dengan menambahkan 'A' atau 'B', 
# sehingga semua kemungkinan dieksplorasi.