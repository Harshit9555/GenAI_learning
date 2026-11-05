#Mini Problem: Menu Using Functions
def add_price(price_list,price):
    return price_list.append(price)

def get_average_price(price_list):
    n  = len(price_list)
    total =sum(price_list)
    return total/n

def get_max_price(price_list):
    return max(price_list)

price_list = []
while True:
    menu = input("Enter The Menu: \n1.Add price\n2.Show  Average price\n3.Show Highest price\nq.Quit:\n ")
    if menu =='q':
        break
    elif menu == '1':
        price = int(input("Enter the price:"))
        add_price(price_list,price)
    elif menu == '2':
        print(get_average_price(price_list))
    elif menu == '3':
        print(get_max_price(price_list))
        