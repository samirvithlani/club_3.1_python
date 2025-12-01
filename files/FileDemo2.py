#read mode:
#location should avaialble...

# file = open("demo1.txt","r")
# f = file.read()
# print(f)


# file = open("th.txt","r")
# for i in file:
#     print(i,end="")


# file = open("th.txt","r")
# f = file.readline()
# print(f)

# file = open("th.txt","r")
# while True:
#     data = file.readline()
#     print(data,end="")
#     if not data:
#         break


# file = open("th.txt","r")
# data = file.readlines()
# print(data)

file = open("th.txt","r")
for i in file.readlines():
    print(i,end="")