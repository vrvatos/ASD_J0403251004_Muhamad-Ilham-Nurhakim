class Node:	
    def	__init__(self,	data):	
        self.data	=	data	
        self.next	=	None	

class CircularSinglyLinkedList:	
    def	__init__(self):	
        self.head	=	None	
        self.tail	=	None		#	Tambahkan	pointer	tail	
    
    def	insert_at_end(self,	data):	
        new_node	=	Node(data)	
        if	not	self.head:		#	Jika	linked	list	kosong	
            self.head	=	new_node	
            self.tail	=	new_node	
            self.tail.next	=	self.head		#	Circular	link	ke	dirinya	sendiri	
        else:	
            self.tail.next	=	new_node		#	Sambungkan	tail	ke	node	baru	
            self.tail	=	new_node		#	Update	tail	ke	node	baru	
            self.tail.next	=	self.head		#	Circular	link	kembali	ke	head		

    def	display(self):	
        if	not	self.head:	
            print("List	is	empty")	
            return

        print("Circular Linked List Traversal:")	
        temp = self.head	
        print(temp.data, end=" -> ")	
        temp =	temp.next	

        while	temp	!=	self.head:	
            print(temp.data,	end=" -> ")	
            temp	=	temp.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next

            if temp == self.head:
                return False
        
        print("...(back to head)")	
	
cll	= CircularSinglyLinkedList()	
cll.insert_at_end(3)	
cll.insert_at_end(7)	
cll.insert_at_end(12)	
cll.insert_at_end(19)
cll.insert_at_end(25)	
cll.display()

print("\nSearch for 13:", cll.search(13))
print("Search for 7:", cll.search(7)) 

