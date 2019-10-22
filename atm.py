'''Cash machine allows to:
    -> withdraw cash
    -> setup new pin number
'''

from atm_card import Card

class Atm(Card):

    def withdraw_cash(self, sum):
        if self.__balance >= 0 and self.__balance >= sum > 0:
            self.__balance = self.__balance - sum
            return True
        else:
            return False

    def change_pin(self, new_pin):
        self.pin = new_pin




c = Atm(100, 'pz', 16123412341234123412341234, 1234)
c.show_pin()
c.change_pin(4321)
c.show_pin()

c.balance()
c.transfer(50)
print(f'Temp acc bal: {c.temp_account_balance}')