# bank_account.py
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = float(balance)
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            return -1
        else:
            self.balance -= amount
            return 0
    def __str__(self):
        account_number = str(self.account_number)
        last_two_digits = account_number[-2:]
        return f"Account number: **{last_two_digits}\nCurrent Balance: {self.balance}"
if __name__ == "__main__":
    my_account = BankAccount("123456789", 1000)
    print(my_account)