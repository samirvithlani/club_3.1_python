#ano...
x = lambda : print("hello this is lambda")
x()

x1 = lambda a: print("this is param",a)
x1(12)

ans = lambda a,b : a+b
print(ans(20,30))

findMax = lambda a,b : a if a >b else b
print(findMax(100,20))


findMax1 = lambda a,b,c : a if a>b and a>c else(b if b>c else c)
print(findMax1(10,20,199))



def checkvalid(x):
    if " "in x:
        return False
    else:
        return True


x3 = lambda x: checkvalid(x)    
print(x3("ram"))