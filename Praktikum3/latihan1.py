class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None


class LinkedList: 
    def __init__(self): 
        self.head = None 
        self.tail = None  

    def insert_at_end(self, data): 
        new_node = Node(data) 
        if not self.head:  
            self.head = new_node 
            self.tail = new_node  
        else: 
            self.tail.next = new_node  
            self.tail = new_node  

    def display(self): 
        temp = self.head 
        while temp: 
            print(temp.data, end=" -> ") 
            temp = temp.next 
        print("null") 

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next

            if self.head is None:
                self.tail = None

            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

        if temp == self.tail:
            self.tail = prev

        temp = None


ll = LinkedList()  
ll.insert_at_end(10)  
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.display()
ll.delete_node(30)
ll.display()
