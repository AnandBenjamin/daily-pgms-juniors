#polymorphism.Duck type


class Pycharm:
        
    def excute(self):
        print("Compiling")
        print("Running")
    

class MyEditor:
    
    def excute1(self):
        print("Covertion Check")
        print("Spell Check")
        print("Compiling")
        print("Running")
    

class Laptop:
    def code(self,ide):
        ide.excute()

        

ide=Pycharm()   #ide=MyEditor()
Lap1=Laptop()
Lap1.code(ide)
