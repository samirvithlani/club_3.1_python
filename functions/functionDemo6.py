
def science(stuname):
    print(f"your admission confirm in science {stuname}")

def comm(stuname):
    print(f"your admission confirm in comm {stuname}")

def arts(stuname):
    print(f"your admission confirm in arts {stuname}")


def admisison(cb):
    print("admission function called !!")
    cb("ram") #sci,comm,arts


admisison(science) 
admisison(comm)   