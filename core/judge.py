from core.player import Player

class Judge:
    '''
    Maneja la logica de quien gana el juego
    Attributes:
        won_checkers: fichas ganadas de cada jugador
    Methods:
        check_winner(): Decide el ganador del juego
        add_checker(): Agrega una ficha ganada al jugador correspondiente
        get_points(): Devuelve las fichas ganadas de cada jugador
    '''
    def __init__(self, player1: Player, player2: Player):
        self.__won_checkers: dict[str, int] = {player1: 0, player2: 0}

    def check_winner(self) -> Player | None:
        for player, won_checkers in self.__won_checkers.items():
            if won_checkers >= 12:
                return player
        return None
    
    def add_checker(self, player: Player):
        if player in self.__won_checkers:
            self.__won_checkers[player] += 1

    def get_points(self):
        return self.__won_checkers
        
