data = {}
while True:
    choice = int(input("enter 1 for continue and 0 for exit"))
    
    if choice ==1:
        name = input("enter name :")
        sal = int(input("enter sal :"))
        data[name]=sal
    else:
        break   

print(data)     
    