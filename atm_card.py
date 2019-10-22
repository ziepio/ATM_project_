'''Card allows to:
    -> display PIN number
    -> validate PIN number, eg. to use an ATM
    -> block account if invalid PIN given 3 times
'''

from atm_account import Account

class Card(Account):

    pin_counter = 3
    blocked_account = False

    def show_pin(self):
        print(self.pin)
        return self.pin

    def pin_validator(self):
        if self.pin_counter != 0:
            check_pin = int(input('Enter your pin number: '))
            if check_pin != self.pin:
                self.pin_counter -= 1
                print(f'Incorrect PIN number. {self.pin_counter} attempts left.')
                return self.pin_validator()
            elif check_pin == self.pin:
                print("Correct PIN number.")
                return True
        else:
            print("You account have been blocked due to incorrect PIN number given 3 times.")
            self.blocked_account = True
            return False

    def is_blocked(self):
        print(self.blocked_account)
        return self.blocked_account


# c = Card(100, 'pz', 16123412341234123412341234, 1234)
# c.show_pin()
# c.is_blocked()
# c.pin_validator()
# c.is_blocked()
