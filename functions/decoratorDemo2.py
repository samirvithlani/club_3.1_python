
no1 = int(input("enter no 1 : "))
no2 = int(input("enter no 2 : "))



def safe_div(func):
    def inner():
        if no2 ==0:
            print("cannot divide by zero")
        else:
            func()
    
    return inner           

@safe_div
def div():
    print(no1/no2)

div()    