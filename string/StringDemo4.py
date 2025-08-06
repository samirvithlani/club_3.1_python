# email  ="samir@gmail.com"

# if "@" in email:
#     print("true")



# name = "java"    
# #x = name.index("p")
# x = name.find("a")
# print(x)



name = "java"

flag = -1

for  i in range(len(name)):
    if name[i] == "p":
        flag = i
        break
print(flag)        