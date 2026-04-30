# utils.py
def person_data_input():
    from person import Person
    from bank_account import BankAccount
    name = input("Enter the person's name:\n")
    new_name = Person(name)
    done = False
    while not done:

        account_number = int(input("Enter a 4-digit account number:\n"))
        inicial_balance = float(input("Enter the initial balance:\n"))
        new_account = BankAccount(account_number, inicial_balance)
        new_name.add_account(new_account)
        done = input("Are you done adding accounts? (yes/no):")
        if done.strip().lower() == "yes":
            break

    return new_name
def balance_summary(person):
    for new_name in person:
        total_balance = sum(account.balance for account in new_name.accounts)
    print(f"{new_name.name} : {total_balance:.2f}")
