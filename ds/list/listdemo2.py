users =["ram", "shyam", "hari","sita"]

users.append("gita")  # add an item to the end of the list
print(users)
users.extend(["mohan", "sita"])  # add a list as an item
print(users)
users.insert(2, "laxman")  # insert an item at a specific index
print(users)


#removedElm = users.pop()
removedElm = users.pop(2)
print(f"removed element: {removedElm}")
print(users)

if "gita" in users:
    print("gitaa is present")
    users.remove("gita")
print(users)
