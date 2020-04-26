class Student:

	def __init__(self,m1, m2):
		self.mark1=m1
		self.mark2=m2

	def display(self):
		print("marks = " , self.mark1, ",", self.mark2)

	def __add__(self, anoobj):
		newmrk1 = (self.mark1 + anoobj.mark1)/2
		newmrk2 = (self.mark2 + anoobj.mark2)/2
		newstud =  Student(newmrk1,newmrk2)
		return newstud

	def __gt__(self, anoobj):
		tots1mrk = self.mark1 + self.mark2
		tots2mrk = anoobj.mark1 + anoobj.mark2
		return tots1mrk > tots2mrk
		

s1 = Student(50,70)
s2 = Student(40,90)
s1.display()
s2.display()
s3 = s1 + s2 # s1.__add__(s2)  --> Student.__add__(s1,s2)
s3.display()  

print (s2 > s1) 