class enca:
	def __init__(self, a, b):
		self.a1=a #obj.a1 = 10
		self.__b1=b #obj.__b1 = 10

	def __display(self):
		print ("a =", self.a1, " b=", self.__b1)

	def setb1(sel, bval):
		sel.__b1 = bval # obj.__b1 = bval

	def getb1(self):
		self.__display()
		return self.__b1


obj = enca(10,10)
obj.a1 = 15

obj.setb1(16)   # enca.setb1(obj,16)
print("a1", obj.a1) 
# print("b1", obj.__b1) 
print("b1", obj.getb1()) 


