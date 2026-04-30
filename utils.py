# utils.py
from person import Person
from bank_account import BankAccount
def person_data_input():
    name = input("Enter the person's name:\n")
    new_name = Person(name)
    done = False
    while not done:

        account_number = int(input("Enter a 4-digit account number:\n"))
        inicial_balance = float(input("Enter the initial balance:\n"))
        new_account = BankAccount(account_number, inicial_balance)
        new_name.add_account(new_account)
        more_accounts = input("Are you done adding accounts? (yes/no)\n").lower()
        if more_accounts == "yes":
            done = True
if __name__ == "__main__":
    person_data_input()
def balance_summary(person):
    print(f"Name: {person.name}")
    for account in person.accounts:
        print(account)