class BankAccount:
    def __init__(self,AccNo,Bal=0):
        self.AccNo=AccNo
        self.__Bal=Bal
    def deposit(self,amt):
        if amt<0:
             print('Invalid balance')
             return
        self.__Bal+=amt
        print(f"{amt} is deposited on account Number {self.AccNo}")

    def withdraw(self,amt):
        if self.__Bal<amt:
           print(f"{amt} can't withdraw Insufficient balance")
           return
        self.__Bal-=amt

    def display(self):
        print(f'{self.AccNo} has balance {self.__Bal}')

# Creating an object of BankAccount class
my_account = BankAccount("9876543210", 1000)  # account number, starting balance

# Using the methods
my_account.deposit(500)     # Deposit Rs. 500
my_account.withdraw(200)    # Withdraw Rs. 200
my_account.display()        # Show balance
