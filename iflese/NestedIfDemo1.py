age = int(input("enter age : "))
status = input("enter status ['active','not active'] :")

if status== "active":
    print("user is active...")
    if age>=18:
        print("user can vote..")
    else:
        print("user can not vote..")    
else:
    print("user is not active..")        