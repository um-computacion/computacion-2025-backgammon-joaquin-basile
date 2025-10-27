import unittest
from core.judge import Judge
from core.player import Player
from core.point import Point
from core.const import black, white

class TestJudge(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Joaco", black)
        self.player2 = Player("Pepe", white)
        self.judge = Judge(self.player1, self.player2)

    def test_add_checker_player1(self):
        self.judge.add_checker(self.player1)
        points = self.judge.get_points()
        self.assertEqual(points[self.player1], 1)
        self.assertEqual(points[self.player2], 0)

    def test_add_checker_player2(self):
        self.judge.add_checker(self.player2)
        points = self.judge.get_points()
        self.assertEqual(points[self.player1], 0)
        self.assertEqual(points[self.player2], 1)

    def test_check_winner(self):
        for _i in range(12):
            self.judge.add_checker(self.player1)
        winner = self.judge.check_winner()
        self.assertEqual(winner, self.player1)

    def test_check_winner_no_win(self):
        result = self.judge.add_checker(self.player1)
        self.assertEqual(result, None)

    def test_is_all_at_final_black(self):
        mock_board = [Point("", 0)] * 25
        for i in range(18, 24):
            mock_board[i] = Point(black, 1)
        result = self.judge.is_all_checkers_at_final(self.player1, mock_board)
        self.assertTrue(result)

    def test_is_all_at_final_white(self):
        mock_board = [Point("", 0)] * 25
        for i in range(0, 6):
            mock_board[i] = Point(white, 1)
        result = self.judge.is_all_checkers_at_final(self.player2, mock_board)
        self.assertTrue(result)

    def test_is_all_at_final_fail(self):
        mock_board = [Point(black, 1)] * 25
        result = self.judge.is_all_checkers_at_final(self.player1, mock_board)
        self.assertFalse(result)
