
def science(stuname):
    print(f"your admission confirm in science {stuname}")
    return f"Hello {stuname} welcome"

def comm(stuname):
    print(f"your admission confirm in comm {stuname}")
    return f"Hello {stuname} welcome"

def arts(stuname):
    print(f"your admission confirm in arts {stuname}")
    return f"Hello {stuname} welcome"


def admisison(cb,name):
    print("admission function called !!")
    message = cb(name) #sci,comm,arts
    print(message)
    return "admission process done.."



name = input("enter your name :")
pers = float(input("enter pers :"))

message = None

if(pers>80):
    message = admisison(science,name)
elif pers>70:
    message = admisison(comm,name)
else:
    message = admisison(arts,name)        

print(message)    