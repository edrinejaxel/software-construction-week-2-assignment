class Account:
    def __init__(self, account_id, balance, owner_id):
        self.account_id = account_id
        self.balance = balance
        self.owner_id = owner_id

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def can_transfer(self, amount):
        return amount > 0 and amount <= self.balance
