from savings_account import SavingsAccount
from checking_account import CheckingAccount

# Scenario: User opens a checking account and withdraws money
print("--- Scenario: User opens a checking account and withdraws $500 ---")
checking1 = CheckingAccount("Rafey", 1500, 200, 500, "987654321", "123456789")
checking1.print_customer_information()
checking1.withdraw(500)
checking1.print_customer_information()

checking2 = CheckingAccount("Ali", 1200, 150, 300, "234567891", "345678912")
checking2.print_customer_information()
checking2.withdraw(300)
checking2.print_customer_information()

print("\n--- Savings Account Demonstration ---")
savings1 = SavingsAccount("Abdul", 2000, 100, 5, "123456789", "987654321")
savings1.print_customer_information()
savings1.apply_interest()
savings1.print_customer_information()

savings2 = SavingsAccount("Hassan", 2500, 150, 3, "567891234", "678912345")
savings2.print_customer_information()
savings2.apply_interest()
savings2.print_customer_information()
