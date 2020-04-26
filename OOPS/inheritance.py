class vehicle:
	def __init__(self,colr):
		self.color = colr

	def disp(self):
		print ("in vehicle")


class bike():
	def __init__(self,price):
		self.price = price

	def disp(self):
		print ("in bike")



class sportsbike(bike,vehicle):
	def __init__(self,modl,price,colr):
		self.model = modl
		bike.__init__(self,price)

	def display(self):
		print ("modl", self.model)
		print ("price", self.price)
		# print ("colr", self.color)


bike1 = sportsbike("A1", 500, "red")
bike1.display()
bike1.disp()
