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
        if color != "bk" and color != "wh":
            raise ValueError("El color tiene que ser 'bk' or 'wh'")
        self.__color = color
        self.__sign = 1 if color == "bk" else -1

    def get_name(self)-> str:
        return self.__name

    def get_color(self)-> str:
        return self.__color

    def get_sign(self)-> int:
        return self.__sign
