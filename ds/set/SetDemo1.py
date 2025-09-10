data = {100,20,30,100,40,45,67,89}
print(data)

data.add(999)
print(data)

#data.update([999,78,56])
data.update({999,78,56})
print(data)

removedElm = data.pop()
print(f"removing element {removedElm}")
print(removedElm)

data.remove(30)
print(data)

#data.clear()

#print(data[0])

for i in data:
    print(i)
    

x= 'india'    
x1 = "".join(set(x))
print(x1)

