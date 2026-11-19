# 3. Inheritance(Single-Level)
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        
    def get_info(self):
        print(f"The Price are: {self.price} for product {self.name}")
    
class ElectronicProduct(Product):
    def __init__(self,name,price,category,warranty_years):
        super().__init__(name,price,category)
        self.warranty_years = warranty_years
        
    def get_info(self):
        print(f"The product are : {self.name},Price  are: {self.price} and the Warranty are : {self.warranty_years} yrs")

    
#Object creation
obj1 = Product("CPU",10000,"Electronics")
obj1.get_info()
obj2 = ElectronicProduct("Mobile",50000,"Electronics",4)
obj2.get_info()
    