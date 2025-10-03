#decorators are pure pyhon function which can user to
#modify function behaviour without changing in function
#decorator will accept another function as argument
#decorator will return inner function object
#decorator wil call using @ top of function body

def order_food(func): #2 func == throw_party
    
    def inner(): #5
        print("ordering food !!!") #6
        func() #7 throw_party()
    
    return inner  #3  



@order_food #4
def throw_party(): #8
    print("throwing party!!") #9
    
throw_party()     #1

