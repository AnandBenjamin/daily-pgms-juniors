class Employee:
       age=0
       def __init__(self,agefromuser):
              self.age=agefromuser
              print("Inside constructor")
              #print(self)
              
       def ageeligibility(self):
              
              if self.age>20:
                     print("adult")
              else:
                     print("child")
		
a=Employee(20)
#a.age=20
print(a.age)

b=Employee(26)
print(b.age)

a.ageeligibility()

b.ageeligibility()
