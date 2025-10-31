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
        self.mock_board = [Point("", 0)] * 24

    def test_won_checker_player1(self):
        self.judge.won_checker(self.player1)
        points = self.judge.get_points()
        self.assertEqual(points[self.player1], 1)
        self.assertEqual(points[self.player2], 0)

    def test_won_checker_player2(self):
        self.judge.won_checker(self.player2)
        points = self.judge.get_points()
        self.assertEqual(points[self.player1], 0)
        self.assertEqual(points[self.player2], 1)

    def test_check_winner(self):
        for _i in range(12):
            self.judge.won_checker(self.player1)
        winner = self.judge.check_winner()
        self.assertEqual(winner, self.player1)

    def test_check_winner_no_win(self):
        result = self.judge.won_checker(self.player1)
        self.assertEqual(result, None)

    def test_is_all_at_final_black(self):
        for i in range(0, 6):
           self.mock_board[i] = Point(black, 1)
        result = self.judge.is_all_checkers_at_final(self.player1, self.mock_board)
        self.assertTrue(result)

    def test_is_all_at_final_white(self):
        for i in range(18, 24):
            self.mock_board[i] = Point(white, 1)
        result = self.judge.is_all_checkers_at_final(self.player2, self.mock_board)
        self.assertTrue(result)

    def test_is_all_at_final_fail(self):
        self.mock_board[15] = Point(black, 2)
        result = self.judge.is_all_checkers_at_final(self.player1, self.mock_board)
        self.assertFalse(result)


    def test_last_chcker_black(self):
        self.mock_board[1] = Point(black, 1)
        self.mock_board[3] = Point(black, 1)
        last_checker = self.judge.last_checker_pos(self.mock_board, black)
        self.assertEqual(last_checker, 3)

    def test_last_chcker_white(self):
        self.mock_board[23] = Point(white, 1)
        self.mock_board[22] = Point(white, 1)
        last_checker = self.judge.last_checker_pos(self.mock_board, white)
        self.assertEqual(last_checker, 22)


    def test_can_checker_exit_exact_black(self):
        self.mock_board[3] = Point(black, 1)
        result = self.judge.can_checker_exit(self.player1, 3, self.mock_board, 4)
        self.assertTrue(result)

    def test_can_checker_exit_exact_white(self):
        self.mock_board[22] = Point(white, 1)
        result = self.judge.can_checker_exit(self.player2, 22, self.mock_board, 2)
        self.assertTrue(result)

    def test_can_checker_exit_higher_black(self):
        self.mock_board[2] = Point(black, 1)
        self.mock_board[3] = Point(black, 1)
        result = self.judge.can_checker_exit(self.player1, 2, self.mock_board, 6)
        self.assertFalse(result)
        result = self.judge.can_checker_exit(self.player1, 3, self.mock_board, 6)
        self.assertTrue(result)
    
    def test_can_checker_exit_higher_white(self):
        self.mock_board[22] = Point(white, 1)
        self.mock_board[21] = Point(white, 1)
        result = self.judge.can_checker_exit(self.player2, 22, self.mock_board, 6)
        self.assertFalse(result)
        result = self.judge.can_checker_exit(self.player2, 21, self.mock_board, 6)
        self.assertTrue(result)


