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
        if self.__points[from_pos].get_quantity() <= 0:
            raise InvalidMove("No hay fichas en la posicion indicada")
        if player.get_color() != self.__points[from_pos].get_color(): 
            raise InvalidMove("La ficha en la posicion indicada no es tuya")

        if pos_to_move >= 0 and pos_to_move <= 23:
            stole = self.__points[pos_to_move].add_checker(player.get_color())
            self.__points[from_pos].del_checker()
            if stole: 
                self.__bar[player.get_oponent_color()] += 1
        else:
            if not self.__judge.is_all_checkers_at_final(player, self.__points):
                raise InvalidMove("No todas las fichas estan en el cuadrante final")

            if not self.__judge.can_checker_exit(player, from_pos, self.__points, dice_number):
                raise InvalidMove("No es posible sacar la ficha con el valor del dado")

            self.__points[from_pos].del_checker()
            self.__judge.won_checker(player)

    def move_from_bar(self, player: Player, dice_number: int):
        from_pos = 0
        if player.get_color() == black:
            from_pos = 24
        else:
            from_pos = -1
        pos_to_move = from_pos + (dice_number * player.get_sign())

        stole = self.__points[pos_to_move].add_checker(player.get_color())
        self.__bar[player.get_color()] -= 1
        if stole:
            self.__bar[player.get_oponent_color()] += 1

    def get_board_state(self)-> list[Point]:
        return self.__points
    
    def get_bar_state(self)-> dict:
        return self.__bar.copy()
