# def outer():
    
#     print("outer called...")
#     def inner():
#         print('innerr called...')
     
#     inner()

# outer()

# def outer(x):
    
#     print("outer called...",x)
#     def inner():
#         in1 = 1000
#         print('innerr called...',x,in1)
    
#     #print("outer in1",in1) 
#     inner()

# outer(100)


def outer(x):
    
    print("outer called...",x)
    def inner():
        in1 = 1000
        print('innerr called...',x,in1)
        return "hi i am room"
    
    #print("outer in1",in1) 
    msg = inner()
    print(msg)

outer(100)
