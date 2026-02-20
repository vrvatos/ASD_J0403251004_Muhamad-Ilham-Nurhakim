#=============================================
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# kelas : A2
#=============================================

#=========================================================================
# Implememtasi Dasar : Queue
#=========================================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika dipanggil / diinstansiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai / data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

class Queue: #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #node paling depan    
        self.rear = None #node paling belakang    

    def is_empty(self):
        return self.front is None

    #membuat fungsi untuk menambahkan data baru pada bagian belakang
    def enqueue(self, data):
        nodeBaru = Node(data)

        # jika q kosong, front dan rear menunjuk ke node yang sama 
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #jika q tidak kosonh, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #letakkan data baru pada setelah rear
        self.rear = nodeBaru #jadikan data baru sebagai rear

    def dequeue(self):
        #menghapus data dari front / depan
        data_terhapus = self.front.data #lihat data paling depan

        #geser front ke node berikutnya
        self.front = self.front.next

        #jika setelah geser front menjadi none, maka q kosong
        if self.front is None:
            self.rear = None

    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(" Rear")

#instantiasi

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()

