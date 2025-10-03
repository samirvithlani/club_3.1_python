def safe_div(func):
    
    def inner(x,y):
        print("inner called..",x,y)
        if y ==0:
            print("cannot divide by zero:")
        else:
            func(x,y)
    
    return inner


@safe_div
def div(no1,no2):
    print(no1/no2)                
   
div(10,0)    