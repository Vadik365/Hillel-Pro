import csv


class Product:

    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)

    def change_price(self, price):
        self.price = float(price)

    def change_stock(self, stock):
        self.stock = int(stock)


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
        self.total_sum = 0.0

    def add_product(self, product, quantity):
        self.item_list.append((product, quantity))

    def calculate_total(self):
        self.total_sum = sum(product.price * quantity for product, quantity in self.item_list)
        return self.total_sum



products_list = []
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
                int(row['stock'])
            )
            products_list.append(product)
        elif row['type'] == 'Customer':
            customer = Customer(row['name'], row['email'])
            customer_list.append(customer)
        elif row['type'] == 'Order':
            order = Order()
            product = products_list[int(row['product_index'])]
            quantity = int(row['quantity'])
            order.add_product(product, quantity)
            order.calculate_total()
            order_list.append(order)
            customer_list[0].add_order(order)


for customer in customer_list:
    print(f"\nCustomer:{customer.name}")

    for order in customer.orders:
        product_names = [
            f"{product.name} x{quantity}"
            for product, quantity in order.item_list
        ]
        print(f"Items: {', '.join(product_names)}")
        print(f"Total price: {order.total_sum}")