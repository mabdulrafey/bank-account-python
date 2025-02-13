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

# Subclass: Savings Account with Interest
class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.current_balance * (self.interest_rate / 100)
        self.current_balance += interest
        print(f"Interest of ${interest:.2f} applied at {self.interest_rate}% rate.")

# Subclass: Checking Account with Transfer Limitation
class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit
    
    def transfer(self, recipient, amount):
        if amount > self.transfer_limit:
            print("Transfer denied! Amount exceeds transfer limit.")
        elif self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            recipient.current_balance += amount
            print(f"${amount} transferred successfully to {recipient.customer_name}.")
        else:
            print("Transfer denied! Insufficient balance.")

# Testing the new subclasses
savings = SavingsAccount("Abdul", 2000, 100, 5)
savings.print_customer_information()
savings.apply_interest()
savings.print_customer_information()

print("\n-----------------------------\n")

checking = CheckingAccount("Rafey", 1500, 200, 500)
checking.print_customer_information()
checking.transfer(savings, 400)
checking.print_customer_information()
savings.print_customer_information()
