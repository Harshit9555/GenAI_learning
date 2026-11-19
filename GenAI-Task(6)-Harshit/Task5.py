cart = []
while True:
    try:
        prices = input("Enter the prices: ")
        if prices.lower() == 'q':
            break
        prices = float(prices)
        if prices <0:
            raise ValueError ("Negative price")
        cart.append(prices)
    except ValueError as ex:
        print(ex)
    finally:
        total_bill = sum(cart)
        print(f"Total items are: {len(cart)}")
        print(f"Total bill are: {total_bill}")
    
    