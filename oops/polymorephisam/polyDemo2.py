from multipledispatch import dispatch

class Shape:
    
    def __init__(self):
        pass
      
    @dispatch(int)
    def area(self,h):
        print("square area called...")    
    
    @dispatch(int,int)
    def area(self,h,w):
        print("rect area called...")    
    
    @dispatch(float)
    def area(self,r):
        print("circle area called..")    



s = Shape()
s.area(10)        
s.area(10,10)
s.area(10.10)