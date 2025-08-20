# data ={}
# print(data)
# print(type(data))


data = {"Gujarat":"Gandhinagr","Maharashtra":"Mumbai","UP":"Lucknow","Gujarat":"Ahmedabad"}
print(data)
print(data["Gujarat"])
print(data.get("Gujarat"))

#keys
k = data.keys()
print(list(k))
v = data.values()
print(list(v))

kv = data.items()
print(list(kv))

for i,j in data.items():
    print(i,"-",j)
    