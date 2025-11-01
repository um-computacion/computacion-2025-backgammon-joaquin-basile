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
    def __init__(self):
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

    def set_values(self, values: list[int]):
        self.__values = values

    def set_used(self, used: list[bool]):
        self.__used = used
    
    def get_value(self, index: int)-> int:
        """
        Devuelve el valor de un dado
        pasar el numero de dado (1 o 2)
        """
        return self.__values[index-1]

    def use_dice(self, index: int):
        """
        Se marca el dado como usado
        pasar el numero de dado (1 o 2)
        """
        i = index-1
        dice = self.__values[i]
        self.__used[i] = True

    def get_used(self)-> list[bool]:
        """
        Devuelve una lista con los dados usados
        """
        return self.__used
    
    def is_used(self, index: int)-> bool:
        return self.__used[index-1]

    def is_all_used(self)-> bool:
        """
        Devuelve si todos los dados fueron usados
        """
        return self.__used[0] and self.__used[1]
