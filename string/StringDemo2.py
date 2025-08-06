data = "ajay"
copyData=  ""

# for i in range(len(data)):
#     #""  = ""+a
#     copyData = copyData + data[i]


# print(copyData)    


#ajay - 4
#0123
for i in range(len(data)-1,-1,-1):
    copyData = copyData + data[i]

print(copyData)    