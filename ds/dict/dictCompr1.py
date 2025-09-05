#{1:1,2:2,3:3,4:4,5:5}

#data ={i:i for i in range(1,6)}
data ={i:i**2 for i in range(1,6)}

# for i in range(1,6):
#     data[i]=i

print(data)    


users = ["amit","sumit","ram","shyam","kunal"]
marsk = [23,22,24,21,19]
#{a:"amit",}

users1 = {i[0]:i for i in users}
print(users1)

#{"amit":4}

users2 = {i:len(i) for i in users}
print(users2)

#zip
userwithmarks = {i:j for i,j in zip(users,marsk)}
print(userwithmarks)
