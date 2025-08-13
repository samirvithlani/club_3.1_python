numners = [1,2,3,4,5,6,7,8,9,90,11,223,4]

# evenList =[]
# for i in numners:
#     if i %2==0:
#         evenList.append(i)

# evenList = [i for i in numners if i %2==0]
# print(evenList)        

# labellist =["event" if i %2==0 else "odd" for i in numners]
# # for i in numners:
# #     if i%2==0:
# #         labellist.append("even")
# #     else:
# #         labellist.append("odd")    

# print(labellist)        



users = ["krisha","khushi","krishna","kairvi","kinjal"]

# userwith5 = [i for i in users if len(i)>6]        
# print(userwith5)

userwith5 = [i.upper() for i in users if len(i)>6]        
print(userwith5)


users = ["naan","naman","bob","parth","jay","madam"]

# palindromeNames = [i for i in users if i == i[::-1]]
# print(palindromeNames)

palindromeLabels = ["palindrome" if i == i[::-1] else "not palindrome" for i in users]
print(palindromeLabels)