users = ["bob","amit","ram","madam","naman","malayalam","seeta"]

userwithpalndrome = {i:len(i) for i in users if i == i[::-1]}
print(userwithpalndrome)


numners = [11,203,405,60,32,1103,4450,202,24044,22,10]

numners1 = {i:i**2 for i in numners if i %2==0}
print(numners1)

#users = ["bob","amit","ram","madam","naman","malayalam","seeta"]

userwithlabel = {i:"palindrom" if i == i[::-1] else "NOt palindrome" for i in users}
print(userwithlabel)