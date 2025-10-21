from core.player import Player 
from core.board import Board
from core.dice import Dice
from core.scheduler import Scheduler
from core.judge import Judge
from core.point import Point
from core.const import black, white

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
    def __init__(self):
        self.__player1: Player
        self.__player2: Player
        self.__judge: Judge
        self.__scheduler: Scheduler 
        self.__dice = Dice()
        self.__board = Board() 

    def actual_player(self):
        return self.__scheduler.get_turn()

    def next_turn(self):
        self.__scheduler.next_turn()

    def with_players(self, name1, name2)-> None:
        self.__player1 = Player(name1, black)
        self.__player2 = Player(name2, white)
        self.__scheduler = Scheduler(self.__player1, self.__player2)

    def start_game(self)-> tuple[dict[str, int], Player]:
        """
        Inicia el juego y elige quien comienza
        """
        while self.__dice.get_values()[0] == self.__dice.get_values()[1]:
            self.__dice.roll()
        name1 = self.__player1.get_name()
        name2 = self.__player2.get_name()
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

    def get_bar_state(self)-> dict:
        return self.__board.get_bar_state()

    def move(self, from_pos: int, dice: int):
        """
        Mueve una ficha en el tablero
        Se indica que ficha y tambien cual de los dos dados usar
        """
        if self.is_checker_on_bar():
            raise Exception("Hay fichas en el bar, no se puede mover otra ficha")
        current_player = self.__scheduler.get_turn()
        dice_numbers = self.__dice.get_values()
        self.__board.move_checker(current_player, from_pos, self.__dice.use_dice(dice))

    def move_from_bar(self, dice: int):
        """
        Mueve la ficha desde el bar
        Se indica solo que dado usar
        """
        current_player = self.__scheduler.get_turn()
        dice_numbers = self.__dice.get_values()
        self.__board.move_from_bar(current_player, dice_numbers[dice])

    def end_game(self)-> bool:
        return False
