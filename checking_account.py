from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
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
