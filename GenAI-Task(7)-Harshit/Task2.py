# 2. Constructor and  Encapsulation..
class  Product:
    def __init__(self,name,price,category):
        self.name = name
        self.__price = price   #Private
        self.category = category
        
    # getter
    def get_price(self):
        print(f"The price  are : {self.__price}")
    
    #setter
    
    def set_price(self,new_price):
        if new_price>0:
            self.__price = new_price
        else:
            print("Price can't be negative !!")

#object creation
obj = Product("Pen",20,"Stationary")
obj.get_price()
obj.set_price(50)
obj.get_price()
    
    
    
    

