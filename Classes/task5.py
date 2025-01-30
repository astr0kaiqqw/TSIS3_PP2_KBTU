class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawn: ${amount}. New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive.")

a = Account("John Doe", 100)
a.deposit(50)
a.withdraw(30)
a.withdraw(200)