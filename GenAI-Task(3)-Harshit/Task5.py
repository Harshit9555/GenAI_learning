# Using filter(): Filter Expensive Products
prices = [100,250,400,1200,50,2000,850]
greater_prices = list(filter(lambda price:price>500,prices))
less_or_equal_prices = list(filter(lambda price:price<=500,prices))
print(f"The price which are greater than 500 are : {greater_prices}")
print(f"The price which are leass than or equal to 500 are : {less_or_equal_prices}")


