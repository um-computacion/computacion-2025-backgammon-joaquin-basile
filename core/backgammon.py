from core.player import Player 
from core.board import Board
from core.dice import Dice
from core.scheduler import Scheduler
from core.judge import Judge

class Backgammon:
    '''
    Maneja el flujo del juego
    Attributes:
        board (Board): Tablero del juego
        dice (Dice): Dados
        scheduler (Scheduler): Maneja la logica de los turnos
        judge (Judge): Maneja la logica de quien gana el juego
    Methods:
        start_game()-> dict[player: number], starter_player: Inicia el juego tirando los dados y eliguiendo quien comienza
        end_game(): Termina el juego
    '''
    def __init__(
            self, 
            player1: Player,
            player2: Player,
            board: Board, 
            dice: Dice,
            scheduler: Scheduler, 
            judge: Judge
        ):
        self.__player1 = player1
        self.__player2 = player2
        self.__dice = dice
        self.__board = board 
        self.__scheduler = scheduler 
        self.__judge = judge
    
    def start_game(self)-> dict[str, int], Player:
        while self.__dice.get_values()[0] == self.__dice.get_values()[1]:
            self.__dice.roll()
        result = {name1: self.__dice.get_values()[0], name2: self.__dice.get_values()[1]}
        starter_player = self.__player1 if result[name1] > result[name2] else self.__player2
        self.__scheduler.start(starter_player)
        return result, starter_player

    def trow_dice(self)-> list[int]:
        return self.__dice.roll()

    def is_checker_on_bar(self)-> bool:
        return self.__board.is_checker_on_bar(self.__scheduler.get_turn())

    def get_board_state(self)-> list[Point]:
        return self.__board.get_board_state()

    def move_from_bar(self, dice: int):
        current_player = self.__scheduler.get_turn()
        dice_numbers = self.__dice.get_values()
        self.__board.move_from_bar(current_player, dice_numbers[dice])

    def move(self, from_pos: int, dice: int):
        """
        Mueve una ficha en el tablero
        Se indica que ficha y tambien cual de los dos dados usar
        """
        current_player = self.__scheduler.get_turn()
        dice_numbers = self.__dice.get_values()
        self.__board.move_checker(current_player, from_pos, dice_numbers[dice])
        self.__judge()
