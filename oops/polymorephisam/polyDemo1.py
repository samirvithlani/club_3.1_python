class Shape:
    
    def __init__(self):
        print("default const...")
    
    
    def area(self,h,w):
        print("2 param area called..")    

    def area(self,x):
        print("1 param area called...")    

s = Shape()
s.area(100)        