#inheritance----by NAVEEN UH!!!!

class Animal:
    def __init__(self,a,b):
        self.a=a+5
        self.b=b+5
        print("Animal",self)
        print(self.a,self.b)
    def speak(self):
        print("swega animal")
class dog(Animal):
    def __init__(self,a,b):
        print("Dog",self)
        #super().__init__(a,b)
        Animal.__init__(self,a,b)
        c=a+b
        print(c)
    def bark(self):
        print("mithra barking")


a=dog(1,2)
print("a",a)
a.bark()
a.speak()
