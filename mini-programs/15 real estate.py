import json

# Define a function to load property data from a JSON file
def load_properties():
    with open('properties.json', 'r') as f:
        return json.load(f)

# Define a function to save property data to a JSON file
def save_properties(properties):
    with open('properties.json', 'w') as f:
        json.dump(properties, f)

# Define a function to search for properties based on certain criteria
def search_properties(properties):
    print("Search for Properties\n")
    print("Available locations: ", set(property["location"] for property in properties))
    print("Available prices: ", set(property["price"] for property in properties))
    print("Available number of bedrooms: ", set(property["bedrooms"] for property in properties))
    
    location = input("Enter location: ")
    price = float(input("Enter maximum price: "))
    bedrooms = int(input("Enter minimum number of bedrooms: "))

    matching_properties = []
    for property in properties:
        if property["location"] == location and property["price"] <= price and property["bedrooms"] >= bedrooms:
            matching_properties.append(property)

    if matching_properties:
        print("\nMatching properties:")
        for property in matching_properties:
            print(f"{property['address']}, {property['location']} - {property['bedrooms']} bedrooms, ${property['price']}")
    else:
        print("\nNo matching properties found.")

# Define a function to add a new property
def add_property(properties):
    print("Add a New Property\n")
    address = input("Enter address: ")
    location = input("Enter location: ")
    price = float(input("Enter price: "))
    bedrooms = int(input("Enter number of bedrooms: "))
    new_property = {"address": address, "location": location, "price": price, "bedrooms": bedrooms}
    properties.append(new_property)
    save_properties(properties)
    print("\nProperty added successfully.")

# Define a function to update an existing property
def update_property(properties):
    print("Update a Property\n")
    address = input("Enter address: ")
    for property in properties:
        if property["address"] == address:
            location = input(f"Enter new location ({property['location']}): ") or property['location']
            price = input(f"Enter new price ({property['price']}): ") or property['price']
            bedrooms = input(f"Enter new number of bedrooms ({property['bedrooms']}): ") or property['bedrooms']
            property["location"] = location
            property["price"] = float(price)
            property["bedrooms"] = int(bedrooms)
            save_properties(properties)
            print("\nProperty updated successfully.")
            return
    print("\nProperty not found.")

# Load property data from file
properties = load_properties()

# Define main program loop
while True:
    print("\nReal Estate Management System")
    print("1. Search for Properties")
    print("2. Add a New Property")
    print("3. Update an Existing Property")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        search_properties(properties)
    elif choice == "2":
        add_property(properties)
    elif choice == "3":
        update_property(properties)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
