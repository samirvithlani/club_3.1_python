data = "hi this is india"
cap =""

for i in range(len(data)):
    #i=0,1,2,3
    #hi t
    if i==0 or data[i-1]== " ":
        if 'a'<= data[i]<='z':
            cap = cap+chr(ord(data[i])-32)#"H"
        else:
            cap = cap+data[i] 
    else:
        cap = cap+data[i]           


print(cap)        
        
        
