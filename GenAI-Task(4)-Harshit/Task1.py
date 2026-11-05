#Write  Sales Records to a  File
sales = [1200,450,980,1500,3000]
f = open('sales_data.txt','w')
f.writelines(str(sale) + '\n' for sale in sales)
f.close()

f = open('sales_data.txt','r')
content = f.read()
print(content)
f.close()