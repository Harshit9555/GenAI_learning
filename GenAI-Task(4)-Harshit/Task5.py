# Ask the user for 3 product names and prices
products = []

for i in range(3):
    name = input(f"Enter product {i + 1} name: ")
    price = float(input(f"Enter price of {name}: "))
    products.append((name, price))

# Write products to a file
with open("products.txt", "w") as data:
    for name, price in products:
        data.write(f"{name} | {price:.2f}\n")

# Read and print the file
with open("products.txt", "r") as data:
    print("\nProduct Information:")
    for line in data:
        print(line.strip())