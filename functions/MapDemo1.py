users = ["ram","shyam","amit","sumit","neha"]

#upperUser = [i.upper() for i in users]
#upperUser = map(lambda x:x.upper(),users)
#upperUser = map(lambda x:x+"-",users)
upperUser = map(lambda x:x[0]=="s",users)
print(list(upperUser))

sname = filter(lambda x:x.startswith("s"),users)
print(list(sname))

