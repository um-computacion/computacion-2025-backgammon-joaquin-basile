import random
class Dice:
    '''
    Maneja la logica de tiradas
    Se podra elegir la cantidad de dados a usar
    Attributes:
        values (list[int]): Valores actuales de los dados
        dice_number (int): Numero de dados a usar
    Methods:
        roll(): Tirar los dados
        set_dice_number(n): Establecer la cantidad de dados a usar
        get_values(): Obtener los valores actuales de los dados
    '''
    def __init__(self, dice_number=2):
        self.__dice_number: int = dice_number
        self.__values: list[int] = []

    def roll(self)-> list[int]:
        self.__values = []
        for _ in range(self.__dice_number):
            self.__values.append(random.randint(1, 6))
        return self.__values

    def set_dice_number(self, new_number: int):
        self.__dice_number = new_number

    def get_dice_number(self)-> int:
        return self.__dice_number

    def get_values(self)-> list[int]:
        return self.__values
