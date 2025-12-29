class Bank:
    
    #opbal = local
    def __init__(self,name,opbal):
        print("op bal",opbal)
        self.opbal = opbal
        self.name = name
    
    def withdraw(self,amount):
        print("withdraw method called...")
        return self.opbal - amount    

b1 = Bank("raj",1000)    
b2 = Bank("jay",2000)

x = b1.withdraw(9000)
print("updated op bal = ",x)