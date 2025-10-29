from core.point import Point
from core.const import black, white
from core.judge import Judge
from core.player import Player
from core.exceptions import InvalidMove 

class Board:
    '''
    Maneja la logica de casillas y fichas
    Decide si un jugador puede o no mover una ficha
    Attributes:
        points (list[point]): Lista de agujas que representan el tablero
        bar (map(color: checkers)): Lista de fichas en la barra

    Methods:
        move_checker(player, from_pos, to_pos): Mueve una ficha de una casilla a otra
        get_board_state(): Devuelve el estado actual del tablero
        is_checker_on_bar(): Revisa si el jugador tiene fichas robadas
    '''
    def __init__(self, judge: Judge):
        # Estado inicial del tablero segun las reglas
        self.__points = [
        Point(white, 2), Point('', 0), Point('', 0), Point('', 0), Point('', 0), Point(black, 5),
        Point('', 0), Point(black, 3), Point('', 0), Point('', 0), Point('', 0), Point(white, 5),

        Point(black, 5), Point('', 0), Point('', 0), Point('', 0), Point(white, 3), Point('', 0),
        Point(white, 5), Point('', 0), Point('', 0), Point('', 0), Point('', 0), Point(black, 2)
        ]
        self.__bar = {black: 0, white: 0}
        self.__judge = judge

    def is_checker_on_bar(self, player: Player)-> bool:
        return self.__bar[player.get_color()] > 0
    
    def move_checker(self, player: Player, index: int, dice_number: int):
        from_pos = index - 1
        pos_to_move = (from_pos) + (dice_number * player.get_sign())

        if self.__points[from_pos].get_quantity() < 0:
            raise InvalidMove("No hay fichas en la posicion indicada")

        stole = self.__points[pos_to_move].add_checker(player.get_color())
        self.__points[from_pos].del_checker()

        if stole:
            self.__bar[player.get_oponent_color()] += 1

    def move_from_bar(self, player: Player, dice_number: int):
        pos_to_move = (dice_number - 1) * player.get_sign()
        self.__points[pos_to_move].add_checker(player.get_color())
        self.__bar[player.get_color()] -= 1

    def get_board_state(self)-> list[Point]:
        return self.__points
    
    def get_bar_state(self)-> dict:
        return self.__bar.copy()

if __name__ == "__main__":
    p1 = Player("Joaco", black)
    p2 = Player("Pepe", white)
    board = Board(Judge(p1, p2))
    board.is_all_checkers_at_final(p1)

