#function as object

def test():
    print("hello this is test function !!")


x = test
print(x)
x()
#print(test)


def add(a,b):
    return a+b


ans = add
print(ans(10,20))
    