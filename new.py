# Initial account details
account_balance = 10000.0      # Current balance in account
correct_pin = "1234"           # ATM PIN
transaction_history = []       # Stores transaction records


# Function to check account balance
def check_balance():
    global account_balance

    print("\n===== ACCOUNT BALANCE =====")
    print(f"Current Balance: ₹{account_balance:.2f}")


# Function to deposit money
def deposit_money():
    global account_balance

    print("\n===== DEPOSIT MONEY =====")

    amount = float(input("Enter amount to deposit: ₹"))

    # Check if amount is positive
    if amount > 0:
        account_balance += amount
        transaction_history.append(f"Deposited ₹{amount}")
        print(f"₹{amount:.2f} deposited successfully.")
        print(f"New Balance: ₹{account_balance:.2f}")
    else:
        print("Invalid amount.")


# Function to withdraw money
def withdraw_money():
    global account_balance

    print("\n===== WITHDRAW MONEY =====")

    amount = float(input("Enter amount to withdraw: ₹"))

    # Check if amount is positive
    if amount <= 0:
        print("Invalid amount.")

    # Check if sufficient balance exists
    elif amount > account_balance:
        print("Insufficient Balance.")

    else:
        account_balance -= amount
        transaction_history.append(f"Withdrawn ₹{amount}")
        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Remaining Balance: ₹{account_balance:.2f}")


# Function to show transaction history
def show_transactions():

    print("\n===== TRANSACTION HISTORY =====")

    # If no transactions exist
    if len(transaction_history) == 0:
        print("No transactions available.")

    else:
        # Loop through all transactions
        for transaction in transaction_history:
            print(transaction)


# Function to display ATM menu
def atm_menu():

    print("\n")
    print("========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    print("==============================")


# LOGIN SECTION

# User gets maximum 3 attempts
attempts = 3

while attempts > 0:

    entered_pin = input("Enter ATM PIN: ")

    # Correct PIN
    if entered_pin == correct_pin:
        print("\nLogin Successful!")
        break

    # Wrong PIN
    else:
        attempts -= 1
        print(f"Wrong PIN. Attempts Left: {attempts}")

# If all attempts are used
if attempts == 0:
    print("\nAccount Blocked. Too many wrong attempts.")

# If login successful, start ATM system
else:

    while True:

        atm_menu()

        choice = input("Enter your choice: ")

        # Check Balance
        if choice == "1":
            check_balance()

        # Deposit
        elif choice == "2":
            deposit_money()

        # Withdraw
        elif choice == "3":
            withdraw_money()

        # Transaction History
        elif choice == "4":
            show_transactions()

        # Exit ATM
        elif choice == "5":
            print("\nThank you for using our ATM.")
            break

        # Invalid Choice
        else:
            print("Invalid choice. Please try again.")