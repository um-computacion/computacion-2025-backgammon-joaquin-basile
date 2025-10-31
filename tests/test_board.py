import unittest
from core.const import black, white
from core.player import Player
from core.board import Board
from core.judge import Judge

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Joaco", black)
        self.player2 = Player("Bob", white)
        self.judge = Judge(self.player1, self.player2)
        self.board_with_stole_checkers = Board(self.judge)
        #Esto es unicamente con motivos de testeo
        self.board_with_stole_checkers._Board__bar = {black: 2, white: 1}


    def test_is_checker_on_bar(self):
        print(self.board_with_stole_checkers._Board__bar)
        result = self.board_with_stole_checkers.is_checker_on_bar(self.player1)
        self.assertTrue(result)
        result = self.board_with_stole_checkers.is_checker_on_bar(self.player2)
        self.assertTrue(result)

    def test_move_checker(self):
        board = Board(self.judge)
        board.move_checker(self.player2, 1, 1)

        state = board.get_board_state()

        checkers_first_point = state[0].get_quantity()
        self.assertEqual(checkers_first_point, 1)

        checkers_second_point = state[1].get_quantity()
        self.assertEqual(checkers_second_point, 1)

    def test_move_checker_and_stole(self):
        board = Board(self.judge)
        #Primer moviemiento deja una aguja con 1 ficha en el lugar 3
        board.move_checker(self.player2, 1, 3)
        #El segundo jugador roba esa la ficha de la aguja 3
        board.move_checker(self.player1, 6, 2)
        white_bar = board.get_bar_state().get(white)
        self.assertEqual(white_bar, 1)

    def test_is_checker_on_bar(self):
        result = self.board_with_stole_checkers.is_checker_on_bar(self.player1)
        self.assertTrue(result)

        result = self.board_with_stole_checkers.is_checker_on_bar(self.player2)
        self.assertTrue(result)

    def test_move_from_black_bar(self):
        self.board_with_stole_checkers.move_from_bar(self.player1, 2)
        board = self.board_with_stole_checkers.get_board_state()
        self.assertEqual(board[22].get_quantity(), 1)

    def test_move_from_white_bar(self):
        self.board_with_stole_checkers.move_from_bar(self.player2, 4)
        board = self.board_with_stole_checkers.get_board_state()
        self.assertEqual(board[3].get_quantity(), 1)

    # def test_won_checker_black(self):
    #     board = Board(self.judge)
    #     mock_board = [Point(white, 1)] * 25
    #     for i in range(0, 6):
    #         mock_board[i] = Point(black, 1)
    #     board._Board__points = mock_board
    #
    #     # Debe fallar por no ser numero exacto
    #     with self.assertRaises(InvalidMove):
    #         board.move_checker(self.player1, 1, 6)
    #     
    #     board.move_checker(self.player1, 6, 6)
    #     self.assertEqual(self.judge.get_points()[self.player1], 1)
    #     self.assertEqual(board.get_board_state()[5].get_quantity(), 0)
    #
    #     with self.assertRaises(InvalidMove):
    #         board.move_checker(self.player1, 1, 6)
    #

