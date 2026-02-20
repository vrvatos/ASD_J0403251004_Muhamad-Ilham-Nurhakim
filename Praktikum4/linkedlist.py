#=============================================
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# kelas : A2
#=============================================

#=========================================================================
# Implememtasi Dasar : Node pada Linked 
#=========================================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika dipanggil / diinstansiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai / data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#1) membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Mendifinisikan head dan menhubungkan node : A -> B -> C -> None
head = nodeA #head menunjuk ke nodeA
nodeA.next = nodeB #nodeA menunjuk ke nodeB
nodeB.next = nodeC #nodeB menunjuk ke nodeC

#3) Traversal : menelusuri node dari head sampai ke none
current = head #head menunjuk ke nodeA
while current is not None:
    print(current.data) #menampilkan data pada node
    current = current.next #memindahkan pointer ke node berikutnya