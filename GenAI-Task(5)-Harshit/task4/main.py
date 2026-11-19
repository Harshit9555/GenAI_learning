# 1. Import shop_package.discount as disc
import shop_package.discount as disc

# 2. Import calculate_total directly
from shop_package.billing import calculate_total

# Import apply_tax
from shop_package.billing import apply_tax


# 3. Call every function

print("Percentage Discount:", disc.apply_discount(1000, 10))

print("Flat Discount:", disc.flat_discount(1000))

print("Total Bill:", calculate_total([100, 200, 300]))

print("Tax:", apply_tax(600))