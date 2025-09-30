import unittest
from core.const import balck, white
from core.player import Player
from core.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board_with_stole_checkers = Board()
        #Esto es unicamente con motivos de testeo
        self.board_with_stole_checkers._Board__bar = {balck: 2, white: 0}

        self.player1 = Player("joaco", black)
        self.player2 = Player("Bob", white)

    def test_move_checker(self):
        board = Board()

        board.move_checker(self.player1, 0, 3)
        self.assertEqual(board.get_board_state()[0].get_checkers(), 1)


    def test_is_checker_on_bar(self):
        pass

    def test_move_from_bar(self):
        pass


