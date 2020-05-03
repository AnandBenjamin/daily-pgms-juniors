#inheritance----by NAVEEN UH!!!!

class Animal:
    def __init__(self):
        """self.a=a+5
        self.b=b+5
        print("Animal",self)
        print(self.a,self.b)"""
    def speak(self):
        print("swega animal")
class dog:
    """def __init__(self,a,b):
        print("Dog",self)
        #super().__init__(a,b)
        Animal.__init__(self,a,b)
        c=a+b
        print(c)"""
    def speak1(self):
        print("mithra barking")


class dog2(dog,Animal):
    def display(self):
        print("its playing")



a=dog2()
#print("a",a)
"""a.bark()
a.speak()
a.play()"""
a.speak()
a.speak()
a.display()
