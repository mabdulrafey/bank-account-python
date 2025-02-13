class BankAccount:
    # Class attribute
    bank_title = "Muhammad's Python Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member

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
        print(f"Account Number: {self._account_number}")