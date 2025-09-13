def calc(*args):
    match args[0]:
        case "add":
            return sum(args[1:])
        case "sub":
            sub =args[1]
            for i in args[1:]:
                sub = sub -i
                return sub
                


print(calc("add",102,20,30))
print(calc("sub",100,20,30))
