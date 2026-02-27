# ========================================================== 
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : A - A2 - P2
# ==========================================================
# Latihan 5 : Generator PIN  
# ========================================================== 

def buat_pin(panjang, hasil=""): 
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
    for angka in ["0", "1", "2"]: 
        buat_pin(panjang, hasil + angka) 
buat_pin(3) 

# Untuk mencegah angka yang sama muncul berulang dalam pembuatan PIN, 
# kita dapat memodifikasi fungsi rekursif dengan menambahkan parameter pelacak, 
# misalnya last_angka untuk mencegah angka yang sama berurutan (dengan membandingkan 
# angka yang akan ditambahkan dengan angka sebelumnya) atau used berupa himpunan untuk 
# mencegah angka yang sama sama sekali (hanya menambahkan angka yang belum pernah dipakai), 
# sehingga setiap cabang rekursi hanya mengeksplorasi pilihan yang memenuhi aturan tersebut 
# dan menghasilkan kombinasi PIN sesuai batasan yang diinginkan.

# Contoh sintaks nya :

# def buat_pin(panjang, hasil="", used=None):
#   if used is None:
#       used = set()
#   if len(hasil) == panjang:
#       print("PIN:", hasil)
#       return
#   for angka in ["0", "1", "2"]:
#       if angka not in used:
#           buat_pin(panjang, hasil + angka, used | {angka})
# buat_pin(3)  # panjang maksimal 3 karena hanya 3 angka