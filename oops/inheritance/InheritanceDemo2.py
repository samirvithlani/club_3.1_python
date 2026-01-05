#multupule parent 1 child

class Father:
    
    def __init__(self):
        print("Father class Const called... ")
        self.amount = 90000
        self.car = "AUDI"

class Mother:
    
    def __init__(self):
        print("Mother class Const called...")        
        self.amount = 4500000
        self.bike = "RE"

class Son(Mother,Father):
    
    def __init__(self):
        super().__init__()
    
    def display(self):
        print(self.amount)
        print(self.bike)
        print(self.car)


s = Son()
s.display()        