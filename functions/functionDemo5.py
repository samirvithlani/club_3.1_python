#hof

def calling():
    print("calling,,,,,")


def call(x):
    print(x) #x == calling
    x()



# call(10)
# call("ram")
# call(False)
# call([])    
call(calling)