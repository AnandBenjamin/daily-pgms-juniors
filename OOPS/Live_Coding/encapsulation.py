#encapsulation

class Person:
    def __init__(self):
        self.name='swegasri'
        self._age=20
    def _display(self):
        print("private method")
    def age(self):
        self._display()
        return self.name+' '+str(self._age)
a=Person()
print(a.name)
print(a.age())
a.age=40
print(a.age)
