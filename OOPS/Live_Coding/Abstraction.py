#abstraction
from abc import ABC,abstractmethod
class Food(ABC):
       @abstractmethod
       def price(self):
              pass
       @abstractmethod
       def type(self):
              pass
       def product(self):
              print("Briyani")
class Briyani(Food):
       def price(self):
            print("$100 price")
       def type(self):
              print("Non-veg")
       def product(self):
              print("Mutton Briyani")
customer1=Briyani()
customer1.price()
customer1.type()
customer1.product()
f1=Food()
