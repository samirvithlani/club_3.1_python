#type of function
#built in | udf
#print,pop,remove,clear,sum,

# with r type with argument
# with r type without argument
#without r type with argument
#without r type without argument

#using def keyword can decalre function

def test():
    print('this is test functions..')

test()    

# def greet(name)->None:
#     print(f"Hello  {name}")

def greet(name:str)->None:
    print(f"Hello  {name}")

greet("MS")    
greet(100)


def add(a,b)->int:
    print("add function called...")
    return a + b


#x = add(10,20)
x = add("ram"," sharma")
print(f"ans = {x}")
print(f"ans = {add(100,200)}")
#add([],[])

#pass 2 list as param and concat each elem index vise and return new list
#[1,2,3],[2,3,4]
#[3,5,7]
