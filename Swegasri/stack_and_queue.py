class palindrome:
    lst=[]
    lst1=[]
    def push(self,value):
        self.lst.append(value)
    def enqueue(self,value):
        self.lst1.append(value)
    def dequeue(self):
        return self.lst1.pop(0)
    def pop(self):
        return self.lst.pop()
    
string=input()
a=palindrome()

for i in string:
    a.push(i)
    a.enqueue(i)
ispalindrome=True
for i in range(0,len(string)):
    if a.dequeue()==a.pop():
        continue
    else:
        ispalindrome=False
        break
if(ispalindrome):
    print("given str in palindrome")
else:
    print("Not a palindrome")
        
