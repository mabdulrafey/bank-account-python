from savings_account import SavingsAccount
from checking_account import CheckingAccount

# Scenario: User opens a checking account and withdraws money
print("--- Scenario: User opens a checking account and withdraws $500 ---")
checking = CheckingAccount("Rafey", 1500, 200, 500, "987654321", "123456789")
checking.print_customer_information()
checking.withdraw(500)
checking.print_customer_information()

print("\n--- Savings Account Demonstration ---")
savings = SavingsAccount("Abdul", 2000, 100, 5, "123456789", "987654321")
savings.print_customer_information()
savings.apply_interest()
savings.print_customer_information()
