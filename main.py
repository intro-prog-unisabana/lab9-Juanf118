def main():
    from utils import person_data, balance_summary
    from bank_account import BankAccount

    people = []

    while True:
        print("Choose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        choice = input().strip()

        if choice == "1":
            person = person_data()
            people.append(person)

        elif choice == "2":
            name = input("Enter the person's name:")
            found = None
            for p in people:
                if p.name == name:
                    found = p
                    break
            if found is None:
                print("Person not found.")
            else:
                account_number = int(input("Enter a 4-digit account number:"))
                initial_balance = float(input("Enter the initial balance:"))
                found.add_account(BankAccount(account_number, initial_balance))

        elif choice == "3":
            if not people:
                print("No data to show.")
            else:
                balance_summary(people)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

