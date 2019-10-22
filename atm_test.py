import unittest
from atm import Atm

class ATMTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.a = Atm(100, 'pz', 16123412341234123412341234, 1234)

    def test_PIN_validator(self):
        self.assertEqual(True, self.a.pin_validator())

    def test_withdraw_cash_pos(self):
        self.assertEqual(True, self.a.transfer(20))

    def test_withdraw_cash_neg(self):
        self.assertEqual(False, self.a.transfer(0))
        self.assertEqual(False, self.a.transfer(-21.5))

    def test_new_pin(self):
        self.a.change_pin(4321)
        self.assertEqual(4321, self.a.show_pin())

if __name__ == '__main__':
    unittest.main()
