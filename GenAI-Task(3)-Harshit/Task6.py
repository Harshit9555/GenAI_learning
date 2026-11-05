def process_prices(prices):
    ans = []
    discount_prices = list(map(lambda prices: prices - (0.10*prices),prices))
    discount_prices_filter = list(filter(lambda x: x>300,discount_prices))
    ans.append(f"Prices after 10% discount: {discount_prices}")
    ans.append(f"Discounted price above 300 : {discount_prices_filter}")
    return ans
print(process_prices([100,500,900,50,750]))
    