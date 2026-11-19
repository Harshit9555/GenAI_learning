# Basic Class & Object Creation
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print(f"The name of product is: {self.name},price of product is {self.price} and category is {self.category}")
        
    def apply_discount(self,percent):
        return f"Price after discount is: {self.price - self.price * percent/100 }"

#Object Creation

obj1 = Product("Pen",20,"Stationary")
obj1.get_info()
disc_amt = obj1.apply_discount(5)
print(disc_amt)

obj2 = Product("Mobile",40000,"Electronics")
obj2.get_info()
    