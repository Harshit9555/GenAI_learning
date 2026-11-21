# 7.Mini Use Case: Sales Analysis
import numpy as np
sales = np.array([1200,1500,900,2000,1800,1700,1600])
total_sales = np.sum(sales)
avg_sales = np.average(sales)
highest = np.max(sales)
lowest = np.min(sales)
std_dev =np.std(sales)

print(f"Total sales {total_sales}")
print(f"Average sales {avg_sales}")
print(f"Highest sales {highest}")
print(f"Lowest sales {lowest}")
print(f"Standard Deviation of sales {std_dev}")

cnt = 0
for i in sales:
    if i>avg_sales:
        cnt +=1
print(f"{cnt} days where sales are above average")