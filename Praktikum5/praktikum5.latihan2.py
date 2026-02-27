# ========================================================== 
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : A - A2 - P2
# ==========================================================
# Latihan 2 : Tracing Rekursi 
# ========================================================== 

def countdown(n): 
    if n == 0: 
        print("Selesai") 
        return 
    print("Masuk:", n) 
    countdown(n - 1) 
    print("Keluar:", n) 
countdown(3)

# Hal ini disebabkan oleh cara kerja tumpukan (stack) rekursi. 
# Setiap kali fungsi memanggil dirinya sendiri, pemanggilan baru ditempatkan di atas tumpukan, 
# dan eksekusi pemanggilan sebelumnya ditunda hingga pemanggilan yang lebih dalam selesai.

# Jadi, urutan "Keluar" mengikuti urutan kembalinya fungsi dari yang paling dalam (n terkecil) 
# ke yang paling luar (n terbesar). Inilah sebabnya output "Keluar" muncul terbalik dibandingkan 
# dengan urutan "Masuk".

# Contoh kasus :
# Saat "Masuk", kita menaruh piring di tumpukan (dari bawah ke atas: 3, lalu 2, lalu 1).
# Saat "Keluar", kita mengambil piring dari atas (yang terakhir ditaruh) terlebih dahulu, 
# yaitu 1, lalu 2, lalu 3.