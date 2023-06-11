# Menu dictionary containing items and prices
menu = {"Burger": 5, "Fries": 2, "Soda": 1}

# Empty cart list
cart = []

# Function to display menu
def show_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

# Function to add item to cart
def add_to_cart(item):
    if item in menu:
        cart.append(item)
        print(f"{item} added to cart.")
    else:
        print("Item not on menu.")

# Function to remove item from cart
def remove_from_cart(item):
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from cart.")
    else:
        print("Item not in cart.")

# Function to display cart and total
def show_cart():
    total = sum([menu[item] for item in cart])
    print("Cart:")
    for item in cart:
        print(f"{item}: ${menu[item]}")
    print(f"Total: ${total}")

# Function to generate receipt
def generate_receipt():
    total = sum([menu[item] for item in cart])
    print("Receipt:")
    for item in cart:
        print(f"{item}: ${menu[item]}")
    print(f"Total: ${total}")
    cart.clear()

# Main program loop
while True:
    print("\n1. Show menu")
    print("2. Add item to cart")
    print("3. Remove item from cart")
    print("4. Show cart")
    print("5. Generate receipt")
    print("6. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        item = input("Enter item: ")
        add_to_cart(item)
    elif choice == "3":
        item = input("Enter item: ")
        remove_from_cart(item)
    elif choice == "4":
        show_cart()
    elif choice == "5":
        generate_receipt()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Try again.")
