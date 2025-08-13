data = (1,2,3,4,56,7)
print(data)
print(type(data))


x = data.count(1)
print(x)

ind = data.index(56)
print(ind)

data[0] = 1000

datalist = list(data)
datalist.append(100)
data = tuple(datalist)
print(data)