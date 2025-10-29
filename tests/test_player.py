import unittest
from core.player import Player
from core.const import black, white

class TestPlayer(unittest.TestCase):
    def test_get_name(self):
        player = Player("Joaco", black)
        self.assertEqual(player.get_name(), "Joaco")

    def test_get_color(self):
        player = Player("Joaco", black)
        self.assertEqual(player.get_color(), black)

    def test_get_sign(self):
        player = Player("Joaco", black)
        self.assertEqual(player.get_sign(), -1)

        player2 = Player("Joaco", white)
        self.assertEqual(player2.get_sign(), 1)

    def test_get_oponent(self):
        player = Player("Joaco", black)
        self.assertEqual(player.get_oponent_color(), white)
        player2 = Player("Pepe", white)
        self.assertEqual(player2.get_oponent_color(), black)
