class Node:
    def __init__(self,a):
        self.data=a
        self.nextValue=None
class LinkedList:
    def __init__(self):
        self.head=None
    def deleteValue(self,value):
        current=self.head
        prev=current
        while(current.data!=value):
            prev=current
            current=current.nextValue
        if(prev==current):
            self.head=current.nextValue
        else:
            prev.nextValue=current.nextValue
    def deleteFromposition(self,userposition):
        current=self.head
        position=1
        prev=current
        while(userposition!=position):
            position+=1
            #prev=current
            current=current.nextValue
        if(prev==current):
            self.head=current.nextValue
        else:
            prev.nextValue=current.nextValue
    def printElement(self):
        current=self.head
        l=[]
        while(current!=None):
            l.append(current.data)
            current=current.nextValue
        return l
    

obj1=Node(1)
obj2=Node(2)
obj3=Node(3)
obj4=Node(4)
obj5=Node(5)
obj1.nextValue=obj2
obj2.nextValue=obj3
obj3.nextValue=obj4
obj4.nextValue=obj5
Llist=LinkedList()
Llist.head=obj1
Llist.deleteFromposition(3)
#Llist.printElement()
print(Llist.printElement())
