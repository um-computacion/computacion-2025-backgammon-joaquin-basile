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
    def __init__(
            self,
            playerB: Player = None,
            playerW: Player = None,
            judge: Judge = None,
            scheduler: Scheduler = None,
            dice: Dice = Dice(),
            board: Board = None,
        ):
        self.__playerB = playerB
        self.__playerW = playerW
        self.__judge = judge
        self.__scheduler = scheduler
        self.__dice = dice
        self.__board = board

    #Metodos backgammon
    def with_players(self, name1, name2)-> None:
        """
        Recive los nombres de los jugadores e inicializa
        todo lo necesario para que backgammon funcione
        """
        if name1 == name2:
            raise ValueError("Los nombres de los jugadores no pueden ser iguales")

        playerB = Player(name1, black)
        playerW = Player(name2, white)
        self.__scheduler = Scheduler(playerB, playerW)
        self.__judge = Judge(playerB, playerW)
        self.__board = Board(self.__judge)


    def start_game(self)-> tuple[dict[str, int], Player]:
        """
        Inicia el juego y elige quien comienza
        """
        while self.__dice.get_values()[0] == self.__dice.get_values()[1]:
            self.__dice.roll()
        playerB, playerW = self.__scheduler.get_players()
        name1 = playerB.get_name()
        name2 = playerW.get_name()
        result = {name1: self.__dice.get_values()[0], name2: self.__dice.get_values()[1]}
        starter_player = playerB if result[name1] > result[name2] else playerW
        self.__scheduler.start(starter_player)
        return result, starter_player

    def move(self, from_pos: int, dice: int):
        """
        Mueve una ficha en el tablero
        Se indica que ficha y tambien cual de los dos dados usar
        """
        if self.__dice.is_used(dice):
            raise Exception("El dado seleccionado ya fue usado")
        current_player = self.__scheduler.get_turn()
        dice_number = self.__dice.get_value(dice)
        self.__board.move_checker(current_player, from_pos, dice_number)
        self.__dice.use_dice(dice)

    def move_from_bar(self, dice: int):
        """
        Mueve la ficha desde el bar
        Se indica solo que dado usar
        """
        if self.__dice.is_used(dice):
            raise Exception("El dado seleccionado ya fue usado")
        current_player = self.__scheduler.get_turn()
        dice_number = self.__dice.get_value(dice)
        self.__board.move_from_bar(current_player, dice_number)
        self.__dice.use_dice(dice)

    def end_game(self)-> bool:
        return False

    ## Metodos de dice
    def trow_dice(self)-> list[int]:
        return self.__dice.roll()
    def get_dice_values(self)-> list[int]:
        return self.__dice.get_values()
    def get_used_dice(self)-> list[bool]:
        return self.__dice.get_used()
    def is_all_dice_used(self)-> bool:
        return self.__dice.is_all_used()

    ## Metodos de scheduler
    def actual_player(self):
        return self.__scheduler.get_turn()
    def next_turn(self):
        self.__scheduler.next_turn()

    ## Metodos de board
    def is_checker_on_bar(self)-> bool:
        return self.__board.is_checker_on_bar(self.__scheduler.get_turn())
    def get_board_state(self)-> list[Point]:
        return self.__board.get_board_state()
    def get_bar_state(self)-> dict:
        return self.__board.get_bar_state()
