data = {"class 11":["raj","parth","amit"],"class 12":["parth","sumit","ajay"]}
print(data)
print(data["class 12"])

#manuplation

#list..
data["class 11"].append("khushi")
#list
data["class 12"].remove("sumit")

for i,j in data.items():
    print(i,end=" ")
    for stu in j:
        print(stu,end=" ")
    print()    



#
#data    ={""}

data = {"class 11":["raj","parth","amit"],"class 12":["parth","sumit","ajay"]}
#{"class 11":3}

newData = {}

for i,j in data.items():
    #newData[i]= len(j)
    newData.update({i:len(j)})
print(newData)    


#sales= {"monday":[10,20,30],"tuesday":[20,30,40]}
#salescount ={"monday":60,..}