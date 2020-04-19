"'Code from Mithra'"
class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def append(self, node):
        if(self.head==None):
            self.head=node
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=node
    
    def printList(self):
        current=self.head
        list=[]
        while(current!=None):
            list.append(current.data)
            current=current.next
        return list
            
    def count(self):
        current=self.head
        count=0
        while(current!=None):
            count+=1
            current=current.next
        return count
    
    def insertElement(self, newValue, position):
        current=self.head
        newElement=Node(newValue)
        if(position==1):
            newElement.next=current
            self.head=newElement
        else:
            for i in range(0, position-2):
                current=current.next
            
            newElement.next=current.next
            current.next=newElement
    
obj1=Node(1)
obj2=Node(2)
obj3=Node(3)
obj4=Node(4)
obj5=Node(5)

Llist=LinkedList()

Llist.append(obj1)
Llist.append(obj2)
Llist.append(obj3)
Llist.append(obj4)
Llist.append(obj5)

print Llist.printList()
print Llist.count()

Llist.insertElement(6,4)
print Llist.printList()
print Llist.count()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            