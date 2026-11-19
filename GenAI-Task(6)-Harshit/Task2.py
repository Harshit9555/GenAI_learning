#Bill Calculator with Error Handling
prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for i in prices:
    try:
        # Check whether the value is numeric
        if not isinstance(i, (int, float)):
            raise TypeError("Price must be a number")

        # Check for negative prices
        if i < 0:
            raise ValueError("Negative price not allowed")

        # Add only positive prices
        if i > 0:
            total += i

        print("Running Total:", total)

    except TypeError as ex:
        print("TypeError:", ex)

    except ValueError as ex:
        print("ValueError:", ex)

print("Final Bill:", total)