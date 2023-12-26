class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class CLL():
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        Node = self.head
        while Node:
            yield Node
            
            if Node.next == self.head:
                break
            Node = Node.next
            
    def c(self,value):
        temp = Node(value)
        temp.next = temp
        self.head = temp
        self.tail = temp
    def insert(self, value , location):
        newnode= Node(value)
        if self.head == None:
            return "there are no nodes"
        elif location == 0:
            newnode.next = self.head
            self.head = newnode
            self.tail.next = newnode
        elif location == 1:
            self.tail.next = newnode
            self.tail = newnode
            newnode.next = self.head
        else:
            temp = self.head
            index = 0
            while index < location -1:
                temp = temp.next
                index += 1
            newnode.next = temp.next 
            temp.next = newnode

    def search(self,value):
        temp = self.head
        while temp:
            if temp.value == value:
                return "true"
            temp = temp.next
            if temp == self.tail.next:
                return "element not found"
    def delete(self,location):
        if self.head == None:
            return "there are no elements to delete"
        elif location == 0:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif location == 1:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node.next is not self.tail:
                    node = node.next
                node.next = self.head 
                self.tail = node
        else:
            node = self.head
            index = 0
            while index < location - 1:
                node = node.next 
                index +=1
            nextnode = node.next
            node.next = nextnode.next
    def delete_entire(self):
        if self.head == None:
            return  "ther's nothing to delete"
        else:
            self.head.next = None
            self.head = None
            self.tail = None

                
                
ob = CLL()     
ob.c(1)  
ob.insert(0,0)   
ob.insert(3,1)
ob.insert(2,2)    

ob.insert(4,1)
ob.insert(5,1)
ob.insert(6,1)
print([node.value for node in ob])
ob.delete_entire()
print([node.value for node in ob])


