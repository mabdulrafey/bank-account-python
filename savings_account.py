from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.current_balance * (self.interest_rate / 100)
        self.current_balance += interest
        print(f"Interest of ${interest:.2f} applied at {self.interest_rate}% rate.")