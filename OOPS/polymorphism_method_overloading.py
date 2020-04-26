class Student:
	def __init__(self,mrk1, mrk2):
		self.mark1 = mrk1
		self.mark2 = mrk2

	def display(self):
		print ("mark1 - ",self.mark1," mark2 - ",self.mark2)

	def __add__(self,other):
		return Student((self.mark1+other.mark1)//2,(self.mark2+other.mark2)//2)


	def add(self,a=None,b=None,c=None):
		if a == None and b == None and c == None:
			return 0
		elif b == None and c == None:
			return a
		elif  c == None:
			return a+b 
		else:
			return a+b+c


s1 = Student(60,70)
s2 = Student(40,80)
s1.display()
s2.display()
s3 = s1 + s2
s3.display()

print (s1.add(3,4,5))
print (s1.add(4,5))
print (s1.add(3.5))
print (s1.add())