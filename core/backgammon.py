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
    
    def start_game(self):
        while self.__dice.get_values()[0] == self.__dice.get_values()[1]:
            self.__dice.roll()
        result = {name1: self.__dice.get_values()[0], name2: self.__dice.get_values()[1]}
        starter_player = self.__player1 if result[name1] > result[name2] else self.__player2
        self.__scheduler.start(starter_player)
        return result, starter_player
    
