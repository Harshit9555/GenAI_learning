# 6.Magic Methods & Operator Overloading
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        
    def get_info(self):
        print(f"The Price are: {self.price} for product {self.name}")
        
    def __str__(self):
        return f"{self.name} is the name and {self.price} is the price int the {self.category} category"
    
    def __add__(self,other):
        return self.price + other.price
    
# Object Creations
obj1 = Product("Pen",20,"Stationary")
obj2 = Product("Mobile",25000,"Electronics")
sum = obj1 + obj2
print(sum)
print(obj1)
obj1.get_info()

    
        

