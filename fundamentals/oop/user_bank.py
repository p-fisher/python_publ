#
class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

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
        # print(f"My Balance: {self.balance}")
        # return self
        return f"{self.balance}"

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_summary(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:
    def __init__(self, name):
        self.name = name
        self.checking = BankAccount(.015,1000)

    def make_deposit(self, amount):
        self.checking += amount
        return self

    def make_withdrawal(self, amount):
        self.checking -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.checking.display_account_info()}")
        return self

    # def execute_transfer(self, other, amount):
    #     self.balance -= amount
    #     other.balance += amount
    #     self.display_user_balance()
    #     other.display_user_balance()
    #     return self

mary = User("Mary")
mary.display_user_balance()

#__repr__

# check