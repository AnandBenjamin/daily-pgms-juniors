class palindrome:
    lst=[]
    
    string=[]
    def push(self,value):
        self.lst.append(value)






string=input()
a=palindrome()

for i in string:
    a.push(i)
ispalindrome=True
for i in string:
    if i==a.lst.pop():
        continue
    else:
        ispalindrome=False
        break
if(ispalindrome):
    print("given str in palindrome")
else:
    print("Not a palindrome")
        
