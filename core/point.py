class Point():
    '''
    Representa una aguja que contiene fichas
    Attributes:
        color (str): El color de la ficha ('w' o 'b')
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

    def get_quantity(self):
        pass

    def get_color(self):
        pass

    def add_checker(self, color: str)-> bool:
        pass

    def del_checker(self):
        # if self.__quantity > 0:
        #     self.__quantity -= 1
        # else:
        #     raise NoCheckers()
