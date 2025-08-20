data = {1:"amit",2:"raj",33:"parth",101:"jay"}
print(data)
# removedElm = data.pop(33)
# print(f"removing {removedElm}")
# print(data)


if 333 in data:
    removedElm = data.pop(33)
    print(f"removing {removedElm}")
    print(data)
else:
    print("no item found !!")    
    

removeddata = data.popitem()    
print(removeddata)
print(data)