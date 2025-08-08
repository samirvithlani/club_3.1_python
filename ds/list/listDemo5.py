data = [[1,2,3],[4,5,6],[7,8,9]]
#3,3
#0 row --3
#1 row --3
print(data[0][0])
print(data[2][0])

# for i in range(0,len(data)):
#     for j in range(0,len(data[i])):
#         print(data[i][j],end=' ')
#     print()        

for i in data:
    for j in i:
        print(j,end=" ")
    print()    