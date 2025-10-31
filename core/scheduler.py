from core.player import Player
class Scheduler:
    '''
    Maneja la logica de los turnos 
    Attributes:
        turn (Player): Indica el turno actual
        player1 (Player): Jugador 1
        player2 (Player): Jugador 2
    Methods:
        start(Player): Se inicia el scheduler diciendo quien empieza 
        current_player()-> Player: Devuelve el turno actual
        next_turn(): Cambia al siguiente turno
    '''
    def __init__(self, playerB, playerW):
        self.__turn = None
        self.__playerB = playerB
        self.__playerW = playerW


    def start(self, starter_player: Player):
        self.__turn = starter_player

    def get_turn(self)-> Player:
        return self.__turn

    def get_players(self)-> tuple[Player, Player]:
        return self.__playerB, self.__playerW
    
    def next_turn(self)-> Player:
        self.__turn = self.__playerB if self.__turn is self.__playerW else self.__playerW
        return self.__turn
