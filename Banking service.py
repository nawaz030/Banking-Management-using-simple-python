accounts = []
next_account_number = 1001 # Start account number

def find_account(acct_no):
    for acc in accounts:
        if acc["account_number"] == acct_no:
            return acc
    return None

# Stage 1: Account Management
while True:
    print("\n--- Account Management Menu ---")
    print("1. Create Account")
    print("2. Delete Account")
    print("3. Show Account Details")
    print("4. Go to Bank Operations")

    choice = input("Enter choice (1-4): ")

    if choice == "1":  # Create Account
        name = input("Enter account holder name: ")
        if name != "":
            account = {"account_number": next_account_number, "name": name, "balance": 0.0}
            accounts.append(account)
            print(f"Account created! Account No: {next_account_number}")
            next_account_number += 1
        else:
            print("Name cannot be empty!")

    elif choice == "2":  # Delete Account
        acc_no = int(input("Enter account number to delete: "))
        acc = find_account(acc_no)
        if acc:
            accounts.remove(acc)
            print(f"Account {acc_no} deleted.")
        else:
            print("Account not found.")

    elif choice == "3":  # Show Accounts
        if accounts:
            print("\n--- Accounts ---")
            for acc in accounts:
                print(f"Account No: {acc['account_number']} | Name: {acc['name']}")
        else:
            print("No accounts found.")

    elif choice == "4":  # Go to Operations
        if accounts:
            break
        else:
            print("Create at least one account first!")

    else:
        print("Invalid choice! Please select 1-4.")

# Stage 2: Bank Operations
while True:
    print("\n--- Bank Operations Menu ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Show Total Balance")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":  # Deposit
        acc_no = int(input("Enter account number: "))
        acc = find_account(acc_no)
        if acc:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                acc["balance"] += amount
                print(f"Deposited {amount}. New Balance: {acc['balance']}")
            else:
                print("Amount must be positive.")
        else:
            print("Account not found.")

    elif choice == "2":  # Withdraw
        acc_no = int(input("Enter account number: "))
        acc = find_account(acc_no)
        if acc:
            amount = float(input("Enter withdrawal amount: "))
            if 0 < amount <= acc["balance"]:
                acc["balance"] -= amount
                print(f"Withdrew {amount}. New Balance: {acc['balance']}")
            else:
                print("Invalid or insufficient balance.")
        else:
            print("Account not found.")

    elif choice == "3":  # Total Balance
        total = sum(acc["balance"] for acc in accounts)
        print(f"Total Balance in Bank: {total}")

    elif choice == "4":  # Exit
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice! Please select 1-4.")
