season = input("enter season :")

match season:
    case "monsoon" | "MONSOON" :
        print("buy raincot")
    case "summer":
        print("buy sunscreen")  
    case _:
        print("invalid choice...")      
        