# 7. Mini Project: Simple Inventory System (OOP  Only)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        return self.price + other.price

    def __str__(self):
        return f"Name: {self.name}, Price: ₹{self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product.name, "added successfully!")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(name, "removed successfully!")
                return

        print("Product not found!")

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

    def show_all_products(self):
        print("\nAll Products")
        for product in self.products:
            print(product)

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        product = Product(name, price, quantity)
        self.inventory.add_product(product)

    def show_summary(self):
        print("\nSTORE SUMMARY")
        print("Store Name:", self.store_name)
        print("Total Items:", len(self.inventory.products))
        print("Total Inventory Value: ₹", self.inventory.get_total_value())
        self.inventory.show_all_products()
        
#Testing...

store = Store("Harshit's Store")

p1 = Product("Laptop", 50000, 2)
p2 = Product("Mobile", 20000, 3)
p3 = Product("Keyboard", 1500, 5)

store.inventory.add_product(p1)
store.inventory.add_product(p2)
store.inventory.add_product(p3)

store.show_summary()


print("\n Operator Overloading")
print("Combined price of Laptop and Mobile:", p1 + p2)

store.inventory.remove_product("Keyboard")


store.show_summary()
