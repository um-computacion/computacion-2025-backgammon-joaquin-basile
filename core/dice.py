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
        self.__values: dict[int] = [0, 0]
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
        i = index-1
        if i not in [0,1]:
            raise Exception("Indice de dado invalido, debe ser 1 o 2")
        if self.__used[i]:
            raise Exception("El dado ya fue usado")
        dice = self.__values[i]
        self.__used[i] = True
        return dice 

    def get_used(self)-> list[bool]:
        """
        Devuelve una lista con los dados usados
        """
        return self.__used

    def is_all_used(self)-> bool:
        """
        Devuelve si todos los dados fueron usados
        """
        return self.__used[0] and self.__used[1]
