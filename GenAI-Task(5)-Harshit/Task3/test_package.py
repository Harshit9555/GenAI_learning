from shop_package.discount import apply_discount, flat_discount

from shop_package.billing import calculate_total, apply_tax

print("Discount:", apply_discount(1000, 10))

print("Flat Discount:", flat_discount(1000))

print("Total Bill:", calculate_total([100, 200, 300]))

print("Tax:", apply_tax(600))