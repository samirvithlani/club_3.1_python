def wrapper():
    
    def product():
        print("hi i am product")
        return f"my price is {100}"
    
    
    return product


x = wrapper() #x == product
ans = x()
print(ans)

# x = wrapper() #x == product
# print(x)



# def converter(unit):
#     def to_meters(value):



converte("cm")
