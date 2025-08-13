#[1,10]
# data =[]
# for i in range(1,11):
#     data.append(i)

# print(data)    

data =[i for i in range(1,11)]
print(data)

x= [1,2,3,4,5]
#x2= [1,4,9,16,25]
# x2=[]
# for i in x:
#     x2.append(i**2)
x2 = [i**2 for i in x]
print(x2)    


users = ["ram","shyam","amit","sumit","kunal"]
#upperUser =[]
# for i in users:
#     upperUser.append(i.upper())
upperUser = [i.upper() for i in users]
print(upperUser)    

#sales = [100,200,300,400,500] #10% profit add