'''
OOP & Encapsulation
Task: Create a class BankAccount.
Use a private attribute __balance.
Provide a property balance to read the amount.
Provide a method deposit(amount) that raises a ValueError if the amount is negative
'''

class BankAccount:
    def __init__(self):
        self.__balance = 0

    @property
    def fetch_balance(self):
        return self.__balance 
    
    @fetch_balance.setter
    def fetch_balance(self,amount):
        if amount <= 0:
            raise ValueError
        else :
            self.__balance = amount
    
    def deposit(self,amount):
        if amount < 0:
            raise ValueError
        else:
            self.fetch_balance += amount

# Execution 
try :
    bank_obj = BankAccount()
    bank_obj.deposit(500)
    bank_obj.deposit(-400)
    print(bank_obj.fetch_balance)
except ValueError :
    print("ValueError Occured since amount can not be negative!")
