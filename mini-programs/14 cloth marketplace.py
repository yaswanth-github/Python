import random

class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []

class Marketplace:
    def __init__(self):
        self.items = []
        self.users = []
        self.current_user = None

    def register_user(self, username, password):
        for user in self.users:
            if user.username == username:
                print("Error: Username already taken.")
                return
        self.users.append(User(username, password))
        print("User registered successfully.")

    def login_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print("Login successful.")
                return
        print("Error: Invalid username or password.")

    def add_item(self, item):
        self.items.append(item)

    def browse_items(self):
        for item in self.items:
            print(f"{item.name} - {item.description} - ${item.price}")

    def search_items(self, query):
        for item in self.items:
            if query in item.name or query in item.description:
                print(f"{item.name} - {item.description} - ${item.price}")

    def add_to_cart(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.current_user.cart.append(item)
                print(f"{item_name} added to cart.")
                return
        print(f"Error: Item {item_name} not found.")

    def view_cart(self):
        total = 0
        for item in self.current_user.cart:
            print(f"{item.name} - {item.description} - ${item.price}")
            total += item.price
        print(f"Total: ${total}")

    def checkout(self):
        if not self.current_user:
            print("Error: You need to be logged in to checkout.")
            return
        if len(self.current_user.cart) == 0:
            print("Error: Your cart is empty.")
            return
        print("Checkout successful.")
        self.current_user.cart = []

# Sample usage
marketplace = Marketplace()

marketplace.register_user("alice", "password")
marketplace.add_item(Item("Vintage T-Shirt", "Black vintage t-shirt with graphic print", 20))
marketplace.add_item(Item("Leather Jacket", "Brown leather jacket with zippered front", 100))
marketplace.add_item(Item("Denim Jeans", "Slim-fit denim jeans with distressed details", 50))

marketplace.login_user("alice", "password")

marketplace.browse_items()
marketplace.search_items("vintage")

marketplace.add_to_cart("Vintage T-Shirt")
marketplace.add_to_cart("Leather Jacket")
marketplace.view_cart()

marketplace.checkout()
marketplace.view_cart()
