class Customer:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer(self, account_number):
        for customer in self.customers:
            if customer.account_number == account_number:
                return customer
        return None

    def deposit(self, account_number, amount):
        customer = self.find_customer(account_number)
        if customer:
            customer.balance += amount
            return True
        return False

    def withdraw(self, account_number, amount):
        customer = self.find_customer(account_number)
        if customer and customer.balance >= amount:
            customer.balance -= amount
            return True
        return False

    def print_report(self):
        print("{:<20} {:<20} {:<10}".format('Name', 'Account Number', 'Balance'))
        for customer in self.customers:
            print("{:<20} {:<20} {:<10}".format(customer.name, customer.account_number, customer.balance))


if __name__ == '__main__':
    bank = Bank()

    # Add some initial customers
    bank.add_customer(Customer('Alice', '123', 1000))
    bank.add_customer(Customer('Bob', '456', 500))
    bank.add_customer(Customer('Charlie', '789', 200))

    # Deposit and withdraw from some accounts
    bank.deposit('123', 500)
    bank.withdraw('456', 200)

    # Print the report
    bank.print_report()
