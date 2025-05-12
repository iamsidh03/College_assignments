# Custom Exception Class
class InsufficientFundsError(Exception):
    def __init__(self, balance, withdrawal_amount):
        self.balance = balance
        self.withdrawal_amount = withdrawal_amount
        super().__init__(f"Insufficient funds: Balance = {balance}, Tried to withdraw = {withdrawal_amount}")

# BankAccount Class
class BankAccount:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"{amount} deposited successfully. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"{amount} withdrawn successfully. Remaining balance: {self.balance}")

    def display_balance(self):
        print(f"Account {self.acc_no} balance: {self.balance}")

# Testing the code
try:
    acc = BankAccount("1234567890", 1000)
    acc.deposit(500)
    acc.withdraw(2000)  # Trying to withdraw more than balance
except InsufficientFundsError as e:
    print("Transaction Failed:", e)
