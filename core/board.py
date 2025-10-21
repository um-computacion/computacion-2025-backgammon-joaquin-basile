from core.point import Point
from core.const import black, white
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
    def __init__(self):
        # Estado inicial del tablero segun las reglas
        self.__points = [
        Point(white, 2), Point('', 0), Point('', 0), Point('', 0), Point('', 0), Point(black, 5),
        Point('', 0), Point(black, 3), Point('', 0), Point('', 0), Point('', 0), Point(white, 5),

        Point(black, 5), Point('', 0), Point('', 0), Point('', 0), Point(white, 3), Point('', 0),
        Point(white, 5), Point('', 0), Point('', 0), Point('', 0), Point('', 0), Point(black, 2)
        ]
        self.__bar = {black: 0, white: 0}

    def is_checker_on_bar(self, player)-> bool:
        return self.__bar[player.get_color()] > 0
    
    def move_checker(self, player, from_pos, dice_number):
        board_backup = self.__points.copy()
        point_color = self.__points[from_pos].get_color()
        if player.get_oponent_color() == point_color:
            raise Exception("No se puede mover fichas que no sean tuyas")

        pos_to_move = from_pos + (dice_number * player.get_sign())

        try:
            self.__points[from_pos].del_checker()
            stole = self.__points[pos_to_move].add_checker(player.get_color())
            if stole:
                self.__bar[player.get_oponent_color()] += 1
        except:
            self.__points = board_backup


    def move_from_bar(self, player, dice_number):
        pos_to_move = (dice_number - 1) * player.get_sign()
        self.__points[pos_to_move].add_checker(player.get_color())
        self.__bar[player.get_color()] -= 1

    def get_board_state(self)-> list[Point]:
        return self.__points
    
    def get_bar_state(self)-> dict:
        return self.__bar.copy()
