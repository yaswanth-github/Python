# Initialize the total donation amount to zero
total_donation = 0

# Define a function to add donations
def add_donation():
    global total_donation
    donation = float(input("Enter the donation amount: "))
    total_donation += donation
    print("Thank you for your donation of ${:.2f}!\n".format(donation))

# Define a function to generate a report
def generate_report():
    print("Total donations received: ${:.2f}".format(total_donation))

# Main program loop
while True:
    print("Choose an option:")
    print("1. Add donation")
    print("2. Generate report")
    print("3. Quit")
    choice = input("> ")
    if choice == "1":
        add_donation()
    elif choice == "2":
        generate_report()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.\n")
