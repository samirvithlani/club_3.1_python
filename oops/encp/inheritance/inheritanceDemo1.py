class Parent:
    car = "BMW"
    def __init__(self):
        print("parent class const called...")
        self.prop = 2000

class Child(Parent):
    
    def __init__(self):
        super().__init__()
        print("child class const called..")
    
    def display(self):
        print("property from parent = ",self.prop)        
        print(self.car)
        print(Parent.car)


c = Child()        
c.display()