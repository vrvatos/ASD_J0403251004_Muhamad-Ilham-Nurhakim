# ========================================================== 
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : A - A2 - P2
# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning) 
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    """
    Fungsi rekursif untuk mencetak semua string biner dengan panjang n,
    namun hanya yang memiliki jumlah angka '1' tidak melebihi batas (pruning).
    Menggunakan teknik backtracking dengan pemangkasan (pruning) untuk efisiensi.

    Parameter:
        n (int): Panjang string biner yang diinginkan.
        batas (int): Batas maksimum jumlah angka '1' yang diperbolehkan.
        hasil (str): String sementara yang sedang dibangun (default kosong).
        jumlah_1 (int): Jumlah angka '1' yang sudah digunakan dalam hasil sementara (default 0).
    """

    # PRUNING (Pemangkasan):
    # jika jumlah angka '1' sudah melebihi batas yang ditentukan,
    # maka tidak perlu melanjutkan rekursi karena akan selalu melebihi batas.
    # ini menghemat waktu dengan memotong cabang yang tidak memenuhi syarat.
    if jumlah_1 > batas:
        return

    # BASE CASE:
    # jika panjang hasil sudah mencapai n, berarti kita telah membangun
    # satu kombinasi lengkap yang memenuhi syarat (karena pruning sudah memastikan
    # jumlah_1 <= batas). Cetak kombinasi tersebut.
    if len(hasil) == n:
        print(hasil)
        return

    # RECURSIVE CASE 1: Menambahkan karakter '0'
    # Jumlah angka '1' tidak bertambah, karena menambahkan '0'.
    # panggil rekursif dengan hasil yang diperbarui.
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # RECURSIVE CASE 2: Menambahkan karakter '1'
    # jumlah angka '1' bertambah 1.
    # panggil rekursif dengan hasil dan jumlah_1 yang diperbarui.
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

# memanggil fungsi untuk n=4 dan batas=2.
# akan mencetak semua string biner 4-bit yang memiliki maksimal 2 buah angka '1'.
biner_batas(4, 2)