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
        self.user_count +=1
        account_number = str(self.pid) + str(random.randint(100000, 999999))
        account = Account(account_holder, self, account_number)
        self.accounts.append(account)
        account_holder.accounts.append(account)
        print(f'{account_holder.name} has created a new {self.name} account with account number {account_number}')

class KudaBank(Bank):
    def __init__(self, name, pid):
       Bank.__init__(self, name, pid )
       self.hq_address = 'Bornu,Nigeria'

    def create_account(self, account_holder):
       Bank.create_account(self, account_holder)
       print(f'At {self.name} bank, we\'re always at your service.')
class AccessBank(Bank):
    def __init__(self, name, pid):
       Bank.__init__(self, name, pid )
       self.hq_address = 'FCT,Nigeria'

    def create_account(self, account_holder):
       Bank.create_account(self, account_holder)
       print(f'At {self.name} bank, One day you go make am!!')
class ZenithBank(Bank):
    def __init__(self, name, pid):
       Bank.__init__(self, name, pid )
       self.hq_address = 'Bornu,Nigeria'

    def create_account(self, account_holder):
       Bank.create_account(self, account_holder)
       print(f'At {self.name} bank, we\'re always at your service.')


class User:
    def __init__(self, name):
		self.name = name
		self.accounts = []


class Account:
	def __init__(self, account_holder, bank):
		self.account_holder = verify_type_or_raise_error(account_holder, User)
		self.bank = verify_type_or_raise_error(bank, Bank)
		self.account_number = # concatenantion of bank's pid and 6 digit number
		self.account_balance = 1000