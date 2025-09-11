# def getUserData(**kwargs):
#     print(kwargs) #dict


# #getUserData(10,20,30)    error
# getUserData(name="amit",age=23,status=True,x=100,y=200,z=500)

# def getUserData(**kwargs,x): error
#     print(kwargs) #dict


# #getUserData(10,20,30)    error
# getUserData(name="amit",age=23,status=True,x=100,y=200,z=500)

def getUserData(*args,**kwargs):
    print(kwargs) #dict


#getUserData(10,20,30)    error
getUserData(name="amit",age=23,status=True,x=100,y=200,z=500)