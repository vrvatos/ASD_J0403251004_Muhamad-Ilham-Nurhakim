# ========================================================== 
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : A - A2 - P2
# ==========================================================
# Latihan 1 : Rekursif Pangkat  
# ========================================================== 

def pangkat(a, n): 

    # Base case 
    if n == 0: 
        return 1 

    # Recursive case 
    return a * pangkat(a, n - 1) 

print(pangkat(2, 4))  # Output: 16

# fungsi pangkat(a, n) menghitung nilai a dengan pangkat n secara rekursif dengan rumus:
#           jika n == 0, maka hasilnya adalah 1 - base case
#           jika n > 0, maka a^n = a * a^(n-1) - rekursif

# BASE CASE
# Base case adalah kondisi yang menghentikan rekursi. Di sini, ketika n == 0, 
# fungsi langsung mengembalikan 1 tanpa memanggil dirinya sendiri. 
# Ini penting agar rekursi tidak berlanjut tanpa batas.

# REKURSIF CASE
# Jika n > 0, fungsi akan mengembalikan a * pangkat(a, n-1). 
# Artinya, masalah a^n diperkecil menjadi a^(n-1), dan seterusnya hingga mencapai base case.