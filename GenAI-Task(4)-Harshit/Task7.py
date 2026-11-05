# Create a dictionary of product prices
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

# Ask the user for a discount percentage
discount = float(input("Enter discount percentage: "))

if 0 <= discount <= 100:
    total_discounted_price = 0

    # Calculate discounted prices
    with open("discount_report.txt", "w") as data:
        data.write("Product | Original Price | Discounted Price\n")
        data.write("-" * 45 + "\n")

        for product, original_price in prices.items():
            discounted_price = original_price * (1 - discount / 100)
            total_discounted_price += discounted_price

            data.write(
                f"{product} | {original_price:.2f} | "
                f"{discounted_price:.2f}\n"
            )

        # Write summary
        average_price = total_discounted_price / len(prices)

        data.write("-" * 45 + "\n")
        data.write(f"Total Items: {len(prices)}\n")
        data.write(f"Average Discounted Price: {average_price:.2f}\n")

    # Read and print the report
    with open("discount_report.txt", "r") as data:
        print("\nDiscount Report:")
        print(data.read())

else:
    print("Please enter a discount between 0 and 100.")