#Linked List
"""
1.Create a List box  ( data,address)
2.Add elements to List Box

       [10,200]-->[20,300] --> [30,400] -->[40,500]-->[50,null]

3.Create a Linked List
4.Forming a chain
       head-->Pointing to [1,null]


"""
class Node:
       def __init__(self,a): #initialized during obj creation
              self.data=a
              self.nextValue=None
              
class LinkedList:
       
       def __init__(self):
              self.head=None
            #   obj1=>address
       
       def appendElement(self,element):
              
              if(self.head==None):
                     self.head=element
                     print("Head is null so adding new element")
              else:
                     current=self.head                     
                     #self.head.nextValue=element
                     while(current.nextValue!=None):
                            current=current.nextValue
                     current.nextValue=element
       
       def printElement(self):
              l=[]
              current=self.head
              while(current!=None):
                     l.append(current.data)
                     #print(current.data)
                     current=current.nextValue
              return l
       
       def countofList(self):
              current=self.head
              count=0
              while(current!=None):
                     count+=1
                     current=current.nextValue
              return count
       
       def positionValue(self,userposition):
              current=self.head
              position=1
            #   print("size",self.countofList())
              
              if(self.countofList()>=userposition):
                     while(userposition!=position):
                            current=current.nextValue
                            position+=1
                     return current.data
              else:
                     print("position is greater than list size")
                     return -1
                     
       def deleteLast(self):
              current=self.head
              while(current.nextValue!=None):
                     prev=current
                     current=current.nextValue
              prev.nextValue=None
              return current
              
       def deleteFirst(self):
              current=self.head
              self.head=current.nextValue
              return current.data
       
       def insertAtPosition(self, position, newValue):
           newElement=Node(newValue)
           if(position==1):
               newElement.nextValue=self.head
               self.head=newElement
           else:
               current=self.head
               for i in range(1, position-1):
                   current=current.nextValue
               newElement.nextValue=current.nextValue
               current.nextValue=newElement
               
       def deleteValue(self, value):
           current=self.head
           prev=current
           while(current.data!=value):
               prev=current
               current=current.nextValue
           if(prev==current):
               self.head=current.nextValue
           else:
               prev.nextValue=current.nextValue
               
       def deleteFromPosition(self, userPosition):
           current=self.head
           position=1
           prev=current
           while(userPosition!=position):
               position+=1
               prev=current
               current=current.nextValue
               
           if(prev==current):
               self.head=current.nextValue
           else:
               prev.nextValue=current.nextValue
           
        #   return current.data
        #   if(current.data==value):
                     
       
obj1=Node(1)  #object created and value passed
# print(obj1)
obj2=Node(2)
# print(obj2)
obj3=Node(3)
obj4=Node(4)
obj5=Node(5)
#print(obj3)
"""
obj1.nextValue=obj2
print(obj1.nextValue)
obj2.nextValue=obj3

print(obj2.nextValue)
"""
Llist=LinkedList()
#print(Llist)
Llist.appendElement(obj1)
# print(Llist.printElement())
#print(Llist.head)
#print(Llist.head.data)
#print(Llist.head.nextValue)
Llist.appendElement(obj2, obj1)
# print(Llist.printElement())
#print(Llist.head.nextValue)
#print(Llist.head.nextValue.data)
Llist.appendElement(obj3)
# print(Llist.printElement())
Llist.appendElement(obj4)
Llist.appendElement(obj5)
print(Llist.printElement())
#print(Llist.head.nextValue)
#print(Llist.head.nextValue.data)
#obj1.nextValue=obj2
# print(obj1.nextValue.data)
#obj2.nextValue=obj3
# print(obj2.nextValue.data)
print "Count:",Llist.countofList()
print "Value at position 2 is:", Llist.positionValue(2)
#print(Llist.deleteLast().data)
print Llist.printElement()
# print(Llist.deleteFirst())
# print(Llist.printElement())
# 1,2,3,4,5 => 4 Pos, 6 => 1,2,3,6,4,5
Llist.insertAtPosition(4,6)
print Llist.printElement()
Llist.deleteValue(1)
print Llist.printElement()
Llist.deleteFromPosition(1)
print Llist.printElement()