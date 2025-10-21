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
        self.__values: list[int] = [0, 0]
        self.__used: list[bool] = [False, False]

    def roll(self)-> list[int]:
        """
        Gira los dados y establece dos valores nuevos a usar
        """
        self.__used = [False, False]
        self.__values = []
        for _ in range(2):
            self.__values.append(random.randint(1, 6))
        return self.__values

    def get_values(self)-> list[int]:
        """
        Devuelve ambos valores
        """
        return self.__values

    def use_dice(self, index: int)-> int:
        """
        Se usa uno de los dados y se marca como usado
        pasar el numero de dado (1 o 2)
        """
        dice = self.__values[index-1]
        self.__used[index-1] = True
        return dice 

    def is_use(self, index: int)-> bool:
        """
        Devuelve true en caso de que ya se haya usado el dado
        tambien recibe el numero de dado (1 o 2)
        """
        return self.__used[index-1]
