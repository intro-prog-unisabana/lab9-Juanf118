# bank_account.py
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Failed")
        else:
            self.balance -= amount
    def __str__(self):
        self.account_number = str(self.account_number)

        return f"Account number {self.account_number} Current Balance ${self.balance:.2f}"