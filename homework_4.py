import csv


class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)
    
    def change_price(self, price):
        self.price = float(price)
        
    def change_quantity(self, quantity):
        self.quantity = int(quantity)
        
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []
        
    def add_order(self, order):
        self.orders.append(order)
        
class Order:
    def __init__(self):
        self.item_list = []
        self.total_price = 0.0

    def add_item(self, product):
        self.item_list.append(product)
        
    def calculate_total_price(self):
        self.total_price = sum(item.price for item in self.item_list)
        return self.total_price
    

product_list = []
customer_list = []
order_list = []
with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['type'] == 'Product':
            product = Product(
                row['name'],
                row['category'], 
                float(row['price']), 
                int(row['quantity'])
            )
            product_list.append(product)
        elif row['type'] == 'Customer':
            customer = Customer(
                row['name'], 
                row['email']
            )
            customer_list.append(customer)
        elif row['type'] == 'Order':
            order = Order()
            order.add_item(product_list[int(row['prod_index']) -1])
            order.calculate_total_price()
            order_list.append(order)
            customer_list[int(row['customer_index'])].add_order(order)

for customer in customer_list:
    print(f"\nCustomer:{customer.name}")
    
    for order in customer.orders:
        product_names = [i.name for i in order.item_list]
        print(f"Item:{', '.join(product_names)}")
        print(f"Price:{order.total_price}")