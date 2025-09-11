import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):
    def test_get_dice_number(self):
        dice = Dice(3)
        self.assertEqual(3, dice.get_dice_number())
        dice2 = Dice(2)
        self.assertEqual(2, dice2.get_dice_number())

    def test_set_dice_number(self):
        dice = Dice(0)
        dice.set_dice_number(2)
        self.assertEqual(2, dice.get_dice_number())

    def test_roll_dice(self):
        dice = Dice(2)
        values = dice.roll()
        self.assertEqual(2, len(values))
        self.assertGreaterEqual(values[0], 1)
        self.assertGreaterEqual(values[1], 1)
        self.assertLessEqual(values[0], 6)
        self.assertLessEqual(values[1], 6)

    def test_get_values(self):
        dice = Dice(2)
        dice.roll()
        values = dice.get_values()
        self.assertEqual(2, len(values))
