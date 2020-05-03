#using atribute
class Person:
  def __init__(self): 
    self.name = 'Naveen'
    self.__age = 20

  def __display(self):
      print("private method")
    
  def Printage(self):
      self.__display()
      return self.name +' ' + str(self.__age)
       
P = Person()
print(P.name)
print(P.Printage())

#print(P.__display())
#'Person' object has no attribute '_age'


#accessing function

"""class SeeMee:
  def youcanseeme(self):
    return 'you can see me'
    
  def __youcannotseeme(self):
    return 'you cannot see me'
       
Check = SeeMee()
print(Check.youcanseeme())
print(Check.__youcannotseeme())"""


"""class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def set_wallet_balance(self, amount):
        if amount < 1000 and amount>  0:
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance

c1=Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())"""
