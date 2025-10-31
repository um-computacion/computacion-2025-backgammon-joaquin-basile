import unittest
from core.scheduler import Scheduler
from core.player import Player
from core.const import black, white
from core.backgammon import Backgammon
from core.dice import Dice

class TestBackgammon(unittest.TestCase):
    def setUp(self):
        self.player_b = Player(black, "pepe")
        self.player_w = Player(white, "joaco")
        self.backgammon = Backgammon(self.player_b, self.player_w,)

    def test_whit_players(self):
        self.backgammon.with_players("joaco", "pepe")
        name1 = self.backgammon._Backgammon__player1.get_name()
        self.assertEqual(name1, "joaco")
        name2 = self.backgammon._Backgammon__player2.get_name()
        self.assertEqual(name2, "pepe")

    def test_whit_players_same_name(self):
        with self.assertRaises(ValueError):
            self.backgammon.with_players("joaco", "joaco")

    def test_get_players(self):
        p1, p2 = self.backgammon.get_players()
        self.assertEqual(p1.get_name(), "pepe")
        self.assertEqual(p2.get_name(), "joaco")

    def test_start_game(self):
        result, starter_player = self.backgammon.start_game()
        name1 = self.backgammon._Backgammon__player1.get_name()
        name2 = self.backgammon._Backgammon__player2.get_name()
        self.assertIn(name1, result)
        self.assertIn(name2, result)
        self.assertIn(starter_player.get_name(), [name1, name2])

    def test_move_invalid_position(self):
        self.backgammon.start_game()
        with self.assertRaises(Exception):
            self.backgammon.move(-2, 1)

    def test_move_occupied(self):
        mock_scheduler = Scheduler()
        mock_scheduler._Scheduler__turn = self.backgammon.get_players()[0]
        mock_dice = Dice()._Dice__values = [3, 5]
        self.backgammon._Backgammon__scheduler = mock_scheduler
        self.backgammon._Backgammon__dice = mock_dice
        self.backgammon.move(6, 2)

    
