'''🔸 Problem 3: BankAccount with Deposit & Withdraw
Task:
Create a class BankAccount with:
Attributes: owner, balance (default = 0)
Methods:
deposit(amount)
withdraw(amount)
display_balance()
test edge cases like withdrawing more than the balance.'''
class BackAccount:
    def __init__(self,owner,balance =0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amt):
        if amt <=0:
            print('invalid amount')
        else:
            self.balance+=amt
            
    def withdraw(self,amt):
        if self.balance<=0:
            print('insufficient balance')
        else:
            self.balance-=amt

    def display(self):
        print(f'balance: {self.balance}')

b1=BackAccount('raj',1000)
b1.deposit(2000)
b1.withdraw(1000)
b1.display()

