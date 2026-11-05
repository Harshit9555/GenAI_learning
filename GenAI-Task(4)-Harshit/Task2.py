#Read files in different ways..
# 1 . Read the entire file using read()

with open('sales_data.txt','r') as data:
    content = data.read()
    print(content)

#2. Read the first linee using readline()  

with open('sales_data.txt','r') as data:
    content = data.readline().strip()
    print(content)

#3. read all lines using readlines() and convert to integers

with open('sales_data.txt','r') as data:
    lines = data.readlines()
    sales = [int(line.strip()) for line in lines ]
    print(sales)