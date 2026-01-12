#cust ex
class InvalidDataException(Exception):
    def __init__(self, *args):
        super().__init__(*args)



name = "rohit_sharma"        

try:
    if " "in name:
        raise InvalidDataException("string is not valid,,")
except InvalidDataException as e:
    print(e)        
else:
    print(name)    