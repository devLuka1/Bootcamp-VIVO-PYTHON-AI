
import textwrap

def menu():
    menu = """\n
    __________________ MENU __________________
    [1] Deposit
    [2] Withdraw
    [3] Statement
    [4] Create User
    [5] Create Account
    [6] Show Accounts
    [0] Exit
    => """
    return input(textwrap.dedent(menu))

def Deposit(balance, amount, statement, /):

        if amount > 0:
            balance += amount
            statement += f"Deposit: ${amount:.2f}\n"
            print(f"\nYour current balance is: ${balance}")

        else:
            print("\nOperation failed! The amount entered is invalid.")

        return balance, statement

def withdrawal(*, balance, amount, statement, withdrawal_count, WITHDRAWAL_LIMIT):

    option = input(menu)    

    if option == "2":
            amount = float(input("Enter the withdrawal amount: $"))

            exceeded_balance = amount > balance

            exceeded_limit = amount > limit

            exceeded_withdrawals = withdrawal_count >= WITHDRAWAL_LIMIT

            if exceeded_balance:
                print("Operation failed! You don't have enough balance.")

            elif exceeded_limit:
                print("Operation failed! The withdrawal amount exceeds the limit.")

            elif exceeded_withdrawals:
                print("Operation failed! Maximum number of withdrawals exceeded.")

            elif amount > 0:
                balance -= amount
                statement += f"Withdrawal: ${amount:.2f}\n"
                withdrawal_count += 1
                print(f"You've withdrawn ${amount}")
                print(f"Now you're current balance is: ${balance}")

            else:
                print("Operation failed! The amount entered is invalid.")

            return balance, statement

def show_statement(balance, /, *, statement):
    print("\n================ STATEMENT ================")
    print("No transactions were made." if not statement else statement)
    print(f"\nBalance: ${balance:.2f}")
    print("===========================================")

def create_user(users):
    ID = input("\nEnter your ID (just numbers): ")
    user = filter_user(ID, users)

    if user:
        print("\nThere's already a user with this ID!")
        return
    
    name = input("\nEnter your name: ")
    birth_date = input("\nEnter your birth date (mm-dd-yyyy): ")
    address = input("\nEnter your address (Street Address, Apartment Number, City, State, ZIP Code): ")

    users.append({"name": name, "birth_date": birth_date, "ID": ID, "address": address})

    print("\nThe User has been created successfully")

def filter_user(ID, users):
    filtered_users = [user for user in users if user["ID"] == ID]
    return filtered_users[0] if filtered_users else None

def create_account(AGENCY, account_number, users):
    ID = input("\nEnter the user ID: ")
    user = filter_user(ID, users)

    if user:
        print("\nThe Account has been created successfully!")
        return {"agency": AGENCY, "account_number": account_number, "user": user}
    
    print("\nThe user has not been found, account creation process terminated.")

def show_accounts(accounts):
    for account in accounts:
        line = f"""\
            Agency: {account['agency']}
            Account: {account['account_number']}
            Owner: {account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))

def main():
    WITHDRAWAL_LIMIT = 3
    AGENCY = "0001"


    balance = 0
    limit = 500
    statement = ""
    withdrawal_count = 0
    users = []
    accounts = []


    while True:

        option = menu()

        if option == "1":
            amount = float(input("Enter the deposit amount: $"))

            if amount > 0:
                balance += amount
                statement += f"Deposit: ${amount:.2f}\n"
                print(f"Your current balance is: ${balance}")

            else:
                print("Operation failed! The amount entered is invalid.")

        elif option == "2":
            amount = float(input("Enter the withdrawal amount: $"))

            exceeded_balance = amount > balance

            exceeded_limit = amount > limit

            exceeded_withdrawals = withdrawal_count >= WITHDRAWAL_LIMIT

            if exceeded_balance:
                print("Operation failed! You don't have enough balance.")

            elif exceeded_limit:
                print("Operation failed! The withdrawal amount exceeds the limit.")

            elif exceeded_withdrawals:
                print("Operation failed! Maximum number of withdrawals exceeded.")

            elif amount > 0:
                balance -= amount
                statement += f"Withdrawal: ${amount:.2f}\n"
                withdrawal_count += 1
                print(f"You've withdrawn ${amount}")
                print(f"Now you're current balance is: ${balance}")

            else:
                print("Operation failed! The amount entered is invalid.")

        elif option == "3":
            print("\n================ STATEMENT ================")
            print("No transactions were made." if not statement else statement)
            print(f"\nBalance: ${balance:.2f}")
            print("===========================================")

        elif option == "4":
            create_user(users)

        elif option == "5":
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)

            if account:
                accounts.append(account)

        elif option == "6":
            show_accounts(accounts)

        elif option == "0":
            break

        else:
            print("Invalid operation, please select the desired operation again.")



main()
