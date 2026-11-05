#Generate Summary Report from File
with open('sales_data.txt','r') as data:
    sales = [int(line.strip()) for line in data.readlines()]
    total_sales = sum(sales)
    highest_sales = max(sales)
    lowest_sales = min(sales)
    average_sales = total_sales/len(sales)
    print("total Sales", total_sales)
    print("Highest Sales",highest_sales)
    print("Lowest Sales",lowest_sales)
    print("Average Sales",round(average_sales),2)
