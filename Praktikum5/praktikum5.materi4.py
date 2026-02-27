# ========================================================== 
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : A - A2 - P2
# ==========================================================
# Contoh Backtracking 1: Kombinaasi Biner (n) 
# ==========================================================

def biner(n, hasil=""):
    """
    Fungsi rekursif untuk mencetak semua kemungkinan string biner dengan panjang n.
    Menggunakan pendekatan backtracking sederhana.

    Parameter:
        n (int): Panjang string biner yang diinginkan.
        hasil (str): String sementara yang sedang dibangun (default kosong).
    """

    # BASE CASE: jika panjang string hasil sudah mencapai n,
    # maka kita telah membangun satu kombinasi lengkap.
    # cetak kombinasi tersebut dan kembali (return) ke pemanggil.
    if len(hasil) == n:
        print(hasil)
        return

    # RECURSIVE CASE 1: Tambahkan karakter '0' ke dalam hasil,
    # lalu panggil fungsi secara rekursif untuk melanjutkan pembangunan string.
    # Ini adalah langkah "choose" (pilih) dan "explore" (jelajahi).
    biner(n, hasil + "0")

    # RECURSIVE CASE 2: Tambahkan karakter '1' ke dalam hasil,
    # lalu panggil fungsi secara rekursif untuk melanjutkan.
    # dengan dua panggilan ini, semua kemungkinan kombinasi akan dijelajahi.
    biner(n, hasil + "1")

# memanggil fungsi biner dengan n = 3 untuk mencetak semua string biner 3-bit.
biner(3)