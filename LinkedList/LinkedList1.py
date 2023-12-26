class Node:
    def __init__(self , value):
        self.value = value
        self.next =None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node  
            self.tail = new_node
        else:
            self.tail.next = new_node   
            self.tail= new_node
        self.length += 1

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    def insert(self,value,i):
        new_node=Node(value)
        if i < 0 or i > self.length:
            return False
        if i == 0:
            new_node.next = self.head
            self.head = new_node
    
        else:     
            temp_node=self.head
            for _ in range(i-1):
                temp_node=temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1 
        return True
    

    def traversal(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    def search(self,s_value):
        temp_node = self.head
        for i in range(self.length):
            if(temp_node.value==s_value):
                return i
            temp_node=temp_node.next

    def get(self,index):
        temp_node=self.head
        if index < 0 or index > self.length:
            return False
        else:
            for _ in range(index):
                temp_node = temp_node.next
        return temp_node.value
    def pop(self):
        temp_node = self.head
        self.head = self.head.next
        temp_node.next = None
        self.length -= 1
        return temp_node.value
    

    
    def remove(self , index):
        prev_node = self.get(index-1)
        pop_node = prev_node.next
        prev_node.next = pop_node.next
        pop_node.next = None
        self.length -= 1







        

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
        
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result
New_object=LinkedList()
New_object.append(10)


New_object.append(20)
New_object.append(30)
New_object.append(40)


New_object.remove(20)
print(New_object)






print('hello world')