# 
class User:		# here's what we have so far
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def execute_transfer(self, other, amount):
        self.account_balance -= amount
        other.account_balance += amount
        self.display_user_balance()
        other.display_user_balance()


Michael = User("Michael")
Bob = User("Bob")
Gertrude = User("Gertrude")


Michael.make_deposit(5)
Michael.make_deposit(10)
Michael.make_deposit(100)
Michael.make_withdrawal(15)
Michael.display_user_balance()


Bob.make_deposit(100)
Bob.make_deposit(50)
Bob.make_withdrawal(25)
Bob.make_withdrawal(25)
Bob.display_user_balance()


Gertrude.make_deposit(99)
Gertrude.make_withdrawal(1)
Gertrude.make_withdrawal(1)
Gertrude.make_withdrawal(2)
Gertrude.display_user_balance()


Michael.execute_transfer(Gertrude,50)
