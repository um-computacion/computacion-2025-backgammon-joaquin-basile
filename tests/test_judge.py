import unittest
from core.judge import Judge
from core.player import Player

class TestJudge(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Joaco", "bk")
        self.player2 = Player("Pepe", "wh")
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
