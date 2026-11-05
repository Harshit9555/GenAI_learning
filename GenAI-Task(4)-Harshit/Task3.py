#append new sales to the files
new_sales = [5000,2500,1700]
with open('sales_data.txt','a') as data:
    for sale in new_sales:
        data.write(f"{sale}\n")

#reopen and print the entire updated files
with open('sales_data.txt','r') as new_data:
    content = new_data.read()
    print(content)

# total length after appending data
with open('sales_data.txt','r') as data:
    lines = data.readlines()
    print(len(lines))
        
    