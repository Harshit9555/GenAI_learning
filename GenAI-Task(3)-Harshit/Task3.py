# Lambda function: GST Calculator
price = 100
gst = lambda price: (price + (0.18 * price))
print(gst(price))