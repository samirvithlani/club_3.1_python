from abc import ABC,abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using credit card")

class DebitCardPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using Debit card")        

class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")        


payments = [CreditCardPayment(),DebitCardPayment(),UPIPayment()]        
for p in payments:
    p.pay(500)
        
    