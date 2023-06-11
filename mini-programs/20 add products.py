# define a dictionary of products with their prices
products = {"apple": 0.5, "banana": 0.25, "orange": 0.75, "pear": 0.6}

# initialize the shopping cart as an empty list
cart = []

# define a function to display the menu and prompt for user input
def display_menu():
    print("Welcome to our online store! Here's our menu:")
    for product, price in products.items():
        print(f"{product.capitalize()}: ${price:.2f}")
    print("Enter the name of the product you want to add to your cart (or 'done' to finish):")

# define a function to calculate the total cost of the order
def calculate_total():
    total = sum([products[item] for item in cart])
    return total

# define a function to generate the invoice
def generate_invoice():
    print("Here's your invoice:")
    for item in cart:
        print(f"{item.capitalize()}: ${products[item]:.2f}")
    total = calculate_total()
    print(f"Total: ${total:.2f}")

# main program loop
while True:
    display_menu()
    user_input = input()
    if user_input == "done":
        break
    elif user_input not in products:
        print("Sorry, that's not a valid product name.")
    else:
        cart.append(user_input)
        print(f"Added {user_input.capitalize()} to your cart.")
        print(f"Your current cart: {', '.join([item.capitalize() for item in cart])}")
# once the user is done shopping, generate the invoice
generate_invoice()
