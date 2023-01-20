'''Create a Bank account with members account number, name, type of account and balance.
Write constructor and methods to deposit at the bank and withdraw an amount from the bank'''

class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!! Welcome to the deposit & Withdraw machine")

    def deposit(self):
        amount = float(input("Enter the amount to be deposited:"))
        self.balance += amount
        print("\nAmount Deposited:",amount)

    def withdraw(self):
        amount = float(input("Enter the amount to be Withdrawn:"))
        if self.balance >= amount:
            self.balance -= amount
            print("Amount Withdrawn is:",amount)
        else:
            print("\nInsufficient balance!!!")

    def display(self):
        print("\nNet available balance = ",self.balance)

s = Bank_Account()
s.deposit()
s.withdraw()
s.display()