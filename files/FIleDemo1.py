#file demo
#3 operations open file read/write close file...
#file class- -> mode r w a r+ w+
#path relative path abs
#th.txt ->D:\royal\club3.1-python\th.txt
#files\FileDemo1.py:D:\royal\club3.1-python\files\FIleDemo1.py

# file = open("demo1.txt","a")
# file.write("hi this is first line using write 1()")
# file.close()



# f = open("demo2.txt","w")
# print("hi this is file from print()",file=f)
# f.close()


# with open("demo3.txt","a") as f:
#     f.writelines(["hi","\nthis","\nis","\nindia"])
#     #file is auto close..

# #f.write("")        file close..


# name = "amit"
# age =23
# gender= "male"

# file = open("files/user.txt","a")
# file.write(f"name ={name}")
# file.write(f"age ={age}")
# file.write(f"gender ={gender}")


data = {"name":"raj","age":23,"gender":"male"}

file = open("files/emp.txt","a")
for i,j in data.items():
    file.write(f"\n {i} = {j}")
file.close()    
