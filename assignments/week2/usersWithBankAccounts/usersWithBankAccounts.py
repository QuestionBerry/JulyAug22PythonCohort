class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.accounts = {
            'checking': BankAccount(0.01),
            'savings': BankAccount(0.04)
            }
        return
    
    def display_info(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points, "\n")
        return self
    
    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print(f"{self.first_name} {self.last_name} is already enrolled.")
        return self
    
    def spend_points(self, amount=int):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print(f"Not enough gold points in {self.first_name}'s account.")
        return self
    
    #newly added methods for usersWithBankAccounts
    def make_deposit(self, amount, acc_type):
        self.accounts[acc_type].deposit(amount)
        return self
    
    def make_withdrawal(self, amount, acc_type):
        self.accounts[acc_type].withdraw(amount)
        return self
    
    def display_user_balance(self):
        print("User:", self.first_name, "\nChecking Balance:", self.accounts['checking'].balance, "\nSavings Balance:",self.accounts['savings'].balance, "\n")
        return self
    
    def transfer_money(self, amount, acc_type, other_user, other_acc_type):
        if self.accounts[acc_type].withdraw(amount): 
            other_user.accounts[other_acc_type].deposit(amount)
        return self

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
            return False
        return self
    
    def display_account_info(self):
        print("Balance:", self.balance)
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.interestRate
        return self


user1 = User("Dalton", "Quesenberry", "dq2505@gmail.com", 28)
user1.make_deposit(250, "checking").display_user_balance()

user2 = User("Lizzi", "Browitt", "elisabethbrowitt@gmail.com", 28)
user2.make_deposit(575, "checking").make_deposit(332, "savings").display_user_balance()

user1.transfer_money(100, "checking", user2, "savings").display_user_balance()
user2.display_user_balance()

user1.transfer_money(300, "savings", user2, "checking").display_user_balance() #should reject because user1 has no balance in savings