class BankAccount:
    # Class attribute
    bank_title = "Muhammad's Python Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.current_balance - amount >= self.minimum_balance:
                self.current_balance -= amount
                print(f"${amount} withdrawn successfully.")
            else:
                print("Withdrawal denied! Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance: ${self.minimum_balance}")


# 2 instances
account1 = BankAccount("Abdul", 500, 100)
account2 = BankAccount("Rafey", 1000, 200)

# Display information
account1.print_customer_information()
print("\n")
account1.deposit(200)
account1.withdraw(500)
print("\n")
account1.print_customer_information()


print("\n-----------------------------\n")
print("\n-----------------------------\n")

account2.print_customer_information()
print("\n")
account2.deposit(300)
account2.withdraw(900)
print("\n")
account2.print_customer_information()
