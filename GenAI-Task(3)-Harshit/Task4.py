# using map(): Apply  GSt to list of  prices
prices = [100,250,400,1200,50]
prices_with_gst = list(map(lambda price : price + (0.18 * price),prices))
print(f"Original Price : {prices}")
print(f"Prices  after GST: {prices_with_gst}")