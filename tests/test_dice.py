import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):
    def test_roll_dice(self):
        dice = Dice()
        values = dice.roll()
        self.assertEqual(2, len(values))
        self.assertGreaterEqual(values[0], 1)
        self.assertGreaterEqual(values[1], 1)
        self.assertLessEqual(values[0], 6)
        self.assertLessEqual(values[1], 6)

    def test_get_values(self):
        dice = Dice()
        dice.roll()
        values = dice.get_values()
        self.assertEqual(2, len(values))

    def test_use_dice(self):
        dice = Dice()
        initial_values = dice.roll()

        used_value1 = dice.use_dice(1)
        self.assertEqual(used_value1, initial_values[0])
        self.assertTrue(dice.get_used()[0])

        used_value2 = dice.use_dice(2)
        self.assertEqual(used_value2, initial_values[1])
        self.assertTrue(dice.get_used()[1])

    def test_use_dice_out_index(self):
        dice = Dice()
        dice.roll()
        with self.assertRaises(Exception):
            dice.use_dice(3)

    def test_use_used_dice(self):
        dice = Dice()
        dice.roll()
        dice.use_dice(1)
        with self.assertRaises(Exception):
            dice.use_dice(1)

    def test_is_all_use(self):
        dice = Dice()
        dice.roll()
        self.assertFalse(dice.is_all_used())
        dice.use_dice(1)
        dice.use_dice(2)
        self.assertTrue(dice.is_all_used())

