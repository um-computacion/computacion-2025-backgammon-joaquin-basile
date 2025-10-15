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
    def __init__(self, player1, player2):
        self.__turn = None
        self.__player1 = player1
        self.__player2 = player2


    def start(self, starter_player: Player):
        self.__turn = starter_player

    def get_turn(self)-> Player:
        return self.__turn
    
    def next_turn(self)-> Player:
        self.__turn = self.__player1 if self.__turn is self.__player2 else self.__player2
        return self.__turn
