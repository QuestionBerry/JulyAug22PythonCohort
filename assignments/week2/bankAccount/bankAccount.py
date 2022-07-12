class BankAccount:

    allAccounts = []

    def __init__(self, interestRate,  balance=0):
        self.interestRate = interestRate
        self.balance = balance
        BankAccount.allAccounts.append(self)
        return
    
    @classmethod
    def display_all_accounts(cls):
        for account in cls.allAccounts:
            print("Balance:", account.balance)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print("Balance:", self.balance)
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.interestRate
        return self


account1 = BankAccount(0.04)
account2 = BankAccount(0.02)

account1.deposit(200).deposit(538).deposit(199).yield_interest().display_account_info()
account2.deposit(350).deposit(19).withdraw(100).withdraw(125).withdraw(99).withdraw(200).yield_interest().display_account_info()

BankAccount.display_all_accounts()