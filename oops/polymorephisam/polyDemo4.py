#overrdiding...
from abc import ABC,abstractmethod
class Parent(ABC):
    
    def __init__(self):
        print("init called...")
    
    @abstractmethod
    def test(self):
        pass 


class Child(Parent):
    
    def __init__(self):
        super().__init__()
    
    def test(self):
        print("overrided method from parent....")            

c = Child()
c.test()        