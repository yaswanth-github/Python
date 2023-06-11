class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    def __str__(self):
        return f"{self.name} - Email: {self.email}, Phone: {self.phone}"


class ContactList:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Added contact {contact.name} to the contact list.")
    
    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query in contact.name or query in contact.email or query in contact.phone:
                results.append(contact)
        
        if not results:
            print("No results found.")
        else:
            print(f"Search results ({len(results)}):")
            for contact in results:
                print(contact)
    
    def view_list(self):
        if not self.contacts:
            print("The contact list is empty!")
        else:
            print("Contact list:")
            for contact in self.contacts:
                print(contact)
    
    def clear_list(self):
        self.contacts = []
        print("The contact list has been cleared.")


def create_contact(contact_list):
    name = input("Enter the contact's name: ")
    email = input("Enter the contact's email: ")
    phone = input("Enter the contact's phone number: ")
    
    contact = Contact(name, email, phone)
    contact_list.add_contact(contact)

def search_contacts(contact_list):
    query = input("Enter a name, email, or phone number to search: ")
    contact_list.search_contacts(query)

def display_list(contact_list):
    contact_list.view_list()

def clear_all(contact_list):
    confirm = input("Are you sure you want to clear the entire contact list? (y/n) ")
    if confirm == "y":
        contact_list.clear_list()

def main():
    contact_list = ContactList()
    
    while True:
        print("Menu:")
        print("1. Create a contact")
        print("2. Search for a contact")
        print("3. View the contact list")
        print("4. Clear the entire contact list")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_contact(contact_list)
        elif choice == "2":
            search_contacts(contact_list)
        elif choice == "3":
            display_list(contact_list)
        elif choice == "4":
            clear_all(contact_list)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please enter a valid choice.")
    
    print("Goodbye!")

if __name__ == "__main__":
    main()
