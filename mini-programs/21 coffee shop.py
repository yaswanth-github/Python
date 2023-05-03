import csv

# Define function to write sales to CSV file
def write_sales_to_csv(sales):
    with open('mini-programs/sales.csv', mode='a') as sales_file:
        writer = csv.writer(sales_file)
        writer.writerow(sales)

# Define function to read inventory from CSV file
def read_inventory_from_csv():
    with open('mini-programs/inventory.csv', mode='r') as inventory_file:
        reader = csv.reader(inventory_file)
        inventory = {rows[0]: int(rows[1]) for rows in reader}
        return inventory

# Define function to update inventory in CSV file
def update_inventory_in_csv(inventory):
    with open('mini-programs/inventory.csv', mode='w') as inventory_file:
        writer = csv.writer(inventory_file)
        for key, value in inventory.items():
            writer.writerow([key, value])

# Define function to generate sales report
def generate_sales_report():
    total_sales = 0
    with open('sales.csv', mode='r') as sales_file:
        reader = csv.reader(sales_file)
        for row in reader:
            total_sales += float(row[1])
    return f"Total sales: ${total_sales:.2f}"

# Define main function
def main():
    print("Welcome to the Coffee Shop Sales and Inventory Tracker!")
    inventory = read_inventory_from_csv()
    while True:
        print("\nWhat would you like to do?")
        print("1. Enter a new sale")
        print("2. Update inventory")
        print("3. Generate sales report")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            print("\nEnter sale information:")
            item = input("Item name: ")
            if item not in inventory:
                print("Item not found in inventory.")
                continue
            quantity = int(input("Quantity sold: "))
            if quantity > inventory[item]:
                print("Insufficient inventory.")
                continue
            price = float(input("Price per item: "))
            sales_total = quantity * price
            write_sales_to_csv([item, sales_total])
            inventory[item] -= quantity
            update_inventory_in_csv(inventory)
            print(f"Sale added: {quantity} {item}s for ${sales_total:.2f}")
        elif choice == '2':
            print("\nEnter inventory information:")
            item = input("Item name: ")
            if item not in inventory:
                print("Item not found in inventory.")
                continue
            quantity = int(input("Quantity added: "))
            inventory[item] += quantity
            update_inventory_in_csv(inventory)
            print(f"Inventory updated: {quantity} {item}s")
        elif choice == '3':
            print("\nSales Report:")
            print(generate_sales_report())
        elif choice == '4':
            print("\nThank you for using the Coffee Shop Sales and Inventory Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == '__main__':
    main()