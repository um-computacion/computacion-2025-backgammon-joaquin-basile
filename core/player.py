from core.const import black, white

class Player:
    '''
    Representa a uno de los jugadores
    Attributes:
        name (str): Nombre del jugador
        color (str): Color de las fichas del jugador
        sign (int): Signo que indica el sentido de movimiento 
    '''
    def __init__(self, name, color):
        self.__name = name
        if color != black and color != white: 
            raise ValueError("El color tiene que ser 'bk' or 'wh'")
        self.__color = color
        self.__sign = -1 if color == black else 1

    def get_name(self)-> str:
        return self.__name

    def get_color(self)-> str:
        return self.__color

    def get_sign(self)-> int:
        return self.__sign

    def get_oponent_color(self) -> str:
        oponent_color = white if self.__color == black else black
        return oponent_color
