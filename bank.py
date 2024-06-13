menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[0] Exit

=> """

balance = 0
limit = 500
statement = ""
withdrawal_count = 0
WITHDRAWAL_LIMIT = 3

while True:

    option = input(menu)

    if option == "1":
        amount = float(input("Enter the deposit amount: "))

        if amount > 0:
            balance += amount
            statement += f"Deposit: ${amount:.2f}\n"
            print(f"Your current balance is: ${balance}")

        else:
            print("Operation failed! The amount entered is invalid.")

    elif option == "2":
        amount = float(input("Enter the withdrawal amount: "))

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

        else:
            print("Operation failed! The amount entered is invalid.")

    elif option == "3":
        print("\n================ STATEMENT ================")
        print("No transactions were made." if not statement else statement)
        print(f"\nBalance: ${balance:.2f}")
        print("==========================================")

    elif option == "0":
        break

    else:
        print("Invalid operation, please select the desired operation again.")
