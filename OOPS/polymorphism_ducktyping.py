# from abc import ABC, abstractmethod
# class comp(ABC):
# 	@abstractmethod
# 	def display():
# 		pass

class desktop():
	def display(self):
		print("in desktop")

class laptop():
	def display2(self):
		print("in laptop")




class Computer:
	def displprocess(self,a):  # (cobj,lobj )
		print("computer")
		a.display()  # lobj.display()  --> laptop.display(lobj)
 
cobj = Computer()
dobj = desktop()
lobj = laptop()
cobj.displprocess(dobj)
cobj.displprocess(lobj)