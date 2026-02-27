# ========================================================== 
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : A - A2 - P2
# ==========================================================
# Contoh Rekursi 1 (Rekursif): Faktorial 
# ========================================================== 

def faktorial(n):
    """
    Fungsi ini menghitung nilai faktorial dari bilangan bulat non-negatif n
    secara rekursif. Faktorial dari n (ditulis n!) didefinisikan sebagai:
    0! = 1
    n! = n * (n-1)! untuk n > 0

    Parameter:
        n (int): n adalah bilangan bulat non-negatif yang akan dihitung faktorialnya.

    Return:
        int adalah hasil faktorial dari n.
    """
    
    # base case: kondisi berhenti rekursi
    # jika n == 0, faktorialnya adalah 1
    if n == 0:
        return 1

    # recursif : panggil diri sendiri dengan masalah yang lebih kecil
    # faktorial n = n * faktorial(n-1)
    # di sini fungsi rekursif memanggil dirinya sendiri dengan argumen n-1,
    # sehingga masalah terus mengecil hingga mencapai base case.
    return n * faktorial(n - 1)

# contoh penggunaan fungsi faktorial
# menghitung 5! = 5 * 4 * 3 * 2 * 1 = 120
print(faktorial(5))  # output nya adalah 120