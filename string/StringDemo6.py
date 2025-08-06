data = "amit"
print("startsWith",data.startswith("a"))
print("startsWith",data.endswith("t"))

data = "Abc"
print("isAlpha",data.isalpha())
print("isnum",data.isnumeric()) #isdigit
print("isalnum",data.isalnum())
print("islower",data.islower()) #isUpper
print("ispace",data.isspace())
print(data.istitle()) #titleCase

data = ""
print(data.isprintable())