class Demo:
    
    no1 = 100 #static variable..
    #this
    def test(self):
        print("test function called...")
        print(self)
        #print(no1)
        print(self.no1)
        self.no2 = 200 #instance variable..
    def test2(self,p):
        print(self.no2)    



#object

d = Demo()
d.test() #class current object       
print(d)
print(d.no1)
print(Demo.no1)
print(d.no2)
d.test2(200)