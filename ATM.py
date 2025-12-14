class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    # Change PIN
    def set_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            return "PIN changed successfully."
        else:
            return "Invalid old PIN."

    # Deposit money
    def deposit(self, amount, pin):
        if self.__pin == pin:
            self.__balance += amount
            return f"Deposited ₹{amount}. New balance = ₹{self.__balance}"
        else:
            return "Invalid PIN. Deposit failed."

    # Withdraw money
    def withdraw(self, amount, pin):
        if self.__pin == pin:
            if self.__balance >= amount:
                self.__balance -= amount
                return f"Withdrawal successful. Remaining balance = ₹{self.__balance}"
            else:
                return "Insufficient balance."
        else:
            return "Invalid PIN. Withdrawal failed."

    # Check balance
    def check_balance(self, pin):
        if self.__pin == pin:
            return f"Your current balance is ₹{self.__balance}"
        else:
            return "Invalid PIN."


# ---------------- MAIN PROGRAM ----------------

old_pin = int(input("Enter your PIN: "))
balance = int(input("Enter initial balance: "))

atm = ATM(old_pin, balance)

while True:
    print("\n===== ATM MENU =====")
    print("1. Change PIN")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        old_pin = int(input("Enter old PIN: "))
        new_pin = int(input("Enter new PIN: "))
        print(atm.set_pin(old_pin, new_pin))

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        pin = int(input("Enter your PIN: "))
        print(atm.deposit(amount, pin))

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        pin = int(input("Enter your PIN: "))
        print(atm.withdraw(amount, pin))

    elif choice == 4:
        pin = int(input("Enter your PIN: "))
        print(atm.check_balance(pin))

    elif choice == 5:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 and 5.")
