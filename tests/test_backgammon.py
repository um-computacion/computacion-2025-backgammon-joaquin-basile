import unittest
from core.const import black, white
from core.exceptions import InvalidMove

from core.backgammon import Backgammon
from core.scheduler import Scheduler
from core.player import Player
from core.dice import Dice
from core.judge import Judge
from core.board import Board

class TestBackgammon(unittest.TestCase):
    def setUp(self):
        self.backgammon = Backgammon()
        self.backgammon.with_players("joaco", "pepe")

    def test_whit_players(self):
        backgammon = Backgammon()
        backgammon.with_players("joaco", "pepe")
        judge: Judge = self.backgammon._Backgammon__judge
        scheduler: Scheduler = self.backgammon._Backgammon__scheduler
        playerB, playerW = scheduler.get_players()
        self.assertEqual(playerW.get_name(), "pepe")
        self.assertEqual(playerB.get_name(), "joaco")
        

    def test_whit_players_same_name(self):
        with self.assertRaises(ValueError):
            self.backgammon.with_players("joaco", "joaco")

    def test_start_game(self):
        backgammon = Backgammon()
        result, starter_player = self.backgammon.start_game()
        p1, p2 = self.backgammon.get_players()
        name1 = p1.get_name()
        name2 = p2.get_name()
        self.assertIn(name1, result)
        self.assertIn(name2, result)
        self.assertIn(starter_player.get_name(), [name1, name2])

    def test_move_invalid_position(self):
        self.backgammon.start_game()
        with self.assertRaises(Exception):
            self.backgammon.move(-2, 1)

    def test_move_occupied(self):
        dice = self.backgammon._Backgammon__dice
        dice.set_values([1, 5])
        scheduler: Scheduler = self.backgammon._Backgammon__scheduler
        scheduler.start(scheduler.get_players()[0])
        with self.assertRaises(InvalidMove):
            self.backgammon.move(6, 2)

    def test_move_no_dice(self):
        scheduler: Scheduler = self.backgammon._Backgammon__scheduler
        scheduler.start(scheduler.get_players()[0])
        with self.assertRaises(InvalidMove):
            self.backgammon.move(1, 2)

    def test_move_from_bar(self):
        dice = self.backgammon._Backgammon__dice
        dice.set_values([1, 5])
        scheduler: Scheduler = self.backgammon._Backgammon__scheduler
        scheduler.start(scheduler.get_players()[0])


    def test_trow_dice(self):
        dice_values = self.backgammon.trow_dice()
        self.assertEqual(len(dice_values), 2)
        self.assertTrue(1 <= dice_values[0] <= 6)
        self.assertTrue(1 <= dice_values[1] <= 6)

    def test_get_used_dice(self):
        self.backgammon.trow_dice()
        used_dice = self.backgammon.get_used_dice()
        self.assertEqual(len(used_dice), 2)
        self.assertFalse(used_dice[0])
        self.assertFalse(used_dice[1])

    def test_is_all_dice_used(self):
        self.backgammon.trow_dice()
        self.assertFalse(self.backgammon.is_all_dice_used())

    def test_actual_player(self):
        self.backgammon.start_game()
        current_player = self.backgammon.actual_player()
        self.assertIn(current_player.get_name(), ["joaco", "pepe"])

    def test_next_turn(self):
        self.backgammon.start_game()
        current_player = self.backgammon.actual_player()
        self.backgammon.next_turn()
        next_player = self.backgammon.actual_player()
        self.assertNotEqual(current_player, next_player)

    def test_get_players(self):
        players = self.backgammon.get_players()
        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].get_name(), "joaco")
        self.assertEqual(players[0].get_color(), black)
        self.assertEqual(players[1].get_name(), "pepe")
        self.assertEqual(players[1].get_color(), white)

    def test_is_checker_on_bar(self):
        self.backgammon.start_game()
        self.assertFalse(self.backgammon.is_checker_on_bar())

    def test_get_board_state(self):
        self.backgammon.start_game()
        board_state = self.backgammon.get_board_state()
        self.assertIsInstance(board_state, list)

    def test_get_bar_state(self):
        self.backgammon.start_game()
        bar_state = self.backgammon.get_bar_state()
        self.assertIsInstance(bar_state, dict)


