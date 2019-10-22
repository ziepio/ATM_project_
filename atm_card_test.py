import unittest
from atm_card import Card

class CardTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.card = Card(100, 'pz', 16123412341234123412341234, 1234)

    def test_show_PIN(self):
        self.assertEqual(1234, self.card.show_pin())

    def test_PIN_validator(self):
        self.assertEqual(True, self.card.pin_validator())

    def test_unblocked(self):
        self.card.blocked_account = False
        self.assertEqual(False, self.card.is_blocked())

    def test_blocked(self):
        self.card.blocked_account = True
        self.assertEqual(True, self.card.is_blocked())

if __name__ == '__main__':
    unittest.main()
