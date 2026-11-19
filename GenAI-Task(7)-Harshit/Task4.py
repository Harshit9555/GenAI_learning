# 4. Polymorphism
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        
    def get_info(self):
        print(f"The name of product are: {self.name} and the price are : {self.price} which lies in {self.category} category")
        
#Laptop class        
class Laptop(Product):
    def __init__(self,name,price,category,product_rating):
        super().__init__(name,price,category)
        self.product_rating = product_rating
        
    def get_info(self):
            print(f"The name of product are: {self.name} and the price are : {self.price} which lies in {self.category} category and product rating are: {self.product_rating}")
            
#Mobile class
class Mobile(Product):
    def __init__(self,name,price,category,product_rating):
        super().__init__(name,price,category)
        self.product_rating = product_rating
        
    def get_info(self):
                print(f"The name of product are: {self.name} and the price are : {self.price} which lies in {self.category} category and product rating are: {self.product_rating}")
        
#Object creation
mobile = Mobile("Samsung",25000,"Electronics",4.5)
mobile.get_info()
laptop = Laptop("Asus VivoBook",75000,"Electronics",4.7)
laptop.get_info()