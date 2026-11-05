# Python Functions Practice

## 📌 About the Project

This project contains Python practice exercises focused on functions, lambda expressions, recursion, `map()`, `filter()`, and combining these concepts to solve real-world problems. It also includes a mini menu-driven program for managing prices.

## 🎯 Tasks Covered

### Task 1: Price After Discount
- Create an `apply_discount(price, discount_percent=5)` function.
- Calculate the price after applying a discount.
- Apply a default discount of 5% when no discount is specified.
- Test custom and default discounts.
- Optionally ensure the discount never exceeds 60%.

### Task 2: Recursive Function — Factorial
- Create a recursive `factorial(n)` function.
- Calculate the factorial of a non-negative integer.
- Handle the base cases `0! = 1` and `1! = 1`.
- Display an error message for negative input.

### Task 3: Lambda Function — GST Calculator
- Use a lambda function to calculate the price after adding 18% GST.
- Test the function with a price of ₹100.
- Optionally combine GST and discount calculations.

### Task 4: Using `map()` — Apply GST
- Use `map()` to apply 18% GST to a list of prices.
- Print the original prices and the prices after GST.

### Task 5: Using `filter()` — Filter Expensive Products
- Filter prices greater than ₹500.
- Create another list containing prices less than or equal to ₹500.
- Display both lists.

### Task 6: Combined Utility Function
- Create a `process_prices(prices)` function.
- Use `map()` and a lambda function to apply a 10% discount.
- Use `filter()` to select discounted prices above ₹300.
- Return both the discounted prices and the filtered prices.

### Task 7: Mini Problem — Menu Using Functions
Create a menu-driven program with the following functions:

- `add_price(prices_list, price)` — Add a price to the list.
- `get_average_price(prices_list)` — Calculate the average price.
- `get_max_price(prices_list)` — Find the maximum price.

The menu allows users to add prices, display the average price, show the highest price, and exit the program.