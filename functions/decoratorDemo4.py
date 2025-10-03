
def check_access(func):
    
    def inner(role):
        if role =="admin":
            func(role)
        else:
            print("no access found!!")    
    
    return inner            


@check_access
def access_data(role):
    print("accessing data",role)

access_data("abc")    