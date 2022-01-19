#
class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        
        # don't worry about user info here; we'll involve the User class soon
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
        else:
            # print(f"Your balance ({self.balance} ) is too low for this withdrawal amount ( {amount} ).")
            print(f"Insufficient funds: charging a $5 fee. Sorry, but we are a bank and like money more than you.")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"My Balance: {self.balance}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_summary(cls):
        for account in cls.accounts:
            account.display_account_info()

money_market = BankAccount(.05,1000)
savings = BankAccount(.01,500)

money_market.deposit(50).deposit(100).deposit(100).withdraw(25).yield_interest().display_account_info()

savings.deposit(500).deposit(100).withdraw(50).withdraw(50).withdraw(100).withdraw(50).yield_interest().display_account_info()

BankAccount.print_all_summary()


# WTF issues
