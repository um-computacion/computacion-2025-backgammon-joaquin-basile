from core.exceptions import InvalidMove, NoCheckers
from core.const import black, white

class Point():
    '''
    Representa una aguja que contiene fichas
    Attributes:
        color (str): El color de la ficha ('wh' o 'bk')
        quantity (int): La cantidad de fichas en la aguja
    Methods:
        get_quantity(): Devuelve cuantas fichas hay en la aguja
        get_color(): Devuelve de que color son las fichas
        add_checker(color)-> stolen: Agrega una ficha del color especificado a la aguja y devolver si hubo un robo
        del_checker(): Remueve una ficha de la aguja
    '''
    def __init__(self, color, quantity):
        self.__color = color
        self.__quantity = quantity

    def get_quantity(self)-> int:
        return self.__quantity

    def get_color(self)-> str:
        return self.__color

    def add_checker(self, color: str)-> bool:
        if self.__color == "":
            self.__color = color  # Asignar el color correctamente
            self.__quantity += 1
            return False

        if self.__color == color:
            self.__quantity += 1
            return False

        if self.__quantity <= 1:
            self.__color = color
            self.__quantity = 1
            return True

        else:
            raise InvalidMove()

    def del_checker(self)-> None:
        self.__quantity -= 1
