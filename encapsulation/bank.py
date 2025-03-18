class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Public Attribute
        self.__balance = balance  # Private Attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful! New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal successful! Remaining balance: ${self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")
    
    def get_balance(self):
        return self.__balance  # Accessing private attribute via method
    
    def transfer(self, recipient_account, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            recipient_account.__balance += amount
            print(f"Transfer successful! Your new balance: ${self.__balance}")
        else:
            print("Transfer failed: Insufficient balance or invalid amount.")

# Example Usage
account1 = BankAccount("John Doe", 1000)
account2 = BankAccount("Alice Smith", 500)

account1.deposit(500)
account1.withdraw(200)
print("Balance Check:", account1.get_balance())
account1.transfer(account2, 300)
print("Recipient's New Balance:", account2.get_balance())
