users1 = {"ram","shyam","kush","luv"}
users2 = {"ram","shyam","arjun","sahdev"}


x = users1.union(users2)
print(x)

x = users1.intersection(users2)
print(x)

x = users1 & users2
print(x)

x = users1.difference(users2)
print(x)
x = users1 - users2
print(x)

x = users1.symmetric_difference(users2)
print(x)


users1 = {"ram","shyam","kush","luv"}
users2 = {"ram","shyam","arjun","sahdev"}


x = users1.issubset(users2)
print(x)

x = users1.issuperset(users2)
print(x)

users1 = {"ram","shyam","kush","luv"}
users2 = {"ram","shyam","arjun","sahdev"}


# users1.intersection_update(users2)
# print(users1)


mumbai = {"amit","summit","raj","parth"}
ahm = {"sanjay","priya","amit","kunnal"}
goa = {"niya","siya","jaya","amit","priya"}

#find who have attended all city event
#find who have attended ahm and goa not mumbai
#fina who have attended only goa
#find who have attended mumai and ahm
