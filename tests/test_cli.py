import unittest
from unittest.mock import Mock, patch, call
from cli.cli import CLI
from core.backgammon import Backgammon
from core.player import Player
from core.const import black, white
from core.point import Point

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.mock_backgammon = Mock(spec=Backgammon)
        self.cli = CLI(self.mock_backgammon)

    @patch('builtins.input', side_effect=['Jugador1', 'Jugador2'])
    @patch('builtins.print')
    @patch('cli.cli.sleep')
    def test_start_cli_initialization(self, mock_sleep, mock_print, mock_input):
        """Test que el CLI inicializa correctamente con los nombres de jugadores"""
        self.mock_backgammon.with_players = Mock()
        self.mock_backgammon.start_game = Mock(return_value=({'Jugador1': 5, 'Jugador2': 3}, Mock()))
        self.mock_backgammon.get_winner = Mock(return_value=Mock(get_name=Mock(return_value='Jugador1')))
        self.mock_backgammon.actual_player = Mock()
        self.mock_backgammon.trow_dice = Mock()
        self.mock_backgammon.next_turn = Mock()
        
        with patch.object(self.cli, 'turn'):
            self.cli.start_cli()
        
        self.mock_backgammon.with_players.assert_called_once_with('Jugador1', 'Jugador2')
        self.mock_backgammon.start_game.assert_called_once()


    @patch('builtins.input', side_effect=KeyboardInterrupt())
    @patch('builtins.print')
    def test_start_cli_keyboard_interrupt(self, mock_print, mock_input):
        """Test que el juego maneja correctamente KeyboardInterrupt"""
        self.cli.start_cli()
        mock_print.assert_any_call("\nSe termino el juego!")

    @patch('builtins.input', side_effect=['5', '1'])
    @patch('builtins.print')
    def test_turn_without_bar(self, mock_print, mock_input):
        """Test turno sin fichas en el bar"""
        self.mock_backgammon.is_checker_on_bar = Mock(return_value=False)
        self.mock_backgammon.is_all_dice_used = Mock(return_value=True)
        self.mock_backgammon.move = Mock()
        
        with patch.object(self.cli, 'display_board'):
            self.cli.turn()
        
        self.mock_backgammon.move.assert_called_once_with(5, 1)

    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    def test_turn_with_bar(self, mock_print, mock_input):
        """Test turno con fichas en el bar"""
        self.mock_backgammon.is_checker_on_bar = Mock(return_value=True)
        self.mock_backgammon.is_all_dice_used = Mock(return_value=True)
        self.mock_backgammon.move_from_bar = Mock()
        
        with patch.object(self.cli, 'display_board'):
            self.cli.turn()
        
        self.mock_backgammon.move_from_bar.assert_called_once_with(2)

    @patch('builtins.input', side_effect=['5', '1', 's'])
    @patch('builtins.print')
    def test_turn_with_exception_omit(self, mock_print, mock_input):
        """Test que permite omitir turno cuando hay una excepción"""
        self.mock_backgammon.is_checker_on_bar = Mock(return_value=False)
        self.mock_backgammon.is_all_dice_used = Mock(return_value=True)
        self.mock_backgammon.move = Mock(side_effect=Exception("Movimiento inválido"))
        
        with patch.object(self.cli, 'display_board'):
            self.cli.turn()
        
        # Fixed: Check if the exception message appears in any print call
        printed_messages = [str(call[0][0]) if call[0] else '' for call in mock_print.call_args_list]
        self.assertTrue(any("Movimiento inválido" in msg for msg in printed_messages))

    @patch('builtins.input', side_effect=['5', '1', 'n', '10', '2'])
    @patch('builtins.print')
    def test_turn_with_exception_no_omit(self, mock_print, mock_input):
        """Test que permite reintentar cuando no se omite el turno"""
        self.mock_backgammon.is_checker_on_bar = Mock(return_value=False)
        self.mock_backgammon.is_all_dice_used = Mock(side_effect=[False, True])
        self.mock_backgammon.move = Mock(side_effect=[Exception("Movimiento inválido"), None])
        
        with patch.object(self.cli, 'display_board'):
            self.cli.turn()
        
        self.assertEqual(self.mock_backgammon.move.call_count, 2)

    @patch('builtins.print')
    def test_display_board(self, mock_print):
        """Test que el tablero se muestra correctamente"""
        mock_points = [Point('', 0) for _ in range(24)]
        mock_points[0] = Point(black, 3)
        mock_points[23] = Point(white, 2)
        
        # Fixed: Mock all methods called in display_board
        self.mock_backgammon.get_board_state = Mock(return_value=mock_points)
        self.mock_backgammon.get_bar_state = Mock(return_value={black: 1, white: 0})
        
        mock_player = Mock()
        mock_player.get_name = Mock(return_value='TestPlayer')
        mock_player.get_color = Mock(return_value=black)
        self.mock_backgammon.actual_player = Mock(return_value=mock_player)
        self.mock_backgammon.get_dice_values = Mock(return_value=[3, 5])
        self.mock_backgammon.get_used_dice = Mock(return_value=[False, False])
        
        self.cli.display_board()
        
        self.mock_backgammon.get_board_state.assert_called_once()
        self.mock_backgammon.get_bar_state.assert_called_once()
        # Verificar que se imprime el tablero
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=['10', '1'])
    @patch('builtins.print')
    def test_turn_whithout_bar(self, mock_print, mock_input):
        """Test método turn_whithout_bar específicamente"""
        self.mock_backgammon.move = Mock()
        
        self.cli.turn_whithout_bar()
        
        self.mock_backgammon.move.assert_called_once_with(10, 1)

    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    def test_turn_whith_bar(self, mock_print, mock_input):
        """Test método turn_whith_bar específicamente"""
        self.mock_backgammon.move_from_bar = Mock()
        
        self.cli.turn_whith_bar()
        
        self.mock_backgammon.move_from_bar.assert_called_once_with(2)
        mock_print.assert_any_call("Tienes fichas en el bar!!")

    @patch('builtins.input', side_effect=['5', '1', '6', '2'])
    @patch('builtins.print')
    def test_turn_recursive_call(self, mock_print, mock_input):
        """Test que turn se llama recursivamente si no se usaron todos los dados"""
        self.mock_backgammon.is_checker_on_bar = Mock(return_value=False)
        # Fixed: The turn method is called recursively, need more False values
        self.mock_backgammon.is_all_dice_used = Mock(side_effect=[False, True])
        self.mock_backgammon.move = Mock()
        
        with patch.object(self.cli, 'display_board'):
            self.cli.turn()
        
        self.assertEqual(self.mock_backgammon.move.call_count, 2)

    @patch('builtins.input', side_effect=['Jugador1', 'Jugador2'])
    @patch('builtins.print')
    @patch('cli.cli.sleep')
    def test_start_cli_displays_dice_results(self, mock_sleep, mock_print, mock_input):
        """Test que muestra los resultados de los dados al inicio"""
        mock_winner = Mock()
        mock_winner.get_name = Mock(return_value='Jugador1')
        
        self.mock_backgammon.with_players = Mock()
        self.mock_backgammon.start_game = Mock(return_value=({'Jugador1': 6, 'Jugador2': 2}, Mock()))
        self.mock_backgammon.get_winner = Mock(return_value=mock_winner)
        self.mock_backgammon.actual_player = Mock()
        self.mock_backgammon.trow_dice = Mock()
        self.mock_backgammon.next_turn = Mock()
        
        with patch.object(self.cli, 'turn'):
            self.cli.start_cli()
        
        # Verificar que se imprimieron los valores de los dados
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any('Jugador1' in str(call) and '6' in str(call) for call in calls))

    @patch('builtins.print')
    def test_display_board_with_bar_checkers(self, mock_print):
        """Test que muestra correctamente las fichas en el bar"""
        mock_points = [Point('', 0) for _ in range(24)]
        
        # Fixed: Mock all methods called in display_board
        self.mock_backgammon.get_board_state = Mock(return_value=mock_points)
        self.mock_backgammon.get_bar_state = Mock(return_value={black: 2, white: 1})
        
        mock_player = Mock()
        mock_player.get_name = Mock(return_value='TestPlayer')
        mock_player.get_color = Mock(return_value=white)
        self.mock_backgammon.actual_player = Mock(return_value=mock_player)
        self.mock_backgammon.get_dice_values = Mock(return_value=[4, 2])
        self.mock_backgammon.get_used_dice = Mock(return_value=[True, False])
        
        self.cli.display_board()
        
        # Verificar que se llamaron los métodos necesarios
        self.mock_backgammon.get_bar_state.assert_called_once()
        self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()
