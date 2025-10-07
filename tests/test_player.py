import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    def test_get_name(self):
        player = Player("Joaco", "bk")
        self.assertEqual(player.get_name(), "Joaco")

    def test_get_color(self):
        player = Player("Joaco", "bk")
        self.assertEqual(player.get_color(), "bk")

    def test_get_sign(self):
        player = Player("Joaco", "bk")
        self.assertEqual(player.get_sign(), 1)

        player2 = Player("Joaco", "wh")
        self.assertEqual(player2.get_sign(), -1)
