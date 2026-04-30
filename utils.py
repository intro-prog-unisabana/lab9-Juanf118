# utils.py
def person_data():
    from person import Person
    from bank_account import BankAccount

    name = input("Enter the person's name:")
    person = Person(name)

    while True:
        account_number = int(input("Enter a 4-digit account number:"))
        initial_balance = float(input("Enter the initial balance:"))
        person.add_account(BankAccount(account_number, initial_balance))

        done = input("Are you done adding accounts? (yes/no):")
        if done.strip().lower() == "yes":
            break

    return person


def balance_summary(person_list):
    for person in person_list:
        total = sum(account.balance for account in person.accounts)
        print(f"{person.name} : {total:.2f}")