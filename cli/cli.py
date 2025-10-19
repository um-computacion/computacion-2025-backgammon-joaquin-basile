from core.backgammon import Backgammon
class CLI:
    '''
    Interfaz del juego por linea de comandos
    '''
    def __init__(self, backgammon: Backgammon):
        self.__backgammon = backgammon

    def start_cli(self):
        print("Iniciando el juego de Backgammon...")
        name1 = input("Elegir el nombre jugador negro: ")
        name2 = input("Elegir el nombre jugador blanco: ")
        self.__backgammon.with_players(name1, name2)
        print("Se estan girando los dados para decidir quien comienza...")
        retult, starter = self.__backgammon.start_game()
        print("Los resultados fueron: ", result)
        print("El jugador ", starter.get_name(), " comienza!!")

        while not self.__backgammon.end_game():
            self.__backgammon.trow_dice()
