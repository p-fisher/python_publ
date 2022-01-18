# 
class User:		# here's what we have so far
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def execute_transfer(self, other, amount):
        self.account_balance -= amount
        other.account_balance += amount
        self.display_user_balance()
        other.display_user_balance()
        return self


Michael = User("Michael")
Bob = User("Bob")
Gertrude = User("Gertrude")


Michael.make_deposit(5).make_deposit(10).make_deposit(100).make_withdrawal(15).display_user_balance()


Bob.make_deposit(100).make_deposit(50).make_withdrawal(25).make_withdrawal(25).display_user_balance()


Gertrude.make_deposit(99).make_withdrawal(1).make_withdrawal(1).make_withdrawal(2).display_user_balance()


Michael.execute_transfer(Gertrude,50)
