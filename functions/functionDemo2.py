#default argument 

def add(a=0,b=0):
    return a+b


print(add(10,30))


#named param function

def getUserData(id,name,age,salary):
    print(f"id = {id}")
    print(f"name = {name}")
    print(f"age = {age}")
    print(f"salary = {salary}")

# getUserData(1,"raj",23,34000)
# getUserData("raj",34000,23,1)    
# getUserData(name="raj",age=23,id=101,salary=23456)

#args 
def names(*args):
    print(args)

#names("raj","parth")    
names()
names("raj","parth","jay")        


def getmarks(*args,x):
    print(args)
    print(x)

#getmarks(10,20,30)    
getmarks(10,20,x=40)    

def getmarks1(x,*args):
    print(args)
    print(x)

#getmarks(10,20,30)    
getmarks1(10,20,30)    

def getmarks2(*args,x,y):
    print(args)
    print(x)

#getmarks(10,20,30)    
#getmarks2(10,20,x=40,50) #compile time error if u have pass any name param before then all param must be name param    

