# 5. Abstraction(using Abstract Base class)
from  abc import abstractmethod
class Payment:
    @abstractmethod
    def process_payment(self):
        pass
    
class  CreditCardpayment(Payment):
    def process_payment(self):
        print("Credit card Payment Process")
        
class UPIPayment(Payment):
    def process_payment(self):
        print("UPI Payment process")

#Object Creations
obj1 = CreditCardpayment()
obj1.process_payment()
obj2 = UPIPayment()
obj2.process_payment()

        
        