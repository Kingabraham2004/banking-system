import random


def verify_type_or_raise_error(value, expected_type):
    if not isinstance(value, expected_type):
        raise TypeError(f"Please provide an object of class {expected_type} not a {type(value)}")
    return value


class Bank:
    def __init__(self, name, pid):
        self.name = name
        self.pid = verify_type_or_raise_error(pid, int)
        self.hq_address = ""
        self.accounts = []
        self.user_count = 0

    def create_account(self, account_holder):
        self.user_count += 1
        account_number = str(self.pid) + str(random.randint(100000, 999999))
        account = Account(account_holder, self, account_number)
        self.accounts.append(account)
        account_holder.accounts.append(account)
        print(f"{account_holder.name} has created a new {self.name} account with account number {account_number}")


class KudaBank(Bank):
    def __init__(self, name, pid):
        Bank.__init__(self, name, pid)
        self.hq_address = "Lagos, Nigeria"

    def create_account(self, account_holder):
        Bank.create_account(self, account_holder)
        print(f"Welcome to {self.name} bank! We're glad you've chosen us.")


class ZenithBank(Bank):
    def __init__(self, name, pid):
        Bank.__init__(self, name, pid)
        self.hq_address = "Lagos, Nigeria"

    def create_account(self, account_holder):
        Bank.create_account(self, account_holder)
        print(f"At {self.name} bank, we're always at your service.")


class AccessBank(Bank):
    def __init__(self, name, pid):
        Bank.__init__(self, name, pid)
        self.hq_address = "Lagos, Nigeria"

    def create_account(self, account_holder):
        Bank.create_account(self, account_holder)
        print(f"{self.name} bank: Banking made easy.")


class User:
    def __init__(self, name):
        self.name = name
        self.accounts = []


class Account:
    def __init__(self, account_holder, bank, account_number):
        self.account_holder = verify_type_or_raise_error(account_holder, User)
        self.bank = verify_type_or_raise_error(bank, Bank)
        self.account_number = account_number
        self.account_balance = 1000

    def deposit(self, amount):
        if amount < 500 or amount > 1000:
            print("Error: Invalid deposit amount. Please deposit an amount between 500 and 1000.")
            return
        self.account_balance += amount
        print(f"{self.account_holder.name} has deposited {amount} into their{self.account_balance}")

