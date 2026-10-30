
account_number = "123456789"
pin = "1234"
balance = 10000.00

print("=" * 35)
print("       WELCOME TO PYTHON ATM")
print("=" * 35)

# Login
entered_account = input("Enter account number: ")
entered_pin = input("Enter your PIN: ")

if entered_account == account_number and entered_pin == pin:

    print("\nLogin successful!")

    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        print("==============================")

        choice = input("Choose an option (1-5): ")

        # Check balance
        if choice == "1":
            print(f"\nYour current balance is Rs. {balance:.2f}")

        # Deposit money
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: Rs. "))

                if amount > 0:
                    balance += amount
                    print(f"Deposit successful: Rs. {amount:.2f}")
                    print(f"Updated balance: Rs. {balance:.2f}")
                else:
                    print("Amount must be greater than zero.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        # Withdraw money
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: Rs. "))

                if amount <= 0:
                    print("Amount must be greater than zero.")

                elif amount > balance:
                    print("Insufficient balance.")

                else:
                    balance -= amount
                    print(f"Withdrawal successful: Rs. {amount:.2f}")
                    print(f"Remaining balance: Rs. {balance:.2f}")

            except ValueError:
                print("Invalid input. Please enter a number.")

        # Change PIN
        elif choice == "4":
            old_pin = input("Enter your current PIN: ")

            if old_pin == pin:
                new_pin = input("Enter your new 4-digit PIN: ")

                if new_pin.isdigit() and len(new_pin) == 4:
                    pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("PIN must contain exactly 4 digits.")
            else:
                print("Incorrect current PIN.")

        # Exit
        elif choice == "5":
            print("\nThank you for using Python ATM!")
            break

        else:
            print("Invalid option. Please choose 1-5.")

else:
    print("\nInvalid account number or PIN.")
    print("Login failed.")
