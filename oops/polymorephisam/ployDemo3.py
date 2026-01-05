#overrdiding...

class Parent:
    
    def __init__(self):
        print("init called...")
    
    def test(self):
        print("test from parent..")    


class Child(Parent):
    
    def __init__(self):
        super().__init__()
    
    def test1(self):
        print("overrided method from parent....")            

c = Child()
c.test()        