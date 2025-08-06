data  ="ahmedabad"

x = data[:]
print(x)
print(data[::])
print(data[0:])
print(data[1:])
print(data[1:4])
print(data[1:7:2])

print(data[0])
print(data[-1])
print(data[0:-2])
print(data[::-1])


name=  "naman"

if name== name[::-1]:
    print("palindrome..")
    

print(name[2:])