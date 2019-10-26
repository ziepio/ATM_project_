''' Account allows to:
    -> display owner data
    -> display account balance
    -> transfer cash between two accounts
'''


class Account(object):

    temp_account_balance = 0

    def __init__(self, balance, name, acc, pin):
        self.__balance = balance
        self.__name = name
        self.acc = acc
        self.pin = pin

    def name(self):
        return self.__name

    def balance(self):
        print(self.__balance)
        return self.__balance

    def transfer(self, amount):
        if self.__balance >= 0 and self.__balance >= amount > 0:
            self.__balance = self.__balance - amount
            self.temp_account_balance += amount
            return True
        else:
            return False