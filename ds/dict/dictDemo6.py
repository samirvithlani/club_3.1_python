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