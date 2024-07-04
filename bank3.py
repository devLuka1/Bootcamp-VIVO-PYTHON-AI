import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

class Transaction(ABC):
    @abstractmethod
    def register(self, account):
        pass

class Deposit(Transaction):
    def __init__(self, amount):
        self.amount = amount

    def register(self, account):
        if self.amount > 0:
            account._balance += self.amount
            account.history.add_transaction(self)
            return True
        return False

    def __str__(self):
        return f"Deposit: ${self.amount:.2f}"

class Withdraw(Transaction):
    def __init__(self, amount):
        self.amount = amount

    def register(self, account):
        if 0 < self.amount <= account._balance:
            account._balance -= self.amount
            account.history.add_transaction(self)
            return True
        return False

    def __str__(self):
        return f"Withdrawal: ${self.amount:.2f}"

class History:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append({
            "transaction": str(transaction),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def show(self):
        return "\n".join([f"{t['date']} - {t['transaction']}" for t in self.transactions])

class Account:
    def __init__(self, agency, number):
        self._balance = 0.0
        self._number = number
        self._agency = agency
        self.history = History()

    def balance(self):
        return self._balance

    @staticmethod
    def new_account(client, number):
        return Account(client.agency, number)

    def deposit(self, amount):
        return Deposit(amount).register(self)

    def withdraw(self, amount):
        return Withdraw(amount).register(self)

    def __str__(self):
        return f"Agency: {self._agency}, Account: {self._number}, Balance: ${self._balance:.2f}"

class CurrentAccount(Account):
    def __init__(self, agency, number, limit, withdrawal_limit):
        super().__init__(agency, number)
        self._limit = limit
        self._withdrawal_limit = withdrawal_limit
        self._withdrawals = 0

    def withdraw(self, amount):
        if self._withdrawals >= self._withdrawal_limit:
            print("Operation failed! Maximum number of withdrawals exceeded.")
            return False
        if amount > self._limit:
            print("Operation failed! The withdrawal amount exceeds the limit.")
            return False
        if super().withdraw(amount):
            self._withdrawals += 1
            return True
        return False

class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def perform_transaction(self, account, transaction):
        return transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)

class Person(Client):
    def __init__(self, id_number, name, birth_date, address):
        super().__init__(address)
        self.id_number = id_number
        self.name = name
        self.birth_date = birth_date

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

def create_user(users):
    id_number = input("\nEnter your ID (just numbers): ")
    if any(user for user in users if user.id_number == id_number):
        print("\nThere's already a user with this ID!")
        return

    name = input("\nEnter your name: ")
    birth_date = input("\nEnter your birth date (yyyy-mm-dd): ")
    address = input("\nEnter your address (Street Address, Apartment Number, City, State, ZIP Code): ")

    users.append(Person(id_number, name, birth_date, address))
    print("\nThe User has been created successfully")

def create_account(users, accounts):
    id_number = input("\nEnter the user ID: ")
    user = next((user for user in users if user.id_number == id_number), None)

    if user:
        account_number = len(accounts) + 1
        account = CurrentAccount("0001", account_number, 500, 3)
        user.add_account(account)
        accounts.append(account)
        print("\nThe Account has been created successfully!")
    else:
        print("\nThe user has not been found, account creation process terminated.")

def show_accounts(accounts):
    for account in accounts:
        print("=" * 100)
        print(account)

def main():
    users = []
    accounts = []

    while True:
        option = menu()

        if option == "1":
            id_number = input("\nEnter the user ID: ")
            user = next((user for user in users if user.id_number == id_number), None)
            if not user:
                print("User not found!")
                continue

            amount = float(input("Enter the deposit amount: $"))
            account_number = int(input("Enter the account number: "))
            account = next((acc for acc in user.accounts if acc._number == account_number), None)

            if account and account.deposit(amount):
                print(f"\nYour current balance is: ${account.balance()}")
            else:
                print("Deposit failed!")

        elif option == "2":
            id_number = input("\nEnter the user ID: ")
            user = next((user for user in users if user.id_number == id_number), None)
            if not user:
                print("User not found!")
                continue

            amount = float(input("Enter the withdrawal amount: $"))
            account_number = int(input("Enter the account number: "))
            account = next((acc for acc in user.accounts if acc._number == account_number), None)

            if account and account.withdraw(amount):
                print(f"\nYou've withdrawn ${amount}")
                print(f"Now your current balance is: ${account.balance()}")
            else:
                print("Withdrawal failed!")

        elif option == "3":
            id_number = input("\nEnter the user ID: ")
            user = next((user for user in users if user.id_number == id_number), None)
            if not user:
                print("User not found!")
                continue

            account_number = int(input("Enter the account number: "))
            account = next((acc for acc in user.accounts if acc._number == account_number), None)

            if account:
                print("\n================ STATEMENT ================")
                print(account.history.show())
                print(f"\nBalance: ${account.balance():.2f}")
                print("===========================================")
            else:
                print("Account not found!")

        elif option == "4":
            create_user(users)

        elif option == "5":
            create_account(users, accounts)

        elif option == "6":
            show_accounts(accounts)

        elif option == "0":
            break

        else:
            print("Invalid operation, please select the desired operation again.")

main()
