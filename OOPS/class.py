class Person:
	def __init__(self, age1, name1): # s1,14, "Raj"
		self.name = name1   #s1.name = "raj"
		self.age = age1
		print("constructor")

	def display(self):
		print("age", self.age)	
		print("name", self.name)	


class Pupil:
	def display(self):
		print("display2")

class Student( Person):
	def __init__(self, std1):
		self.std = std1  #s1.std = 7
		 # s1,14, "Raj"

	# def display(self):	
	# 	print("std", self.std)
	# 	Person.display(self)

s1 = Student(7) 
s1.display() #Student.display(s1)
s1.display()

# p1 = Person(23, "siva") #Person(p1,23)

# p1.display(5)  #Person.display(p1,5)

# p2 = Person(13, "balu")
# p2.display(3)  #Person.display(p2, 6)
