# Basic function: Price after discount
def apply_discount(price,discount_percent =  5):
    total_amt = price  - (price  * discount_percent/100)
    return total_amt
print(f"Total amount after discount : {apply_discount(1000,10)}")
print(f"Total amount after discount : {apply_discount(500)}")

    