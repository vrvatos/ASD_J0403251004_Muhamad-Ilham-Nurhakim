#======================================
# Latihan 4 
#
# Menggabungkan dua single linked menjadi 1 linked baru
# ======================================

class Node:	
    def	__init__(self,data):	
        self.data	= data	
        self.next	=	None

class	LinkedList:    
    def	__init__(self):	
        self.head	=	None	
        self.tail	=	None		

    def	insert_at_end(self,	data):	
        new_node	=	Node(data)	
        if	not	self.head:		
            self.head	=	new_node	
            self.tail	=	new_node	
        else:	
            self.tail.next	=	new_node		
            self.tail	=	new_node		

    def	display(self):		
        temp	=	self.head	
        while temp:	
            print(temp.data,	end=" -> ")	
            temp	=	temp.next	
        print("null")

def	merge_linked_lists(ll1, ll2):
    merged_ll	=	LinkedList()	

    current1	=	ll1.head	
    while current1:	
        merged_ll.insert_at_end(current1.data)	
        current1	=	current1.next	

    current2	=	ll2.head	
    while current2:	
        merged_ll.insert_at_end(current2.data)	
        current2	=	current2.next	

    return	merged_ll

print("=== Tampilan 1 ===")
print("\nLinked List 1:")
ll1 = LinkedList()
ll1.insert_at_end(1)
ll1.insert_at_end(3)
ll1.insert_at_end(5)
ll1.insert_at_end(16)
ll1.display()

print("\nLinked List 2:")
ll2 = LinkedList()
ll2.insert_at_end(2)
ll2.insert_at_end(4)
ll2.insert_at_end(6)
ll2.insert_at_end(8)
ll2.display()

merged_ll = merge_linked_lists(ll1, ll2)
print("\nMerged Linked List 1:")
merged_ll.display()


print("\n=== Tampilan 2 ===")
print("\nLinked List 3: ")
ll3 = LinkedList()
ll3.insert_at_end(10)
ll3.insert_at_end(12)
ll3.insert_at_end(14)
ll3.display()

print("\nLinked List 4: ")
ll4 = LinkedList()

merged_ll2 = merge_linked_lists(ll3, ll4)
print("\nMerged Linked List 2:")
merged_ll2.display()



