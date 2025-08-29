data = {"gujarat":"gandhinagar","maharashtra":"mumbai","up":"lucknow"}

print(data)
print(data["gujarat"])

data["rajasthan"]="Jaipur"
print(data)


removedValue = data.pop("maharashtra")
print(f"removing ..",removedValue)
print(data)

removedData = data.popitem()
print("removing",removedData)
print(data)
