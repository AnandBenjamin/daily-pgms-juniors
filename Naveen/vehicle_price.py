class Vehicle:
    def __init__(self,name,color,kind,value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle("ford","red","mustang",600000)
"""car1.name = "Ford"
car1.color = "red"
car1.kind = "mustang sport"
car1.value = 6000000.00"""

car2 = Vehicle("BMW","blue","b4",80000)
"""car2.name = "BMW"
car2.color = "blue"
car2.kind = "b4 van"
car2.value = 8000000.00"""

print(car1.description())
print(car2.description())
