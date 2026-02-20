#=============================================
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# kelas : A2
#=============================================

#=========================================================================
# Implememtasi Dasar : Stack
#=========================================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika dipanggil / diinstansiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai / data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#Stack ada operasi Push (memasukkan head baru) dan Pop (menghapus head)
# A -> B -> C -> None

class stack:
    def __init__(self):
        self.top = None #pointer top menunjuk ke node paling atas (awal=none)

    def is_empty(self):
        return self.top is None #mengembalikan true jika top menunjuk ke none (stack kosong), false jika tidak

    def push(self,data): #memasukkan data baru ke dalam stack
        # 1 membuat node baru dengan data yang diberikan
        nodeBaru = Node(data) #memanggil konstruktor Node untuk membuat node baru dengan data yang diberikan

        # 2 menghubungkan node baru dengan node yang sudah ada (jika ada)
        nodeBaru.next = self.top #node baru menunjuk ke node yang saat ini menjadi top (bisa jadi none jika stack kosong)

        # 3 geser top untuk menunjuk ke node baru
        self.top = nodeBaru #top sekarang menunjuk ke node baru yang baru saja dibuat

    def pop(self): #mengambil / menghapus node paling atas (top/head)
        
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dam simpan di variabel
        # B -> A -> None
        self.top = self.top.next 
        return data_terhapus

    def peek(self): #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        current = self.top
        print("Top -> ", end="")
        while current is not None:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

# Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat top): ", s.peek())