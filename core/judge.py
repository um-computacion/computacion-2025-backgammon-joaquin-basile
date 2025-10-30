from core.player import Player
from core.point import Point
from core.const import black, white

class Judge:
    '''
    Se encarga de validaciones que tienen que ver con las reglas del juego
    Attributes:
        won_checkers: fichas ganadas de cada jugador
    Methods:
        
    '''
    def __init__(self, player1: Player, player2: Player):
        self.__won_checkers: dict[str, int] = {player1: 0, player2: 0}
        self.__black_last_quadrant = range(0, 6)
        self.__white_last_quadrant = range(18, 24)

    def check_winner(self) -> Player | None:
        for player, won_checkers in self.__won_checkers.items():
            if won_checkers >= 12:
                return player
        return None
    
    def won_checker(self, player: Player):
        if player in self.__won_checkers:
            self.__won_checkers[player] += 1

    def get_points(self):
        return self.__won_checkers

    def is_all_checkers_at_final(self, player: Player, board: list[Point])-> bool:
        color = player.get_color()
        final_quadrant = self.__black_last_quadrant if color == black else self.__white_last_quadrant

        checkers_in_final_quadrant = sum(
            board[i].get_quantity() for i in final_quadrant if board[i].get_color() == color
        )

        checker_in_board = sum(point.get_quantity() for point in board if point.get_color() == color)

        return checker_in_board == checkers_in_final_quadrant
    
    def can_checker_exit(self, player: Player, board: list[Point], dice_value: int) -> bool:
        color = player.get_color()
        final_quadrant = self.__black_last_quadrant if color == black else self.__white_last_quadrant

        # Verificar si el dado permite salir del tablero
        for point_index in final_quadrant:
            point = board[point_index]
            if point.get_color() != color or point.get_quantity() < 0:
                continue

        return False


    def no_possible_moves(self, board: list[Point])-> bool:
        pass


