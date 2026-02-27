# ========================================================== 
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : A - A2 - P2
# ==========================================================
# Contoh Rekursi 2 (Call Stack):  Tracing Masuk/keluar
# ==========================================================

def hitung(n):
    """
    Fungsi rekursif ini menunjukkan urutan "masuk" dan "keluar" dari setiap level rekursi.
    Setiap panggilan rekursif akan mencetak "Masuk: n" sebelum memanggil dirinya sendiri,
    dan mencetak "Keluar: n" setelah panggilan rekursif selesai.
    """

    # BASE CASE: kondisi berhenti rekursi
    # ketika n mencapai 0, kita tidak bisa melakukan panggilan rekursi lagi.
    # cukup cetak "Selesai" dan return (kembali ke pemanggil sebelumnya).
    if n == 0:
        print("Selesai")
        return

    # bagian ini dieksekusi SEBELUM fungsi memanggil dirinya sendiri.
    # menampilkan nilai n saat memasuki level rekursi saat ini.
    print("Masuk:", n)

    # rECURSIVE CASE: panggil fungsi yang sama dengan nilai n-1.
    # di sinilah terjadi rekursi, masalah diperkecil.
    # program akan berhenti di sini sementara, menjalankan hitung(n-1) hingga selesai,
    # baru kemudian melanjutkan ke baris berikutnya.
    hitung(n - 1)

    # bagian ini dieksekusi SETELAH panggilan rekursif selesai (kembali dari rekursi).
    # menampilkan nilai n saat keluar dari level rekursi saat ini.
    # perhatikan bahwa nilai n di sini adalah nilai dari pemanggil, bukan dari rekursi yang lebih dalam.
    print("Keluar:", n)

# Memanggil fungsi hitung dengan argumen 3 untuk melihat alur rekursi.
hitung(3) 