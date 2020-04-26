from abc import ABC, abstractmethod


class computer(ABC): #abstract class computer 
	@abstractmethod
	def read(self):
		pass
	@abstractmethod
	def write(self):
		pass


class desktop(computer):
	def read(self):
		print("reading")
	def write(self):
		print("writing")

d = desktop()
d.read()
d.write()
