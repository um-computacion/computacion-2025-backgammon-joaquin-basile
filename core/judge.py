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
    def __init__(self, playerB: Player, playerW: Player):
        self.__won_checkers: dict[str, int] = {playerB: 0, playerW: 0}

    def check_winner(self) -> Player | None:
        for player, won_checkers in self.__won_checkers.items():
            if won_checkers >= 15:
                return player
        return None
    
    def won_checker(self, player: Player):
        self.__won_checkers[player] += 1

    def get_points(self)-> dict[Player, int]:
        return self.__won_checkers

    def is_all_checkers_at_final(self, player: Player, board: list[Point])-> bool:
        color = player.get_color()
        final_quadrant: iter 
        if color == black:
            final_quadrant = range(0, 6)
        else:
            final_quadrant = range(18, 24)

        checkers_in_final_quadrant = sum(
            board[i].get_quantity() for i in final_quadrant if board[i].get_color() == color
        )

        checker_in_board = sum(point.get_quantity() for point in board if point.get_color() == color)

        return checker_in_board == checkers_in_final_quadrant
    
    def can_checker_exit(self, player: Player, from_pos: int, board: list[Point], dice_value: int) -> bool:
        color = player.get_color()
        exact_num = 0
        ## Verifica si sale con el numero exacto
        if color == black:
            exact_num = from_pos + 1
        else:
            exact_num = 24 - from_pos
        if dice_value == exact_num:
            return True

        ## Verifica si es el espacio más alejado para salir con el exacto o mas 
        last_checker_pos = self.last_checker_pos(board, color)
        if from_pos == last_checker_pos and dice_value > exact_num:
            return True

        return False
    
    def last_checker_pos(self, board: list[Point], color: str)-> int:
        final_quadrant: iter
        if color == black:
            final_quadrant = range(5, -1, -1)
        else:
            final_quadrant = range(18, 24)
        for i in final_quadrant:
            if board[i].get_quantity() > 0 and board[i].get_color() == color:
                return i
