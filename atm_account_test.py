import unittest
from atm_account import Account

class AccountTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.acc = Account(100, 'pz', 16123412341234123412341234, 1234)

    def test_name_pos(self):
        self.assertEqual('pz', self.acc.name())

    def test_balance_pos(self):
        self.assertEqual(100, self.acc.balance())

    def test_transfer_pos(self):
        self.assertEqual(True, self.acc.transfer(60))

    def test_transfer_neg(self):
        self.assertEqual(False, self.acc.transfer(0))
        self.assertEqual(False, self.acc.transfer(-10))

if __name__ == '__main__':
    unittest.main()
