from core.player import Player
from core.point import Point
from core.const import black, white

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


    def is_all_checkers_at_final(self, player: Player, board: list[Point])-> bool:
        color = player.get_color()
        if color == black:
            start, end = 18, 24  # Último cuadrante para black
        else:
            start, end = 0, 6   # Último cuadrante para white

        checkers_in_final_quadrant = sum(
            board[i].get_quantity() for i in range(start, end) if board[i].get_color() == color
        )
        checker_in_board = sum(point.get_quantity() for point in board if point.get_color() == color)

        return checker_in_board == checkers_in_final_quadrant
