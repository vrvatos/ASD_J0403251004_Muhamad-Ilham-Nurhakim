# ========================================================== 
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : A - A2 - P2
# ==========================================================
# Contoh Rekursi 3(Data List): Menjumlahkan elemen list
# ==========================================================

def jumlah_list(data, index=0):
    """
    Fungsi rekursif untuk menghitung jumlah seluruh elemen dalam sebuah list.

    Parameter:
        data (list): List yang berisi angka-angka (int/float) yang akan dijumlahkan.
        index (int): Indeks saat ini yang diproses (nilai default 0).

    Return:
        int/float: Total jumlah semua elemen dari indeks 'index' hingga akhir list.
    """

    # BASE CASE (Kasus Dasar)
    # jika indeks yang akan diproses sudah mencapai panjang list,
    # artinya tidak ada lagi elemen yang tersisa. Maka kembalikan 0.
    if index == len(data):
        return 0

    # RECURSIVE CASE (Kasus Rekursif)
    # jumlahkan elemen pada posisi 'index' dengan hasil rekursif dari sisa list.
    # fungsi memanggil dirinya sendiri dengan indeks berikutnya (index + 1),
    # sehingga masalah diperkecil hingga mencapai base case.
    return data[index] + jumlah_list(data, index + 1)

# contoh penggunaan: menjumlahkan elemen list [2, 4, 6, 8]
# proses rekursif yang terjadi:
# jumlah_list([2,4,6,8], 0) = 2 + jumlah_list([2,4,6,8], 1)
#                           = 2 + (4 + jumlah_list([2,4,6,8], 2))
#                           = 2 + (4 + (6 + jumlah_list([2,4,6,8], 3)))
#                           = 2 + (4 + (6 + (8 + jumlah_list([2,4,6,8], 4))))
#                           = 2 + (4 + (6 + (8 + 0))) = 20
print(jumlah_list([2, 4, 6, 8]))  # Output: 20